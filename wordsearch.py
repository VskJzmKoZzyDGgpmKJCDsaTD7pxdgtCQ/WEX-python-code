import random

words = []

while True:
    word_current = input("Enter a word (or 'end' to stop): ").upper()
    if word_current == "END":
        break
    words.append(word_current)

size_x = int(input("Enter horizontal size: "))
size_y = int(input("Enter vertical size: "))

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

grid = [[random.choice(alphabet) for _ in range(size_x)] for _ in range(size_y)]

for word in words:
    if random.choice([True, False]):
        word = word[::-1]
    
    direction = random.choice([(0, 1), (1, 0), (1, 1)])
    dr, dc = direction 
    
    max_r = size_y - (len(word) * dr)
    max_c = size_x - (len(word) * dc)
    
    if max_r < 0 or max_c < 0:
        print(f"Skipping '{word}' - it's too long for this grid size.")
        continue

    start_r = random.randint(0, max_r)
    start_c = random.randint(0, max_c)
    
    for i in range(len(word)):
        grid[start_r + (i * dr)][start_c + (i * dc)] = word[i]

print("\n--- WORD SEARCH ---\n")
for row in grid:
    print(" ".join(row))
    
print("\nThe words to look for are:")
for i, w in enumerate(words, 1):
    print(f"{i} - {w}")
