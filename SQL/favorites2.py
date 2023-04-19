import csv

with open("favorites.csv", "r") as file:
reader = csv.DictReader(file)
counts ={}
# iterating through the dictionary reader row by row, row will ++ intself after every loop
for row in reader:
    favorite = row["language"]
    if favorite in counts:
        counts[favorite] += 1
    else:
        counts[favorite] = 1

# iterating through a dictionary
for favorite in counts:
    print(f"{favorite}: {counts[favorite]}")

#sorting
for favorite in sorted(counts, reverse=True):
    print(f"{favorite}: {counts[favorite]}")

# sort by top 3
def get_value(language):
    return counts[language]

# key tells sorted, what to sort using as reference and here the function to sort os get_value's
# return which is the number of times a language was picked, it will then output the languages
# at the top being the least favorite since reverse is set to true
for favorite in sorted(counts, key=get_value, reverse=True):
    print(f"{favorite}: {counts[favorite]}")


#creating a separate function of variable just to use at one place is ot recomended and in python
# one use function can be replaced by anonymous function known as lambda
# redoing the get value loop use using a lambda
for favorite in sorted(counts, key=lambda language: counts[language], reverse=True):
    print(f"{favorite}: {counts[favorite]}")

#key=lambda language: counts[language]
# here you declare lamda function the the paramter/argument your are passing to the function followed by a semicolon
# the the return value i.e counts[language] without explicitly stating return and that it
# key will the be assigned to the return value of the lambda function



