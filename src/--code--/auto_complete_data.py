
class AutoCompleteData:

    def __init__(self, sentence, src_txt):
        self.completed_sentence = sentence
        self.source_text = src_txt


class SubstringData:

    def __init__(self, comp_id, offset):
        self.comp_id = comp_id
        self.offset = offset