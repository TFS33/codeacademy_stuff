# Exercise 1:	Write a Python program to find the most common elements and their counts in a specified text
# Original string: lkseropewdssafsdfafkpwe
# Most common three characters of the said string:
# [('s', 4), ('e', 3), ('f', 3)]

def count_chars(og_string):
    counted_char = {}
    for chr in og_string:
        if chr in counted_char:
            counted_char[chr] += 1
        else:
            counted_char[chr] = 1
    return counted_char



og_string = 'lkseropewdssafsdfafkpwe'

counted = count_chars(og_string)

print(counted)

# top trys geras su setu
def return_most_common(text, number=3):
    result =[]
    for l in set(text):
        result.append((l,text.count(l)))
    result.sort(key=lambda x: x[1], reverse=True)
    return result[:3]

text = 'lkseropewdssafsdfafkpwe'



#  Create a list by picking an odd-index items from the first list and even index items from the second
# Given two lists, l1 and l2, write a program to create a third list l3 by picking
# an odd-index element from the list l1 and even index elements from the list l2.
#
# Given:
#
# l1 = [3, 6, 9, 12, 15, 18, 21]
# l2 = [4, 8, 12, 16, 20, 24, 28]
# Expected Output:
#
# Element at odd-index positions from list one
# [6, 12, 18]
# Element at even-index positions from list two
# [4, 12, 20, 28]
#
# Printing Final third list
# [6, 12, 18, 4, 12, 20, 28]

def pick_odd_index(l1):
    odd_index = l1[1::2]
    return odd_index

def pick_even_index(l2):
    even_index = l2[0::2]
    return even_index

def get_new_list(even_index , odd_index):
    new_one = odd_index + even_index
    return new_one

l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]

odd_index = pick_odd_index(l1)
even_index = pick_even_index(l2)
new = get_new_list(even_index, odd_index)

print(new)

# Create a Python set such that it shows the element from both lists in a pair
# Expected Output: {(6, 36), (8, 64), (4, 16), (5, 25), (3, 9), (7, 49), (2, 4)

def get_merged(first_list, second_list):
    return {(x, y) for x, y in zip(first_list, second_list)}
# return set(zip(listas_1, listas_2)) dar geriau

first_list = [2, 3, 4, 5, 6, 7, 8]
second_list = [4, 9, 16, 25, 36, 49, 64]

answer = get_merged(first_list, second_list)

print(answer)


# Iterate a given list and check if a given element exists as a key’s value in a dictionary.
# If not, delete it from the list
# roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
# sample_dict = {'John':47, 'Emma':69, 'Kelly':76, 'Jason':97}

def start_iter(rollas, samples, ): # panaikina priklausomybe nuo rollo ir sample kintamuju
    removed = []
    for number in rollas:
        if number in samples.values():
            removed.append(number)
    return removed

roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sample_dict = {'John':47, 'Emma':69, 'Kelly':76, 'Jason':97}

print(start_iter(roll_number, sample_dict))

# Get all values from the dictionary and add them to a list but don’t add duplicates
# Given:
# speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}
# Expected Outcome:
# [47, 52, 44, 53, 54]

def pick_values(speed):
    pick_dubs = []
    for value in speed.values():
        if value not in pick_dubs:
            pick_dubs.append(value)
    return pick_dubs



speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}


pick_dubs = pick_values(speed)
print(pick_dubs)