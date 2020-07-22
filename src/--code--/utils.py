def normal_string(string):
    ret = ""
    length = len(string)

    for i in range(length):
        if string[i].isalpha():
            ret += string[i]
        elif ' ' == string[i] and i:
            if ' ' != string[i - 1]:
                ret += ' '
    if ' ' == ret[-1]:
        ret = ret[:-2]
    return ret.lower()
