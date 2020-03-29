def permutate(seq):
    """permutate a sequence and return a list of the permutations"""
    if not seq:
        return [seq] # is an empty sequence
    else:
        temp_perm = []
        for i in range(len(seq)):
            part = seq[:i] + seq[i+1:]
            for p in permutate(part):
                temp_perm.append(seq[i:i+1] + p)
        return temp_perm

print(permutate([0,5,6,9]))