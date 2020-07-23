import glob
from auto_complete_data import AutoCompleteData


sentences_dict = {}


def init_sentences_dict():
    # read sentences from files

    for filename in glob.iglob("../--data--technology_texts/python-3.8.4-docs-text/" + 'bugs.txt', recursive=True):

        with open(filename, mode='r', encoding='utf-8') as f:
            sentences = f.readlines()
            sentences = [x.strip() for x in sentences]
            for i in range(len(sentences)):
                sentences_dict[i] = AutoCompleteData(sentences[i], filename.rpartition("/")[-1].rpartition(".")[0])

