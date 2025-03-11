#Function: Triangle sequence
#T=number of of dots in a triangle
#if the nth triangle
#Tn=n*(n+1)/2
def numbers_of_dots(n):
    return n*(n+1)/2
#n range from 1 to 11
#print T1 to T10
for n in range(1,11):
    Tn = numbers_of_dots(n)
    print("T"+str(n)+"=",Tn)
