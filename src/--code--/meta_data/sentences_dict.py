import glob
import os
from auto_complete_data import AutoCompleteData


sentences_dict = {}


def init_sentences_dict():

    # read sentences from files
    for (root, dirs, files) in os.walk("../--data--technology_texts", topdown=True):
        for file in files:
            with open(os.path.join(root, file), mode='r', encoding='utf-8') as f:
                sentences = f.readlines()
                sentences = [x.strip() for x in sentences]

                for i in range(len(sentences)):
                    sentences_dict[i] = AutoCompleteData(sentences[i], file)
