import glob


# has to be an object, while changing remember go to sub_string_trie.init - values
sentences_dict = {}


def init_sentences_dict():
    # read sentences from files

    for filename in glob.iglob("../--data--technology_texts/python-3.8.4-docs-text/" + '/**.txt', recursive=True):

        with open(filename, mode='r', encoding='utf-8') as f:
            sentences = f.readlines()
            sentences = [x.strip() for x in sentences]
            for i in range(len(sentences)):
                sentences_dict[i] = sentences[i]

