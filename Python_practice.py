# from unittest.util import _count_diff_all_purpose


# print ("Hello World!")
# counties = ["Arapahoe", "Denver", "Jefferson"]

# print (counties[2])

# len(counties)

# print (counties[0:2])

# print (counties[1:])

# counties.append("El Paso")

# print (counties)

# counties.insert(2, "El Paso")

# print (counties)

# counties.remove("El Paso")

# print (counties)

# counties.pop(3)


# print (counties)

# counties.insert(1, "El Paso")
# counties.pop(0)
# counties.insert(2, "Denver")

# print (counties)

# counties_tuple = ("Arapahoe", "Denver", "Jefferson")

# print(counties_tuple)
# len(counties_tuple)

# counties_dict = {}
# counties_dict["Arapahoe"] = 42289
# print(counties_dict)

# counties_dict["Denver"] = 463353
# counties_dict["Jefferson"] = 432438

# print(counties_dict)

# print(len(counties_dict))

# print(counties_dict.get("Denver"))

voting_data = []
voting_data.append({"county":"Arapahoe", "registered_voters":422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})


voting_data.insert(2, {"county":"El Paso", "registered_voters":461149})


voting_data.remove({"county":"Arapahoe", "registered_voters":422829})

voting_data.remove({"county":"Denver", "registered_voters":463353})
voting_data.insert(3, {"county":"Denver", "registered_voters":463353})
voting_data.append({"county":"Arapahoe", "registered_voters":422829})

print(voting_data)