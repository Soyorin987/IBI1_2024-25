#Function: to find the largest intron in a given sequence
#Firstly determine the splice donor and splice acceptor sites, then go through the sequence, keep comparing the sequence with the splice donor and splice acceptor sites, and finally find the largest intron.
seq='ATGCAAGTGGTGTGTCTGTTCTGAGAGGGCCTAA'
splice_donor='GT'
splice_acceptor='AG'
#set the splice donor and splice acceptor
largest_intron_length=0
#initialize the largest intron length to 0
largest_intron=''

#start to search for the largest intron
for i in range(len(seq)):
    if seq[i:i+2]==splice_donor:
        for j in range(i+2, len(seq)):
            if seq[j:j+2]==splice_acceptor:
                d=seq[i:j+2]
                
        if len(d)>largest_intron_length:
            largest_intron_length=len(d)

# Print the largest intron and its length
print("Largest intron:", largest_intron)
print("Length of the largest intron:", largest_intron_length)