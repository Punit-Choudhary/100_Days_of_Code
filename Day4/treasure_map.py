# Treasure map

map = [
    ['[]', '[]', '[]'],
    ['[]', '[]', '[]'],
    ['[]', '[]', '[]']
]

cordinate = input()

column = int(cordinate[0])
row = int(cordinate[1])

map[row - 1][column - 1] = 'x'

print(f"{map[0]}\n{map[1]}\n{map[2]}")