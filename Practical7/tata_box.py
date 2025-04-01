input_file_path = r'C:\cygwin64\home\Stat9\IBI1_2024-2025\IBI1_2024-25\Practical7\Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'
output_file_path = r'C:\cygwin64\home\Stat9\IBI1_2024-2025\IBI1_2024-25\Practical7\tata_genes.fa'
MAX_LINE_LENGTH = 30
#set the maximum line length to 30
with open(input_file_path, 'r') as infile, open(output_file_path, 'w') as outfile:
    current_header = None
    current_sequence = []

    for line in infile:
        line = line.strip()
        if line.startswith(">"):  # detect header line
            if current_header:  # if not the first gene
                outfile.write(f"{current_header}\n")
                for i in range(0, len(''.join(current_sequence)), MAX_LINE_LENGTH):
                    outfile.write(f"{''.join(current_sequence)[i:i+MAX_LINE_LENGTH]}\n")
            # select the header, remove the first space and everything after the first space
            # in this case we get the gene name
            current_header = line.split(" ")[0]
            current_sequence = []
        else:
            current_sequence.append(line)  # collect sequence lines

    # write the last gene if it exists
    if current_header:

        outfile.write(f"{current_header}\n{''.join(current_sequence)}\n")
        for i in range(0, len(''.join(current_sequence)), MAX_LINE_LENGTH):
            outfile.write(f"{''.join(current_sequence)[i:i+MAX_LINE_LENGTH]}\n")
print(f"Formatted genes saved to '{output_file_path}'.")