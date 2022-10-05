def inexact_matches(motive, sequence, mismatches_limit):
    occurrences = 0
    positions = []
    for index_seq in range(0, len(sequence)-len(motive)+1):
        mismatches_count = 0
        for index_mot in range(0, len(motive)):
            if motive[index_mot] != sequence[index_seq + index_mot]:
                mismatches_count += 1
                if mismatches_count > mismatches_limit:
                    break
        if mismatches_count <= mismatches_limit:
            occurrences += 1
            positions.append(index_seq)
    return occurrences, positions

