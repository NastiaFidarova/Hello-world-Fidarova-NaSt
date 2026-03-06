files = ["seq1", "seq2", "seq3", "seq4"]
date = "06.26.2026" 
for name in files:
       new_name = name + ".fasta_" + date
       print(f"{new_name}")