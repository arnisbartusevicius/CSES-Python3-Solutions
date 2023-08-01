dna_seq = input()
 
consec_letters = 1
max_consec_letters = 1
prev_letter = dna_seq[0]
 
for i in range(1, len(dna_seq)):
    if dna_seq[i] == prev_letter:
        consec_letters += 1
    else:
        consec_letters = 1
    if consec_letters > max_consec_letters:
        max_consec_letters = consec_letters
    prev_letter = dna_seq[i]        
 
print(max_consec_letters)