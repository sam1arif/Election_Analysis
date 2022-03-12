## The data we need to retrieve.
## 1. The total number of votes cast
## 2. A complete list of candidates who received votes
## 3. The percentage of votes each candidate won
## 4. The total number of votes each candidate won
## 5. The winner of the election

## Import the datetime class from the datetime module.
import datetime as dt

## Use the now() attribute on the datetime class to get the present time.
now = dt.datetime.now()

## Print the present time.
print("The time right now is ", now)

import csv
import os
## Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

## Open the election results and read the file.
# with open(file_to_load) as election_data:

## To do: perform analysis.
    # print(election_data)

## Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

## Using the open() function with the "w" mode we will write data to the file.
# with open(file_to_save, "w") as txt_file:
    ## Write three counties to the file
    # txt_file.write("Arapahoe, Denver, Jefferson. ")

    ## Or we can write the same three counties with a newline escape sequence (\n).
    ## The newline escape sequence adds "enter" after every value it is typed.
    #txt_file.write("Counties in the Election\n---------------\nArapahoe\nDenver\nJefferson")

## Close file.
#txt_file.close()

with open(file_to_load) as election_data:

## To do: read and analyze the data here.

## Read the file object with the reader function.
    file_reader = csv.reader(election_data)
## Print the header row.
    headers = next(file_reader)
    print(headers)
## Print each row in the CSV file.
    # for row in file_reader:
    #     print(row)
## To get the first item from each row we use the code below or indexing:
    # for row in file_reader:
    #     for i in range(len(row)):
    #         print(row[0])

