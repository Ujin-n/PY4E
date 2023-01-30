name = input("Enter file: ")
if len(name) < 1:
    name = "files/mbox-short.txt"
handle = open(name)

d = dict()

for l in handle:
    if l.startswith("From "):
        h = l.split()[5].split(":")[0]
        d[h] = d.get(h, 0) + 1

l = sorted(d.items())

for v in l:
    print(v[0], v[1])