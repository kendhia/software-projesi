

class Question:

    question_str = ""
    question_type = ""

    def add_text(self, qstn_str):
        self.questoin_str = qstn_str

    def qst_txt(self):
        return self.questoin_str

    def set_qst_type(self, type):
        self.question_type = type
    
