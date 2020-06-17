# Functions and Conditionals

# If and else
def mean(aCollection):
    # Mean of a dictionary
    if isinstance(aCollection, dict):
        return sum(aCollection.values()) / len(aCollection)
    # Mean of a list
    else:
        return sum(aCollection) / len(aCollection)


aList = [1, 2, 3]
print("Mean of", aList, "=", mean(aList))

aDictionary = {"Daniel": 1, "Martha": 2, "Ricardo": 3}
print("Mean of", aDictionary, "=", mean(aDictionary))

# Else if


def compare(x, y):
    if x > y:
        return "x is greater than y"
    elif x == y:
        return "x is equal to y"
    else:
        return "x is less than y"


x = 1
y = 2
print("x =", x, "y =", y, "comparison =", compare(x, y))

y = 1
print("x =", x, "y =", y, "comparison =", compare(x, y))

x = 2
print("x =", x, "y =", y, "comparison =", compare(x, y))
