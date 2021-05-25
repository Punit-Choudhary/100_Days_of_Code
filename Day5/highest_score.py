# Highest Score

scores = list(map(int, input("Enter a list: ").split()))

highest = float('-inf')

for score in scores:
    if score > highest:
        highest = score

print(f"Highest score: {highest}")