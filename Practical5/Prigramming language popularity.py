my_dict={'JavaScript':62.3, 'HTML':52.9, 'Python':51, 'SQL':51, 'TypeScript':38.5}
# Create a dictionary with the given data
print(my_dict)

import numpy as np
import matplotlib.pyplot as plt
# Import the matplotlib library
Language=list(my_dict.keys())
Users_percentage=list(my_dict.values())
# Extract the keys and values from the dictionary
plt.bar(Language,Users_percentage,color='blue')
# Create the bar graph
plt.title('Programming language popularity')
# Add the title
plt.xlabel('Languages')
plt.ylabel('Users(percentage)')
# Add the labels

Choice=input("Enter a programming language from the list (JavaScript, HTML, Python, SQL, TypeScript): ")
# Ask the user to enter a programming language from the list
if Choice in Language:
    print("The percentage of users who use",Choice,"is",my_dict[Choice],"%")
# If the user's choice is in the list, print the percentage of users who use that language
else:
    print("The programming language is not in the list")
# If the user's choice is not in the list, tell the user that it is not in the list