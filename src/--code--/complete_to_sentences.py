from .meta_data.sub_strings_trie import init_substring_trie
from .meta_data.sentences_dict import init_sentences_dict


def init_system():
    init_substring_trie()
    init_sentences_dict()


def find_best_k_completions(sub_string):
    pass
