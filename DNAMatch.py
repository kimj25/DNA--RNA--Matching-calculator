# Julie Kim
# Project: Compares two DNA sequences (comprises nucleotides ACTG) and finds the longest sequence match
# using dynamic programming (bottom-up approach)
# and returns the length of the matching sequence
# calculates the percentage of match
# returns the matching sequence, if asked

def get_dna_sequences():
    valid_nucleotides = {"A", "T", "C", "G"}
    sequences = []

    for i in range(2):
        while True:
            seq = input(f"Enter DNA sequence {i + 1} (or press Enter to skip): ").strip().upper()
            if not seq:
                return sequences  # Stop early if user skips

            if all(nucleotide in valid_nucleotides for nucleotide in seq):
                sequences.append(seq)
                break
            else:
                print("Error: Invalid DNA sequence. Please enter a sequence containing only A, T, C, and G.")

    return print("Received DNA sequences:", sequences)


def get_rna_sequences(dna_seq):
    """Convert a DNA sequence to an RNA sequence (replace T with U)."""
    return print(f' RNA sequence of {dna_seq} is {dna_seq.replace("T", "U")}')

def dna_match_sequence(DNA1, DNA2):
    """ returns the length of longest subsequence match between DNA1 and DNA2"""

    m = len(DNA1)
    n = len(DNA2)

    # Create DNA_table (m+1 rows, n+1 columns)
    dna_table = [[0] * (n+1) for i in range(m+1)]

    # base case (if i is 0 or j is 0)
    for i in range(m+1):
        dna_table[i][0] = 0

    for j in range(n+1):
        dna_table[0][j] = 0

    for i in range(1, m+1):
        for j in range(1, n+1):
            # if current characters match
            if DNA1[i-1] == DNA2[j-1]:
                dna_table[i][j] = 1+ dna_table[i-1][j-1]
            # if not matching
            else:
                dna_table[i][j] = max(dna_table[i][j-1], dna_table[i-1][j])

    # Backtrack to find the sequence
    sequence = ""
    i, j = m, n

    while i > 0 and j > 0:
        if DNA1[i - 1] == DNA2[j - 1]:
            sequence = DNA1[i - 1] + sequence
            i -= 1
            j -= 1
        elif dna_table[i - 1][j] > dna_table[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return print(f'length of matching subsequence is {dna_table[m][n]} and the matching subsequence is {sequence}')


def user_interact():

    answer = input("Hello, do you have DNA sequences? Y/N ?")
    if answer == 'Y':
        num_seq = input("one or two sequences?")
        if num_seq ==1 or 'one':
            num_seq = 1
        if num_seq ==2 or 'two':
            num_seq = 2
        else:
            print("choose one or two")
            user_interact()
    else:
        return print("Good Bye")

    if num_seq == 1:
        answer1 = input("do you want to know the rna sequence? Y/N ? ")
        if answer1 == 'Y' or 'y':
            sequence1 = get_dna_sequences()
            get_rna_sequences(sequence1)
        elif answer1 == 'N' or 'n':
            print("Okay, there is nothing else I can do for you. Good bye")
        else:
            print("the response is invalid, try again")
            return

    if num_seq == 2:
        answer1 = input("do you want to know the rna sequence? Y/N ? ")
        answer2 = input("do you want to know the matching longest subsequence between the two? Y/N ? ")
        if answer1 == 'Y' and answer2 =='Y':
            sequence1, sequence2 = get_dna_sequences()
            get_rna_sequences(sequence1)
            get_rna_sequences(sequence2)
            dna_match_sequence(sequence1, sequence2)

        elif answer1 == 'Y' and answer2 =='N':
            sequence1, sequence2 = get_dna_sequences()
            get_rna_sequences(sequence1, sequence2)
            dna_match_sequence(sequence1, sequence2)

        elif answer1 == 'N' and answer2 =='Y':
            sequence1, sequence2 = get_dna_sequences()
            dna_match_sequence(sequence1, sequence2)
        else:
            print("the response is invalid, try again")
            return


user_interact()
