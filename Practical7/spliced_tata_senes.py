import re

# Ask the user for the splice donor/acceptor combination
splice_combination = input("Enter the splice donor/acceptor combination (GTAG, GCAG, ATAC): ").strip().upper()
if splice_combination not in {"GTAG", "GCAG", "ATAC"}:
    print("Invalid input. Please enter one of the following: GTAG, GCAG, ATAC.")
    exit()

# Define input and output file paths
input_file_path = r'C:\cygwin64\home\Stat9\IBI1_2024-2025\IBI1_2024-25\Practical7\Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'
output_file_path = f'C:\cygwin64\home\Stat9\IBI1_2024-2025\IBI1_2024-25\Practical7\{splice_combination}_spliced_genes.fa'

# Define the TATA box pattern
TATA_BOX_PATTERN = "TATA[AT]A[AT]"

# Process the input file and write the output
with open(input_file_path, 'r') as infile, open(output_file_path, 'w') as outfile:
    current_header = None
    current_sequence = []

    for line in infile:
        line = line.strip()
        if line.startswith(">"):  # Header line
            if current_header and current_sequence:
                # Process the previous gene
                full_sequence = ''.join(current_sequence)
                tata_count = len(re.findall(TATA_BOX_PATTERN, full_sequence))
                if tata_count > 0:
                    gene_name = current_header.split(" ")[0][1:]  # Extract gene name
                    outfile.write(f">{gene_name} | TATA instances: {tata_count}\n{full_sequence}\n")
            # Update the current header
            current_header = line
            current_sequence = []
        else:
            current_sequence.append(line)  # Collect sequence lines

    # Process the last gene
    if current_header and current_sequence:
        full_sequence = ''.join(current_sequence)
        tata_count = len(re.findall(TATA_BOX_PATTERN, full_sequence))
        if tata_count > 0:
            gene_name = current_header.split(" ")[0][1:]  # Extract gene name
            outfile.write(f">{gene_name} | TATA instances: {tata_count}\n{full_sequence}\n")

print(f"Spliced genes with TATA box saved to '{output_file_path}'.")