from meta_data.sentences_dict import sentences_dict, init_sentences_dict
from meta_data.sub_strings_trie import sub_strings_trie, init_substring_trie


def init_system():
    init_sentences_dict()
    init_substring_trie()


def find_best_k_completions(sub_string):
    id_offset_completions = sub_strings_trie.search_best_complete_string(sub_string)
    id_offset_completions = id_offset_completions[:min(5, len(id_offset_completions))]
    sentences_and_offsets = []

    for completion in id_offset_completions:
        sentences_and_offsets.append((sentences_dict[completion[0]], completion[1]))

    return sentences_and_offsets
