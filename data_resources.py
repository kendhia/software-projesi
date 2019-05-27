import pyodbc

connection = None

def find_in_db(param, qst_type, extra_condition):
    ''' 1 -> where, 2 -> when, 3 -> who 4 -> how many students 5 -> with whom 6 -> how long '''
    global connection
    
    if connection == None:
        connection = pyodbc.connect("DSN=questioning", autocommit=True)
    
    try:

        if qst_type == 1:
            
            fac_id = f"select FacultyID as id from faculty where FacultyFname = {param}"
            fac_id = connection.execute(fac_id).fetchone().id

            query = f"select UniversityID as uni_id from study where FacultyID = {fac_id}"
            uni_id = connection.execute(query).fetchone().uni_id

            query = f"select UniversityName from university where UniversityID = {uni_id}"
            
            result = connection.execute(query).fetchone().UniversityName.strip()

        elif qst_type == 2:
            fac_id = f"select FacultyID as id from faculty where FacultyFname = {param}"
            fac_id = connection.execute(fac_id).fetchone().id

            query = f"select GraduationDate as date from study where FacultyID = {fac_id}"
            result = connection.execute(query).fetchone().date

        elif qst_type == 3:
            result = []
            uni_id = f"select UniversityID as id from university where UniversityName = {param}"
            uni_id = connection.execute(uni_id).fetchone().id

            if (len(extra_condition) > 0):
                extra_condition[1] = extra_condition[1].replace("*", "'")
                query = f"select FacultyID from study where UniversityID = {uni_id} and GraduationDate {extra_condition[0]} {extra_condition[1]}"
                persons_list = connection.execute(query).fetchall()
            else:
                query = f"select FacultyID from study where UniversityID = {uni_id}"
                persons_list = connection.execute(query).fetchall()
            for person in persons_list:
                query = f"select FacultyFname, FacultyLname from faculty where FacultyID = {person.FacultyID}"
                full_name = connection.execute(query).fetchone()
                result.append(f"{full_name.FacultyFname.strip()} {full_name.FacultyLname.strip()}")

        elif qst_type == 4:
            uni_id = f"select UniversityID from university where UniversityName = {param}"
            uni_id = connection.execute(uni_id).fetchone().UniversityID

            query = f"SELECT COUNT(*) as count from study where UniversityID = {uni_id}"
            result = connection.execute(query).fetchone().count
        elif qst_type == 5:
            result = []
            fac_id = f"select FacultyID  as id from faculty where FacultyFname ='{param}'"
            fac_id = connection.execute(fac_id).fetchone().id

            query = f"select UniversityID as uni_id from study where FacultyID = {fac_id}"
            uni_id = connection.execute(query).fetchone().uni_id

            query = f"select FacultyID from study where UniversityID = {uni_id}"
            fac_list = connection.execute(query).fetchall()
            for fac in fac_list :
                fac_name = f"select FacultyFname,  FacultyLname  from faculty where FacultyID = {fac.FacultyID}"
                full_name = connection.execute(fac_name).fetchone()
                result.append(f"{full_name.FacultyFname.strip()} {full_name.FacultyLname.strip()}")

        elif qst_type == 6:
            fac_id = f"select FacultyID as id from faculty where FacultyFname = {param}"
            fac_id = connection.execute(fac_id).fetchone().id

            query = f"select * from study where FacultyID = {fac_id}"
            result = connection.execute(query).fetchone()
            result = result.enddate - result.startdate

        else:
            result = ""
    except Exception as e:
        result = "There was a problem in finding your query in our DB. Please check your values again."
        

    return result