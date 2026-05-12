with open('questions.txt', 'r') as file:
    blocks = file.read().strip().split('\n\n')

inputs = []
answers = []
results = []

for block in blocks:
    lines = block.splitlines()
    
    question_text = "\n".join(lines[:-1])
    correct_answer = lines[-1]
    
    print(question_text)
    user_choice = input("Your answer: ")
    inputs.append(user_choice)
    answers.append(correct_answer)
    
    if user_choice.lower() == correct_answer.lower():
        results.append(f"Correct: {lines[0]}\n")
    else:
        results.append(f"Incorrect. Correct answer: {correct_answer})\n")
        
    print("Answer registered. Moving on...\n")

print("-" * 20)
print("QUIZ SUMMARY")
print("-" * 20)
for res in results:
    print(res)

correct = sum(1 for i in range(len(inputs)) if inputs[i].lower() == answers[i].lower())
print(f"\nYour final score: {correct} / {len(blocks)}")