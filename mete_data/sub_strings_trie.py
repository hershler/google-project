

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

    def insert_sub_string(self, sub_string):

        current_node = self.root
        length = len(sub_string)

        for level in range(length):
            index = self.char_to_index(sub_string[level])

            if not current_node.chars[index]:
                current_node.chars[index] = self.get_node()
            current_node = current_node.chars[index]

        current_node.complete_strings = init_best_complete_strings(sub_string)

    def find_best_complete_string(self, sub_string):

        current_node = self.root
        length = len(sub_string)

        for level in range(length):
            index = self.char_to_index(sub_string[level])

            if not current_node.chars[index]:
                return []
            current_node = current_node.chars[index]

        return current_node.complete_strings


