import re
print(sum([int(x) for x in re.findall('[0-9]+', open("files/regex_sum_1727283.txt").read())]))