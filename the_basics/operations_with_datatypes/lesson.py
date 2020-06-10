# Append
aList = []
print("A list before appending elements:", aList)
aList.append("Alfred")
aList.append("Beatrice")
aList.append("Charles")
aList.append("Diana")
aList.append("Edward")
aList.append("Fergie")
print("A list after appending elements:", aList)

# Access
print("The first element:", aList[0])
print("Sublist from the 2nd element to the 4th element:", aList[1:3])
print("Sublist from beginning to 4th element:", aList[:3])
print("Sublist from 4th element to the end:", aList[3:])
# Negative indexing
print("The last element:", aList[-1])
print("Sublist of the last 3 elements:", aList[-3:])

# Negative Indexing in strings
aString = "a string"
print("The last three characters of a string:", aString[-3:])

# Chained indexing
aListOfDifferentPrimitives = [1, 1.0, "One"]
print("Chained indexing:", aListOfDifferentPrimitives[-1][-2:])

# Dictionaries

student_grades = {"Mary": 9.1, "John": 8.4, "Miranda": 8.9, "Jeremy": 9.1}
print("Mary's grade:", student_grades["Mary"])
