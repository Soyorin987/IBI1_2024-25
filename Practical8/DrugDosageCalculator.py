#Function: collect the individual's weight and the strength of paracetamol
# then return the volume of paracetamol required

#define the function to calculate the volume of paracetamol required
def calculate(volume):
    mg=weight*15
    volume=mg/strengthfloat
    return volume

# Example usage of the function with hardcoded values
weight = 25  
strengthfloat = 120 / 5
volume = calculate(0)
print("The volume of paracetamol required for a weight of 25 kg is (for 25kg and 120mg/5ml) " + str(volume) + "ml.")

#ask the user to put in their weight and the strength of paracetamol
weight = float(input("Enter your weight in kg: "))
strength = input("Enter your strength of paracetamol(120mg/5ml or 250mg/5ml): ")
if strength == "120mg/5ml":
   strengthfloat= 120/5
elif strength == "250mg/5ml":
    strengthfloat= 250/5
#then check whether the values are proper
else:
    print("Error: Please enter a valid strength (eg:120mg/5ml).")
    exit()

if weight<10 or weight>100:
    print("Error:Please enter a valid weight")
    exit()
#if the values are proper, then calculate the volume of paracetamol required
#call the function and print the result
volume = calculate(0)
print("The volume of paracetamol required is " + str(volume) + "ml.")

