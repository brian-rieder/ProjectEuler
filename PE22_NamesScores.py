__author__ = 'Brian Rieder'

# Problem 22: Names Scores

# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first
# names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name,
# multiply this value by its alphabetical position in the list to obtain a name score.
#
# For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53,
# is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.
#
# What is the total of all the name scores in the file?


def get_name(fp):
    fp.read(1)
    ch = fp.read(1)
    list1 = []
    while ch != '"':
        list1.append(ch)
        ch = fp.read(1)
    name = ''.join(list1)
    return name


def score_name(one_name, pos):
    i = 0
    score = 0
    for i in range(0, len(one_name)):
        score += ord(one_name[i]) - 64
        i += 1
    score *= pos
    return score


# Main Function

file_ptr = open("names.txt", "r")
name_list = []

while True:
    name = get_name(file_ptr)
    name_list.append(name)
    comma = file_ptr.read(1)
    if comma != ',':
        break

name_list.sort()

ind = 0
total = 0
for name_itr in range(0, len(name_list)):
    total += score_name(name_list[name_itr], name_itr + 1)
print(total)
