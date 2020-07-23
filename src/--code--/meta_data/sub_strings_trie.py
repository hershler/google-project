from .sentences_dict import sentences_dict
from utils import normal_string


class TrieNode:

    def __init__(self, father):
        self.chars = [None for i in range(26 + 1)]
        self.complete_strings = []
        self.father = father


class Trie:

    def __init__(self):
        self.root = self.get_node(None)

    def get_node(self, father):
        return TrieNode(father)

    def char_to_index(self, ch):
        return 26 if ' ' == ch else ord(ch) - ord('a')

    def insert_sub_string(self, sub_string, string_key):

        current_node = self.root
        length = len(sub_string)

        for level in range(length):
            index = self.char_to_index(sub_string[level])

            if not current_node.chars[index]:
                current_node.chars[index] = self.get_node(current_node)
            current_node = current_node.chars[index]

        if len(current_node.complete_strings) < 5 and string_key not in current_node.complete_strings:
            current_node.complete_strings.append(string_key)

    def search_best_complete_string(self, sub_string):

        def search(node, string):
            if node is None:
                return [], None
            length = len(string)

            for level in range(length):
                index = self.char_to_index(string[level])

                if not node.chars[index]:
                    return [], node.father
                node = node.chars[index]

            return node.complete_strings, node.father

        # call to search
        res, father = search(self.root, sub_string)

        current_index = len(sub_string) - 1

        while current_index and father and 5 != len(res):
            for char in father.chars:
                current_res, father = search(char, sub_string[current_index:])
                res += current_res
            current_index -= 1


        return res


sub_string_trie = Trie()


def find_substrings_of_string(string):

    length = len(string)
    for i in range(length):
        for j in range(i + 1, length + 1):
            yield string[i: j]


def init_substring_trie():

    for key, sentence in sentences_dict.items():
        for sub_string in find_substrings_of_string(normal_string(sentence.completed_sentence)):
            sub_string_trie.insert_sub_string(sub_string, key)
