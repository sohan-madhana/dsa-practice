def isValidSubsequence(array, sequence):
    seq_index = 0
    for value in array:
        if seq_index == len(sequence):
            break
        if sequence[seq_index] == value:
            seq_index += 1
    return seq_index == len(sequence)