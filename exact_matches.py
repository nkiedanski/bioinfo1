def exact_matches(motive, sequence):
    occurrences = 0
    positions = []
    for index in range(0, len(sequence)-len(motive)+1):
        nucleotide_match = 0
        for nucleotide in motive:
            if nucleotide == sequence[index]:
                index += 1
                nucleotide_match +=1
            else:
                break
        if nucleotide_match == len(motive):
            occurrences += 1
            positions.append(index)
    return occurrences, positions
