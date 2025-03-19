uk_countries=[57.11,3.13,1.91,5.45]
uk_name=['England','Wales','Northern Ireland','Scotland']
Zhejiang_neighbouring_provinces_in_China=[65.77,41.88,45.28,61.27,85.15]
Zhejiang_neighbouring_provinces_name=['Zhejiang','Fujian','Jiangxi','Anhui','Jiangsu']
# Make two lists using the given data
print("The population sizes of the UK countries in ascending order:",sorted(uk_countries))
print("The population sizes of the neighbouring provinces of Zhejiang in China in ascending order:",sorted(Zhejiang_neighbouring_provinces_in_China))
# Print the two lists

#Firslty, draw the pie chart of the distrbution of population sizes in UK countries
import matplotlib.pyplot as plt
# Import the matplotlib library
plt.title('Population sizes of the UK countries',fontweight='bold')
# Set the title
lables='England','Wales','Northern Ireland','Scotland'
# Set the lables
sizes=[57.11,3.13,1.91,5.45]
# Set the sizes
explode=(0,0,0,0)
plt.pie(sizes,explode=explode,labels=lables,autopct='%1.1f%%',shadow=False,startangle=0)
plt.axis('equal')
# Create the pie chart
plt.show()
# Show the pie chart

#Then, draw the pie chart of the distrbution of population sizes in Provinces neighbouring Zhejiang in China
plt.title('Population sizes of the neighbouring provinces of Zhejiang in China',fontweight='bold')
# Set the title
lables2='Zhejiang','Fujian','Jiangxi','Anhui','Jiangsu'
# Set the lables
sizes2=[65.77,41.88,45.28,61.27,85.15]
# Set the sizes
explode2=(0,0,0,0,0)
plt.pie(sizes2,explode=explode2,labels=lables2,autopct='%1.1f%%',shadow=False,startangle=100)
plt.axis('equal')
# Create the pie chart
plt.show()
# Show the pie chart