#Function: BMI Calculator:Show people's BMI and whether they are overweight, underweight or normal weight
#BMI=weight(kg)/height(m)^2
#Input weight and height
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))
#calculate BMI
bmi = weight / (height ** 2)
#If BMI<18.5, State=underweight
#If 18.5<=BMI<25, State=normal weight
#If BMI>=25, State=overweight
if bmi < 18.5:
    state = "underweight"
elif 18.5 <= bmi < 25:
    state = "normal weight"
else:
    state = "obese"
#Print BMI and State
print("Your BMI is " + str(bmi) + " and you are " + state + ".")