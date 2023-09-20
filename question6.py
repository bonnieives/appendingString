"""

    ASSIGNMENT #1
    QUESTION 6
    AUTHOR: Bonnie Ives de Castro Nunes
    DATE: September 15th, 2023
    
"""

print("Please inform the first string: ")
s1 = input()
print("-------------------")

print("\nPlease inform the second string: ")
s2 = input()
print("-------------------")

lengthS1 = len(s1)
lengthS2 = len(s2)

letterS1 = [char for char in s1]
letterS2 = [char for char in s2]

string = []

for letters1 in range(0,(lengthS1)):    
    
    if letters1 == ((lengthS1 // 2)):       
        for letters2 in range(0,(lengthS2)):            
            string.append(letterS2[letters2])
            
    string.append(letterS1[letters1])

print("\nThe strings informed are "+ s1+ " and "+ s2 + ".")
print("The new string is: " + ''.join(string))
