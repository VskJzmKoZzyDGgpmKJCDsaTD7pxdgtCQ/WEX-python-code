def process_grades(filename):
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]

    subject_name = lines[0]
    topics = []
    idx = 1
    while idx < len(lines) and not lines[idx].replace('.', '', 1).isdigit():
        if idx + 1 < len(lines) and lines[idx+1].replace('.', '', 1).isdigit():
            break
        topics.append(lines[idx])
        idx += 1

    num_tests = len(topics)
    students = []
    
    while idx < len(lines):
        name = lines[idx]
        try:
            grades = [float(lines[idx + i + 1]) for i in range(num_tests)]
            overall_avg = sum(grades) / len(grades)
            students.append({"name": name, "grades": grades, "avg": overall_avg})
            idx += num_tests + 1
        except (ValueError, IndexError):
            idx += 1

    # --- NEW: SORTING LOGIC ---
    print("How would you like to sort the students?")
    print("1. Alphabetical (by Last Name)")
    print("2. Performance (Best to Worst)")
    choice = input("Enter 1 or 2: ")

    # We need a ranking copy to determine "Top 10%" even if sorted alphabetically
    ranked_students = sorted(students, key=lambda x: x['avg'], reverse=True)
    best_avg = ranked_students[0]['avg']
    worst_avg = ranked_students[-1]['avg']
    num_students = len(students)

    if choice == "1":
        # Sorts by the last word in the 'name' string
        students.sort(key=lambda x: x['name'].split()[-1])
    else:
        students = ranked_students

    print(f"\n--- {subject_name} Analysis ---")
    for i in range(num_tests):
        test_grades = [s["grades"][i] for s in students]
        avg = sum(test_grades) / len(test_grades)
        print(f"Average grade on {topics[i]} = {avg:.2f}%")

    print("\n--- Student Summaries ---")
    
    def get_rating(g):
        if g >= 90: return "amazing"
        if g >= 75: return "good"
        if g >= 50: return "average"
        if g >= 30: return "bad"
        return "terrible"

    for s in students:
        # Topic breakdown
        for i in range(num_tests):
            print(f"{s['name']} did {get_rating(s['grades'][i])} on {topics[i]}")

        best_score = max(s['grades'])
        worst_score = min(s['grades'])
        best_sub = topics[s['grades'].index(best_score)]
        worst_sub = topics[s['grades'].index(worst_score)]
        
        print(f"Result: {s['name']} is {get_rating(best_score)} at {best_sub} "
              f"but {get_rating(worst_score)} at {worst_sub}")

        # Standing logic
        standing = f"Overall, {s['name']} is a {get_rating(s['avg'])} student."
        
        # Check rank position from our pre-sorted list
        rank = ranked_students.index(s) + 1 

        if s['avg'] == best_avg:
            standing += f" {s['name']} is the best student in the class!"
        elif s['avg'] == worst_avg:
            standing += f" {s['name']} is the worst student in the class."
        elif rank <= num_students * 0.1:
            standing += f" {s['name']} is one of the best students in the class (Top 10%)."
        elif rank >= num_students * 0.9:
            standing += f" {s['name']} is one of the worst students in the class (Bottom 10%)."
            
        print(standing + "\n")

if __name__ == "__main__":
    process_grades("names-n-grades.txt")