# Strings

# Concatenation
#    2 or more strings and put them together

firstName = "Mo"
lastName = "Lester"

print(firstName + " " + lastName)

name = firstName + " " + lastName
lastFirst = lastName + ", " + firstName

print(lastFirst)

# Repetition
# repetition activator

print("Hip "*2 + "Hooray !")

def rowYourBoat():
    print("Row, "*3 + "your boat")
    print("Gently down the stream")
    print("merrily, "*4)
    print("Life is but a dream")


rowYourBoat()

# Indexing

name = "Roy G Biv"
firstChar = name[0]
print(firstChar)

middleCharIndex = len(name) // 2
print(middleCharIndex)
print(name[middleCharIndex])

print(name[-3])

for i in range(1, len(name)):
    print(name[i])

# SLicing and Dicing

print(name[-4:8])

for i in range(0, len(name)+1):
    print(name[0:i])

# Searching

print("biv" in name)

if "y" not in name:
print("y" not in name)