from .sentences_dict import sentences_dict
from find_completions_offline import find_best_complete_strings_offline


class TrieNode:

    def __init__(self):
        self.chars = [None for i in range(26 + 1)]
        self.complete_strings = []


class Trie:

    def __init__(self):
        self.root = self.get_node()

    def get_node(self):
        return TrieNode()

    def char_to_index(self, ch):
        return 26 if ' ' == ch else ord(ch) - ord('a')

    def insert_sub_string(self, sub_string, string_key):

        current_node = self.root
        length = len(sub_string)

        for level in range(length):
            index = self.char_to_index(sub_string[level])

            if not current_node.chars[index]:
                current_node.chars[index] = self.get_node()
            current_node = current_node.chars[index]

        if len(current_node.complete_strings) < 5 and string_key not in current_node.complete_strings:
            current_node.complete_strings.append(string_key)

    def search_best_complete_string(self, sub_string):

        current_node = self.root
        length = len(sub_string)

        for level in range(length):
            index = self.char_to_index(sub_string[level])

            if not current_node.chars[index]:
                return []
            current_node = current_node.chars[index]

        return current_node.complete_strings


sub_string_trie = Trie()


def find_substrings_of_string(string):

    length = len(string)
    for i in range(length):
        for j in range(i + 1, length + 1):
            yield string[i: j]


def init_substring_trie():

    for key, sentence in sentences_dict.items():
        for sub_string in find_substrings_of_string(sentence):
            sub_string_trie.insert_sub_string(sub_string, key)
