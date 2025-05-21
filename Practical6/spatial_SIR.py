import numpy as np 
import matplotlib.pyplot as plt
#make array of all susceplible population
population=np.zeros((100,100))

#randomly choose one person in this 100*100 array to be the first infected person
outbreak = np.random.choice(10000, 1)#chooses one number from 0 to 9999, which is the index of the 100*100 array
row = outbreak[0] // 100
col = outbreak[0] % 100
population[row, col] = 1#set this person's status to 1, which means infected

#set beta and gamma
beta=0.3
gamma=0.05

#then start the simulation
#status 0 means susceplible, 1 means infected, 2 means recovered
#status 1 means infected
#status 2 means recovered
#make the people around the infected person have a probability of beta to change form status 0 to 1
#make the infected person have a probability of gamma to change from status 1 to 2
times=101
for time in range(times):
 new_population=population.copy()
 for i in range(100):
     for j in range(100):
            if population[i, j] == 1:
                # choose the people around the infected person
                for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1), (i+1, j+1), (i+1, j-1), (i-1, j+1), (i-1, j-1)]:
                    if 0 <= x < 100 and 0 <= y < 100:
                        if population[x, y] == 0:
                            # roll a number and compare it with beta to figure out whether the person will be infected
                            if np.random.random() <= beta:
                                new_population[x, y] = 1
                if np.random.random() <= gamma:
                    new_population[i, j] = 2
     population = new_population
 #define when to save the plot
 save_time=[0,10,50,100]
 if time in save_time:
     plt.figure(figsize=(6, 4), dpi=150)
     plt.imshow(population, cmap='viridis', interpolation='nearest')
     plt.title(f"Time Step {time}")
     plt.show()
     

    
 
