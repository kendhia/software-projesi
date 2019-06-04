
import admin
from pyfiglet import Figlet 
from QuestionHandler import QuestionHandler

fig = Figlet()

questionHandler = QuestionHandler()

print(fig.renderText("UNIV+"))

while True:
    name = input("Please enter your username:")
    if (name == admin.Admin.admin_name):
        password = input("Please enter admins password:")
        if (password == admin.Admin.admin_psw):
            print("\n \n \n Welcome Admin, if you want to add/modify questoins collection, please check Database Manager. \n \n \n")
            break
        print(fig.renderText("Checking..."))
    else:
        print(fig.renderText("Welcome %s"%name))
        break
    
    print("The password you provided is wrong.")

qst_input = input("What\'s your question : ")
while(qst_input != "q"):

    questionHandler.notifyQueRec(qst_input)
    result = questionHandler.get_result()

    print("*********************************")
    print(result)
    print("*********************************")

    qst_input = input("What\'s your question : ")
        
 