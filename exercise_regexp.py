import re

file_name = "files/regex_sum_1727283.txt"
handle = open(file_name)

total_sum = 0

for l in handle:
    num_list = re.findall('[0-9]+', l)
    for n in num_list:
        total_sum = total_sum + int(n)

print(total_sum)