from QuestionVerifier import QuestionVerifier 
from AnswerCollection import AnswerCollection

class QuestionHandler(object): 
    result = None
    answerCollection = None
    answer_ready = False

    def __init__(self):
        self.answerCollection = AnswerCollection()


    def notifyQueRec(self, questionText):
        questionVerifier = QuestionVerifier(questionText)

        if (questionVerifier.getIsAccepted()):

            param, qst_type, extra_condition = questionVerifier.getQuestionType()
            self.result = self.answerCollection.getAnswerOf(param, qst_type, extra_condition)
        else:
            self.result = "Question not accepted. Please try another question."

    def get_result(self):
        return self.result