
def normal_string(string):
    ret = ""
    length = len(string)

    for i in range(length):

        if string[i].isalpha():
            ret += string[i]
        elif ' ' == string[i] and i:
            if ' ' != string[i - 1]:
                ret += ' '
    ret2 = ret
    if ret and ' ' == ret[-1]:
        ret2 = ret[:-2]
    return ret2.lower()


def detailed_completion(completion):
    return f"{(completion[0]).completed_sentence} \
|| source: {(completion[0]).source_text} \
|| offset: {(completion[1])}\n"


