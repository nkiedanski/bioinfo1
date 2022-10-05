def exact_matches(motive, sequence):
    occurrences = 0
    positions = []
    for index_seq in range(0, len(sequence)-len(motive)+1):
        nucleotide_match = 0
        for index_mot in range(0, len(motive)):
            if motive[index_mot] == sequence[index_seq + index_mot]:
                nucleotide_match += 1
            else:
                break
        if nucleotide_match == len(motive):
            occurrences += 1
            positions.append(index_seq)
    return occurrences, positions




# def exact_matches(motive, sequence):
#     occurrences = 0
#     positions = []
#     for index in range(0, len(sequence)-len(motive)+1):
#         nucleotide_match = 0
#         for nucleotide in motive:
#             if nucleotide == sequence[index]:
#                 index += 1
#                 nucleotide_match += 1
#             else:
#                 break
#         if nucleotide_match == len(motive):
#             occurrences += 1
#             positions.append(index)
#     return occurrences, positions