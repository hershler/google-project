from meta_data.sentences_dict import sentences_dict, init_sentences_dict
from meta_data.sub_strings_trie import sub_strings_trie, init_substring_trie


def init_system():
    init_sentences_dict()
    init_substring_trie()


def find_best_k_completions(sub_string):
    sources_list = sub_strings_trie.search_best_complete_string(sub_string)
    best_completions = []
    for source in sources_list:
        best_completions.append(sentences_dict[source])

    return best_completions
