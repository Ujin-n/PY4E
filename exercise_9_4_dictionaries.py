name = input("Enter file: ")

if len(name) < 1:
    name = "files/mbox-short.txt"

handle = open(name)

dict_from = dict()

for line in handle:
    if line.startswith("From "):
        dict_from[line.split()[1]] = dict_from.get(line.split()[1], 0) + 1

max_name = None
max_num = None

for name, num in dict_from.items():
    if max_name is None or max_num < num:
        max_name = name
        max_num = num

print(max_name, max_num)