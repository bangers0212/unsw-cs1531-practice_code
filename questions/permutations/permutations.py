

def permutations(string):
    l = permutation_helper(string)
    # empty set
    if len(l) == 0:
        return {}
    return {i for i in l}


def permutation_helper(string):
    l = []
    if len(string) == 0:
        return []
    elif len(string) == 1:
        return [string]
    else:
        for i in range(len(string)):
            char = string[i]
            other_chars = string[:i] + string[i+1:]
            for p in permutation_helper(other_chars):
                l.append(char + p)
    return l


if __name__ == "__main__":
    print(permutations('aab'))
