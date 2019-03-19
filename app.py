import json
import pyodbc
import question, answer, admin, user
import re

class app:
    connection = pyodbc.connect("driver", autocommit=True)

    def run(self):
        
        qst_input = input("What\'s your question : ")
        
        while(qst_input == "q"):

            qst_list = qst_input.split(" ")
            question_type = (re.search("^(who|where|when)", qst_list)).group(0)
             
            if (question_type == "where"):
                # where question
                person_name = (re.search(r'"(.*?)"', qst_list)).group(0)
                result = self.find_in_db(person_name, 1)

            elif (question_type == "when"):
                # when question
                person_name = (re.search(r'"(.*?)"', qst_list)).group(0)
                result = self.find_in_db(person_name, 2)

            elif (question_type == "who"):
                # who question
                univ_name = (re.search(r'"(.*?)"', qst_list)).group(0)
                result = self.find_in_db(univ_name, 3)
            else :
                # not defined yet
                result = print("Not a recognized question.")
            print("*********************************")
            print(result)
            print("*********************************")

            qst_input = input("What\'s your question : ")
                
    
    def find_in_db(self, param, qst_type):
        ''' 1 -> where, 2 -> when, 3 -> who'''
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

            query = f"select fac_id from study where uni_id = {uni_id}"
            result = self.connection.execute(query).fetchall()

        else:
            result = ""

        return result

