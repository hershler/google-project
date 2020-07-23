
class AutoCompleteData:

    def __init__(self, sentence, src_txt):
        self.completed_sentence = sentence
        self.source_text = src_txt
        self.offset = 0
        self.score = 0
