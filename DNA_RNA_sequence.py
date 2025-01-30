# Julie Kim
# Project: Asks for DNA from the user (either one or two)
# if user wants, returns the RNA that transcribes from the input DNA
# Also if user wants, compares two input DNA sequences and finds the longest sequence match
# using dynamic programming (bottom-up approach)
# and returns the length of the matching sequence


def get_dna_sequences(num_sequences):
    """Prompt user for DNA sequences based on required number."""
    valid_nucleotides = {"A", "T", "C", "G"}
    sequences = []

    for i in range(num_sequences):
        while True:
            seq = input(f"Enter DNA sequence {i + 1}: ").strip().upper()
            if all(nucleotide in valid_nucleotides for nucleotide in seq):
                sequences.append(seq)
                break
            else:
                print("Error: Invalid DNA sequence. Please enter a sequence containing only A, T, C, and G.")

    print("Received DNA sequences:", sequences)
    return sequences


def get_rna_sequences(dna_seq):
    """Convert a DNA sequence to an RNA sequence (replace T with U)."""
    rna_seq = dna_seq.replace("T", "U")
    print(f'RNA sequence of {dna_seq} is {rna_seq}')
    return rna_seq


def dna_match_sequence(DNA1, DNA2):
    """Returns the length of longest subsequence match between DNA1 and DNA2."""

    m, n = len(DNA1), len(DNA2)
    dna_table = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill table using bottom-up DP
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if DNA1[i - 1] == DNA2[j - 1]:
                dna_table[i][j] = 1 + dna_table[i - 1][j - 1]
            else:
                dna_table[i][j] = max(dna_table[i][j - 1], dna_table[i - 1][j])

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

    print(f'Length of matching subsequence: {dna_table[m][n]}')
    print(f'Matching subsequence: {sequence}')


def one_DNA():
    sequences = get_dna_sequences(1)
    sequence1 = sequences[0]

    answer1 = input("Do you want to know the RNA sequence? Y/N: ").strip().lower()
    if answer1 == 'y':
        get_rna_sequences(sequence1)
    elif answer1 == 'n':
        print("Okay, there is nothing else I can do for you. Goodbye!")
    else:
        print("Invalid response. Try again.")
        one_DNA()


def two_DNA():
    sequences = get_dna_sequences(2)
    if len(sequences) < 2:
        print("Error: Two valid DNA sequences were not provided.")
        return

    sequence1, sequence2 = sequences

    answer1 = input("Do you want to know the RNA sequence? Y/N: ").strip().lower()
    answer2 = input("Do you want to find the longest matching subsequence? Y/N: ").strip().lower()

    if answer1 == 'y':
        get_rna_sequences(sequence1)
        get_rna_sequences(sequence2)

    if answer2 == 'y':
        dna_match_sequence(sequence1, sequence2)

    if answer1 == 'n' and answer2 == 'n':
        print("Goodbye!")


def user_interact():
    """Main user interaction function."""
    answer = input("Hello, do you have DNA sequences? Y/N: ").strip().lower()
    if answer == 'y':
        num_seq = input("One or two sequences? ").strip().lower()
        if num_seq in {"1", "one"}:
            one_DNA()
        elif num_seq in {"2", "two"}:
            two_DNA()
        else:
            print("Invalid choice. Please enter 'one' or 'two'.")
            user_interact()
    elif answer == 'n':
        print("Goodbye!")
    else:
        print("Invalid answer. Try again.")
        user_interact()


# Run the program with the user input
user_interact()
