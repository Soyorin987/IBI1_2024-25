import re

# set the input and output file paths
input_file_path = r'C:\cygwin64\home\Stat9\IBI1_2024-2025\IBI1_2024-25\Practical7\Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'
output_file_path = r'C:\cygwin64\home\Stat9\IBI1_2024-2025\IBI1_2024-25\Practical7\tata_genes.fa'

# set the maximum line length for output, in case the line is too long
MAX_LINE_LENGTH = 30

# define the TATA box pattern
TATA_BOX_PATTERN = "TATA[AT]A[AT]"

with open(input_file_path, 'r') as infile, open(output_file_path, 'w') as outfile:
    current_header = None
    current_sequence = []

    for line in infile:
        line = line.strip()
        if line.startswith(">"):  # find the start of a new gene
            if current_header and current_sequence:  # if there is a previous gene, process it
                full_sequence = ''.join(current_sequence)  # combine sequence lines
                if re.search(TATA_BOX_PATTERN, full_sequence):  # check for TATA box
                    outfile.write(f"{current_header}\n")
                    for i in range(0, len(full_sequence), MAX_LINE_LENGTH):
                        outfile.write(f"{full_sequence[i:i+MAX_LINE_LENGTH]}\n")
            # update the current header and reset sequence
            current_header = line.split(" ")[0]  # take the header line and remove extra info
            current_sequence = []
        else:
            current_sequence.append(line)  # collect sequence lines
    # process the last gene
    if current_header and current_sequence:
        full_sequence = ''.join(current_sequence)
        if re.search(TATA_BOX_PATTERN, full_sequence):  
              outfile.write(f"{current_header}\n")
        for i in range(0, len(full_sequence), MAX_LINE_LENGTH):
                outfile.write(f"{full_sequence[i:i+MAX_LINE_LENGTH]}\n")

print(f"Genes containing TATA box saved to '{output_file_path}'.")