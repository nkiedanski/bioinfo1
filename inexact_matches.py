def inexact_matches(motive, sequence, mismatches_limit):
    occurrences = 0
    positions = []
    for index in range(0, len(sequence)-len(motive)+1):
        mismatches_count = 0
        for nucleotide in motive:
            if nucleotide == sequence[index]:
                index += 1
            else:
                mismatches_count += 1
                if mismatches_count > mismatches_limit:
                    break
        if mismatches_count <= mismatches_limit:
            occurrences += 1
            positions.append(index-len(motive))
    return occurrences, positions
