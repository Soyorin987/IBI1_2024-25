#import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

beta=0.3
gramma=0.05
#form the vaccination rates
vaccination_rates= np.arange(0.1,1.1,0.1)
#vaccination rates will range from 0.1 to 1.0 with a step of 0.1
results={}
for vaccination_rate in vaccination_rates:
    #set the basic variables
    Susceptible=9999
    Infected=1
    Recovered=0
    N=Susceptible+Infected+Recovered
    #apply vaccination
    vaccinated=int(Susceptible*vaccination_rate)
    Susceptible-=vaccinated
    Recovered+=vaccinated
    Susceptible_array=[Susceptible]
    Infected_array=[Infected]
    Recovered_array=[Recovered] 
    #for every vaccination rates, run the simulation for 1000 times
    times=1000
    for t in range(times):
     Probability_of_infection=beta*Infected/N
     new_infection=np.random.choice(range(2),Susceptible,p=[1-Probability_of_infection,Probability_of_infection]).sum()
     new_recover=np.random.choice(range(2),Infected,p=[1-gramma,gramma]).sum()

     new_infection = min(new_infection, Susceptible)  
     new_recover = min(new_recover, Infected)
     Susceptible -= new_infection
     Recovered += new_recover
     Infected+= new_infection-new_recover
     Susceptible_array.append(Susceptible)
     Infected_array.append(Infected)
     Recovered_array.append(Recovered)
     results[vaccination_rate] = {
     "Susceptible": Susceptible_array,
     "Infected": Infected_array,
     "Recovered": Recovered_array
}
#take down the results of each vaccination rate
plt.figure(figsize=(10, 6))
#plot the results for different vaccination rates
for vaccination_rate, data in results.items():
    plt.plot(data["Infected"], label=f"Vaccination Rate: {int(vaccination_rate * 100)}%")

plt.xlabel("Time Steps")
plt.ylabel("Infected Population")
plt.title("Effect of Vaccination on Infection Spread")
plt.legend()
plt.show()