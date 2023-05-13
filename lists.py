# List is a collection which is ordered and changeable. Allows duplicate members.

nums = [1,2,3,4,5]
print(nums)
# [1,2,3,4,5]

fruits = ['banana', 'apple', 'orange']
print(fruits)
# ['banana', 'apple', 'orange']

print (len(fruits))
# 3

### Access List Items ####

print(fruits[1])
# apple

print(fruits[-1])
# Orange

print(fruits[0:2])
# ['banana', 'apple']

if "apple" in fruits:
    print("Yes, Apple is in the list")
# Yes, Apple is in the list

### Change List Items ###
fruits[0] = "kiwi"
print(fruits)
# ['kiwi', 'apple', 'orange']

fruits.insert(2, "blueberry")
print(fruits)
# ['kiwi', 'apple', 'blueberry', 'orange']

### Add List Items ###

fruits.append('grape')
print(fruits)
# ['banana', 'apple', 'orange', 'grape']

#tropical = ["mango", "pineapple", "papaya"]
#tropical = ("mango", "pineapple", "papaya")
tropical = {"mango", "pineapple", "papaya"}
fruits.extend(tropical)
print(fruits)
# ['kiwi', 'apple', 'blueberry', 'orange', 'grape', 'mango', 'pineapple', 'papaya']

### Remove List Items ###

fruits.remove('apple')
print(fruits)
# ['banana', 'orange', 'grape']

fruits.pop(1)
print(fruits)
# ['kiwi', 'orange', 'grape', 'pineapple', 'papaya', 'mango']

del fruits[0]
print(fruits)
# ['orange', 'grape', 'mango', 'pineapple', 'papaya']

fruits.clear()
print(fruits)
# []

del fruits
print(fruits)
# NameError: name 'fruits' is not defined