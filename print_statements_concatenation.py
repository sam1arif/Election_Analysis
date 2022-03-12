# counties_dict = {"Arapahoe": 36927, "Denver": 413229, "Jefferson": 390222}

# for county, voters in counties_dict.items():
#     print(county + " county has " + str(voters) + " registered voters.")


## or to use f string concatenation this is what we do:


# for county, voters in counties_dict.items():
#     print(f"{county} county has {voters} registered voters.")

## multi line f-string

# candidates_votes = int(input("How many votes did the candidate get in the election? "))
# total_votes = int(input("What is the total number of votes in the election? "))

# message_to_candidate = (
#     f"You received {candidates_votes:,} number of votes. "
#     f"The total number of votes in the election was {total_votes:,}. "
#     f"You received {candidates_votes / total_votes * 100: .2f}% of the total votes. ")

# print(message_to_candidate)

# counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

# for county, registered_voters in counties_dict.items():
#     print(f"{county} county has {registered_voters} registered voters.")


## Refer to the following dictionary to complete the activity.
voting_data = [{"county": "Arapahoe", "registered_voters": 422829}, {"county": "Denver", "registered_voters": 463353}, {"county": "Jefferson", "registered_voters": 432438}]

 ## Print each county and registered voter from the dictionary. The output should look like the following:
## Arapahoe county has 422,829 registered voters.
## Denver county has 463,353 registered voters.
## Jefferson county has 432,438 registered voters.