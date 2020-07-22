from meta_data.sentences_dict import sentences_dict


def find_best_complete_strings_offline(sub_string):
    completions = []
    for key, sentence in sentences_dict.items():
        if sub_string in sentence:
            completions.append(key)

    return completions
