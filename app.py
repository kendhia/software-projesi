import data_verifier as DataVerifier
import data_resources as DataResources
import admin
from pyfiglet import Figlet 

def run():
    fig = Figlet()

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
            print("\n \n \n Welcome %s. \n \n \n" %name)
            break
        
        print("The password you provided is wrong.")

    qst_input = input("What\'s your question : ")
    
    while(qst_input != "q"):

        questio_ver_res = DataVerifier.check_question(qst_input)
        if not questio_ver_res:
            result = "Not a recognized question."
        else:
            result = DataResources.find_in_db(questio_ver_res[0], questio_ver_res[1], questio_ver_res[2])

        print("*********************************")
        print(result)
        print("*********************************")

        qst_input = input("What\'s your question : ")
            
 

run()