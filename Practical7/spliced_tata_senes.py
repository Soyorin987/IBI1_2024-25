#Fuction:to find the genes containing the splice donor/acceptor combination and TATA box and put them into a new file
import re
splice_combination = input("Enter the splice donor/acceptor combination (GTAG, GCAG, ATAC): ")#ask the user to input the splice donor/acceptor combination
if splice_combination not in {"GTAG", "GCAG", "ATAC"}:
    print("Invalid input. Please enter one of: GTAG, GCAG, ATAC.") #check if the input is valid, if not, then output the error message
    exit()

infile= r'C:\cygwin64\home\Stat9\IBI1_2024-2025\IBI1_2024-25\Practical7\Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'
outfile = f'{splice_combination}_spliced_genes.fa'# the output file name will be the splice donor/acceptor combination + "_spliced_genes.fa"

# define the TATA box pattern
TATA_BOX_PATTERN = "TATA[AT]A[AT]"
donor=splice_combination[0:2] #get the first two letters of the splice donor/acceptor combination
acceptor=splice_combination[2:4] #get the last two letters of the splice donor/acceptor combination

with open(infile, "r") as fin, open(outfile, "w") as fout:
    current_header = None
    current_sequence = [] #set the variable to store the sequence
    for line in fin:
        line = line.strip()
        if line.startswith(">"):  #find the header line
            if current_header and current_sequence:
                full_sequence = ''.join(current_sequence) #join the sequence lines
                if re.search(TATA_BOX_PATTERN, full_sequence) and re.search(rf'{donor}.+{acceptor}',full_sequence): #check if the TATA box and donor, acceptor combination are in the sequence
                    fout.write(f"{current_header}\n")
                    fout.write(f"{full_sequence}\n")
            # update the current header
            gene_id = line.split(" ")[0][1:]  # delete the > sign'>'
            gene_name = gene_id.split("_")[0]  # delete the _ and the 'mRNA' after it
            current_header = f">{gene_name}" #only keep the first part of the header(the name)
            current_sequence = []
        else:
            current_sequence.append(line)

    # deal with the last sequence
    if current_header and current_sequence:
        full_sequence = ''.join(current_sequence)
        if re.search(TATA_BOX_PATTERN, full_sequence) and splice_combination in full_sequence:
            fout.write(f"{current_header}\n")
            fout.write(f"{full_sequence}\n")


with open(outfile, "r") as f:
    lines = f.readlines()
if lines:
    lines[-1] = lines[-1].rstrip("\n")  #remove the last newline character
with open(outfile, "w") as f:#open the file in write mode
    f.writelines(lines)#write the lines back to the file

print(f"Genes containing TATA box and {splice_combination} combination saved to '{outfile}'.")#output the result