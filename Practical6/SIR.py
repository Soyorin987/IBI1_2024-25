#import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
#define the variables
Susceptible=9999
Infected=1
Recovered=0
N=Susceptible+Infected+Recovered
beta=0.3
gramma=0.05
#set the initial values
Susceptible_array=[Susceptible]
Infected_array=[Infected]
Recovered_array=[Recovered]
#set the initial arrays to track how the variables evolve over time

#define the probabilty of infection
#the probability of infection=beta*the number of infected people/N
#in each cycle people in the Susceptible group will be infected with the probability of infection
#Meanwhile, the infected person has a probability of gramma, 0.05 to recover
#the person who recovers from infection will then be put into the Recovered group
#track the number of people in each group after each cycle
#repeat this cycle for 1000 times

times=1000
for t in range(times):
    Probability_of_infection=beta*Infected/N
    new_infection=np.random.choice(range(2),Susceptible,p=[1-Probability_of_infection,Probability_of_infection]).sum()
    new_recover=np.random.choice(range(2),Infected,p=[1-gramma,gramma]).sum()

    new_infection = min(new_infection, Susceptible)  
    new_recover = min(new_recover, Infected)
    Susceptible -= new_infection
    Recovered += new_recover
    Infected=N-Susceptible-Recovered
    Susceptible_array.append(Susceptible)
    Infected_array.append(Infected)
    Recovered_array.append(Recovered)

plt.plot(Susceptible_array, label="Susceptible")
plt.plot(Infected_array, label="Infected")
plt.plot(Recovered_array, label="Recovered")
plt.xlabel("Time Steps")
plt.ylabel("Population")
plt.title("SIR Model Simulation")
plt.legend()
plt.show()