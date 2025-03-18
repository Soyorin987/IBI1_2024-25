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
plt.show()