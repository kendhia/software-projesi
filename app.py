import json
import pyodbc
import question, answer, admin, user
import re

class app:
    connection = pyodbc.connect("driver", autocommit=True)

    def run(self):
        
        qst_input = input("What\'s your question : ")
        
        while(qst_input == "q"):

            qst_list = qst_input
            question_type = (re.search("^(who|where|when|how many|how long)", qst_list)).group(0)
            school_ = (re.search(r'(university|school)', qst_list)).group(0)
            get_school = (re.search("^(get school|find school)", qst_list)).group(0)

            if (question_type == "where" or get_school):
                # where question
                person_name = (re.search(r'"(.*?)"', qst_list)).group(0)
                result = self.find_in_db(person_name, 1, 0)

            elif (question_type == "when"):
                # when question
                person_name = (re.search(r'"(.*?)"', qst_list)).group(0)
                result = self.find_in_db(person_name, 2, 0)

            elif (question_type == "who" and school_):
                person_name = (re.findall(r'"(.*?)"', qst_list[qst_list.find("in"):]))[0]
                result = self.find_in_db(person_name, 5, 0)

            elif (question_type == "who"):
                # who question
                univ_name = (re.search(r'"(.*?)"', qst_list)).group(0)
                before_after = (re.search(r'(before|after)"', qst_list)).group(0)
                extra_condition = []

                if (before_after and before_after == 'before'):
                    extra_condition[0] =  "<="
                elif(before_after and before_after == 'after'):
                    extra_condition[0] =  ">="

                if (before_after):
                    date = (re.search(r'(\d+)"', qst_list)).group(0)

                    if (date):
                        extra_condition[1] =  date
                    else:
                        raise AttributeError
                    

                result = self.find_in_db(univ_name, 3, extra_condition)

            elif (question_type == "how many"):
                univ_name = (re.search(r'"(.*?)"', qst_list)).group(0)
                result = self.find_in_db(univ_name, 4, 0)

            elif (question_type == "how long"):
                person_name = (re.search(r'"(.*?)"', qst_list)).group(0)
                result = self.find_in_db(person_name, 6, 0)

            else :
                # not defined yet
                result = print("Not a recognized question.")
            print("*********************************")
            print(result)
            print("*********************************")

            qst_input = input("What\'s your question : ")
                
    
    def find_in_db(self, param, qst_type, extra_condition):
        ''' 1 -> where, 2 -> when, 3 -> who 4 -> how many students 5 -> with whom 6 -> how long '''
        if qst_type == 1:
            
            fac_id = f"select id from faculty where name = {param}"
            fac_id = self.connection.execute(fac_id).fetchone().id

            query = f"select uni_id from study where fac_id = {fac_id}"
            uni_id = self.connection.execute(query).fetchone().uni_id

            query = f"select uni_name from university where uni_id = {uni_id}"
            
            result = self.connection.execute(query).fetchall()

        elif qst_type == 2:
            fac_id = f"select id from faculty where name = {param}"
            fac_id = self.connection.execute(fac_id).fetchone().id

            query = f"select date from study where fac_id = {fac_id}"
            result = self.connection.execute(query).fetchone().date

        elif qst_type == 3:
            
            uni_id = f"select id from university where name = {param}"
            uni_id = self.connection.execute(fac_id).fetchone().id

            if (len(extra_condition) > 0):
                query = f"select fac_id from study where uni_id = {uni_id} and enddate {extra_condition[0]} {extra_condition[1]}"

            else:
                query = f"select fac_id from study where uni_id = {uni_id}"
            result = self.connection.execute(query).fetchall()

        elif qst_type == 4:
            uni_id = f"select id from university where name = {param}"
            uni_id = self.connection.execute(fac_id).fetchone().id

            query = f"SELECT COUNT(*) from study where uniid = {uni_id}"
            result = self.connection.execute(query).fetchone()
        elif qst_type == 5:
            result = []
            fac_id = f"select id from faculty where name = {param}"
            fac_id = self.connection.execute(fac_id).fetchone().id

            query = f"select uni_id from study where fac_id = {fac_id}"
            uni_id = self.connection.execute(query).fetchone().uni_id

            query = f"select facid from study where uni_id = {uni_id}"
            fac_list = self.connection.execute(query).fetchall()
            for fac in fac_list :
                fac_name = f"select name from faculty where id = {fac.id}"
                result.append(self.connection.execute(fac_name).fetchone().name)

        elif qst_type == 6:
            fac_id = f"select id from faculty where name = {param}"
            fac_id = self.connection.execute(fac_id).fetchone().id

            query = f"select * from study where fac_id = {fac_id}"
            result = self.connection.execute(query).fetchone()
            result = result.enddate - result.startdate

        else:
            result = ""

        return ",".join(result)

