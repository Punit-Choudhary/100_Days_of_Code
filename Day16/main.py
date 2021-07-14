from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"], align='l')
table.add_column("Type", ["Electric", "Water", "Fire"], align='l')

print(table)