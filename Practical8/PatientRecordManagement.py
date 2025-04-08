#Function:collect the individual's name, age, date of latest admission and medical history
#then print all the details in a single line
class Patient:
    def __init__(self, name, age, date_of_latest_admission, medical_history):
        self.name = name
        self.age = age
        self.date_of_latest_admission = date_of_latest_admission
        self.medical_history = medical_history

    def display(self):
        print("Name: " + self.name + ", Age: " + str(self.age) + ", Date of Latest Admission: " + self.date_of_latest_admission + ", Medical History: " + self.medical_history)
#an example of using the class    
patient1 = Patient("John Doe", 45, "2025-04-01", "Diagnosed with hypertension.")
patient1.display()