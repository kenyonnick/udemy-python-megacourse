# Primitives
anInteger = 1
aFloat = 1.0
aString = "A string"

print("Primitives:", anInteger, aFloat, aString)

# Containers

# Lists
aListOfIntegers = [1, 2, 3]
print(aListOfIntegers)

aListOfFloats = [1.0, 2.0, 3.0]
print(aListOfFloats)

aListOfStrings = ["One", "Two", "Three"]
print(aListOfStrings)

aListOfDifferentPrimitives = [1, 1.0, "One"]
print(aListOfDifferentPrimitives)

# Using the range function
aListUsingRange = list(range(1, 10, 1))
print(aListUsingRange)

# dir command - returns the attributes of a type as strings
# print(dir(list))

# help command - returns the description of an attribute
# help(str.upper)

# Average of a list
theSum = sum(aListOfIntegers)
numberOfElements = len(aListOfIntegers)
theAverage = theSum / numberOfElements
print("The average value of", aListOfIntegers, "is", theAverage)

# Dictionaries
student_grades = {"Mary": 9.1, "John": 8.4, "Miranda": 8.9, "Jeremy": 9.1}
gradeSum = sum(student_grades.values())
numberOfStudents = len(student_grades)
classAverage = gradeSum / numberOfStudents
print("The average grade in the class was", classAverage)

# Tuples
# Tuples are immutable whereas lists are mutable
aTuple = (1, 2, 3)
