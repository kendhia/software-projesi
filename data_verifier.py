import re

def check_question(qst_list):
    
    question_type = "test"
    if ((re.search("^(who|where|when|how many|how long)", qst_list))):
        question_type = (re.search("^(who|where|when|how many|how long)", qst_list)).group(0)
    school_ = (re.search(r'(university|school)', qst_list))
    get_school = (re.search("^(get school|find school)", qst_list))

    if (question_type == "where" or get_school):
        # where question
        person_name = (re.search(r"'(.*?)'", qst_list)).group(0)
        return person_name, 1, 0

    elif (question_type == "when"):
        # when question
        person_name = (re.search(r"'(.*?)'", qst_list)).group(0)
        return person_name, 2, 0

    elif (question_type == "who" and school_):
        person_name = (re.findall(r"'(.*?)'", qst_list[qst_list.find("in"):]))[0]
        return person_name, 5, 0

    elif (question_type == "who"):
        # who question
        univ_name = (re.search(r"'(.*?)'", qst_list)).group(0)
        before_after = (re.search("(before|after)", qst_list))
        extra_condition = []

        if (before_after and before_after.group(0) == 'before'):
            extra_condition.append("<=")
        elif(before_after and before_after.group(0) == 'after'):
            extra_condition.append(">=")

        if (before_after):
            date = (re.search(r"\*(.*?)\*", qst_list)).group(0)

            if (date):
                extra_condition.append(date)
            else:
                raise AttributeError
            
        return univ_name, 3, extra_condition


    elif (question_type == "how many"):
        univ_name = (re.search(r"'(.*?)'", qst_list)).group(0)
        return univ_name, 4, 0

    elif (question_type == "how long"):
        person_name = (re.search(r"'(.*?)'", qst_list)).group(0)
        return person_name, 6, 0

    else :
        # not defined yet
        return None