import re

# set the input and output file paths
infile= r'C:\cygwin64\home\Stat9\IBI1_2024-2025\IBI1_2024-25\Practical7\Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'
outfile= r'C:\cygwin64\home\Stat9\IBI1_2024-2025\IBI1_2024-25\Practical7\tata_genes.fa'

# define the TATA box pattern
TATA_BOX_PATTERN = "TATA[AT]A[AT]"

with open(infile, "r") as fin, open(outfile, "w") as fout:
    current_header = None
    current_sequence = []
    for line in fin:
        line = line.strip()
        if line.startswith(">"):  #find the header line
            if current_header and current_sequence:
                full_sequence = ''.join(current_sequence) #join the sequence lines
                if re.search(TATA_BOX_PATTERN, full_sequence): #check if the TATA box is in the sequence
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
        if re.search(TATA_BOX_PATTERN, full_sequence):
            fout.write(f"{current_header}\n")
            fout.write(f"{full_sequence}\n")

print(f"Genes containing TATA box saved to '{outfile}'.")#output the result