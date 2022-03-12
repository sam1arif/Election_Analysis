# While loop

# x = 0
# while x <= 5:
#     print(x)
#     x = x+1

# count = 7
# while count < 1:
#     print("Hello World")


# counties = ["Arapahoe", "Denver", "Jefferson"]

# county = "Arapahoe"
# for county in counties:
#     print(county)

# numbers = [0, 1, 2, 3, 4]

# for num in numbers:
#     print(num)

# for num in range(5):
#     print(num)

# for i in range(len(counties)):
#     print(counties[i])


# counties_tuples = ("Arapahoe", "Denver", "Jefferson") 

# # for i in range(len(counties_tuples)):
# #     print(counties_tuples[i])

# for county in counties_tuples:
#     print(county)

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

# for county in counties_dict:
#     print(county)

# or we can uses keys() like below. And when using keys(), it doesn't matter what variable name we use.

# for county in counties_dict.keys():
#     print(county)

# how to print values?

# for county in counties_dict:
#     print(counties_dict[county])

# another method is to use the get() method in the for loop:

# for county in counties_dict:
#     print(counties_dict.get(county))

# get the key-value paris of dictionaries

# for key, value in counties_dict.items():
#     print(key, value)

# or
# for county, voters in counties_dict.items():
#     print(county, voters)
