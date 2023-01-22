# Use the file name mbox-short.txt as the file name

fname = input("Enter file name: ")
fh = open(fname)

line_count = 0
num = 0.0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    line_count = line_count + 1
    num = num + float(line.split()[1])

print("Average spam confidence:", num / line_count)