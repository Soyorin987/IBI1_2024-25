#Function:to make 3 comparisons between three sequences and output the alignment score and percentage of identical amino acids for each of the three comparisons

#input the three sequences
with open("c:/cygwin64/home/Stat9/IBI1_2024-2025/IBI1_2024-25/Practical13/P04179.fasta", "r") as file:
    lines = file.readlines()
    seq_human = "".join(line.strip() for line in lines[1:]) #join the lines to get the sequence and delete the first line because it is the name of the sequence

with open("c:/cygwin64/home/Stat9/IBI1_2024-2025/IBI1_2024-25/Practical13/P09671.fasta", "r") as file:
    lines = file.readlines()
    seq_rat = "".join(line.strip() for line in lines[1:]) 

with open("c:/cygwin64/home/Stat9/IBI1_2024-2025/IBI1_2024-25/Practical13/random_sequence.fasta", "r") as file:
    lines = file.readlines()
    seq_random = "".join(line.strip() for line in lines[1:])

#create the BLOSUM62 matrix
blosum62 = {}
#input the BLOSUM62 matrix from the file
with open("c:/cygwin64/home/Stat9/IBI1_2024-2025/IBI1_2024-25/Practical13/blosum62.fasta", "r") as file:
    lines = file.readlines() #read all the lines in the file
    headers = lines[0].split() #the first line is the names of the AAs, so we split it into parts
    for line in lines[1:]:#the first line is the names of the AAs, so we skip it and then go through the rest of the lines
        parts = line.split() #split the line into parts
        row_aa = parts[0] #the first word part is the row AA name
        blosum62[row_aa] = {} #initialize the dictionary for the row AA
        for i in range(1, len(parts)):
            col_aa = headers[i - 1] #find the column AA name
            score = int(parts[i]) #convert the score to an integer
            blosum62[row_aa][col_aa] = score #store the score in the dictionary

def compare(seq1, seq2, blosum62): #make a function to compare the two sequences
    score = 0
    identical = 0 #initialize the score and identical variables
    for a1, a2 in zip(seq1, seq2):
        score += blosum62[a1][a2]
        if a1 == a2:
            identical += 1
    identity = (identical / len(seq1)) * 100
    return score, identity

score_hm, id_hm = compare(seq_human, seq_rat, blosum62)
score_hr, id_hr = compare(seq_human, seq_random, blosum62)
score_rr, id_rr = compare(seq_rat, seq_random, blosum62)

print("Human vs Rat:    Score =", score_hm, " Identity =", f"{id_hm:.1f}%")
print("Human vs Random: Score =", score_hr, " Identity =", f"{id_hr:.1f}%")
print("Rat vs Random:   Score =", score_rr, " Identity =", f"{id_rr:.1f}%")