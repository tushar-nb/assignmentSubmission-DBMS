import mysql.connector

mydb = mysql.connector.connect(host ="localhost",user ="root",database="project_608")
# if mydb:
#     print("Success")
# else:
#     print("Falied")
     
c = mydb.cursor()
c.execute('CREATE DATABASE IF NOT EXISTS project_608;')

#############################################   CREATE TABLES  ##########################################################

def create_table_faculties():
    c.execute('CREATE TABLE IF NOT EXISTS faculties(facultyId varchar(256) NOT NULL,firstName varchar(50) NOT NULL,lastName   varchar(50) NOT NULL,email varchar(320) NOT NULL,DOB datetime DEFAULT NULL,age int DEFAULT NULL,address varchar(512) DEFAULT NULL,institution varchar(512) DEFAULT NULL,contact varchar(15) DEFAULT NULL,password varchar(50) DEFAULT NULL,PRIMARY KEY (facultyId),UNIQUE KEY facultyId (facultyId),UNIQUE KEY email (email))')
    
def create_table_classes():
    c.execute('CREATE TABLE IF NOT EXISTS classes(classCode varchar(40) NOT NULL,course varchar(512) NOT NULL,subject varchar(512) NOT NULL,className varchar(512) NOT NULL,cr varchar(20) DEFAULT NULL,facultyId varchar(256) DEFAULT NULL,PRIMARY KEY (classCode),UNIQUE KEY classCode (classCode),FOREIGN KEY (facultyId) REFERENCES faculties (facultyId))')
    
def create_table_assignments():
    c.execute('CREATE TABLE IF NOT EXISTS assignments(assignmentId varchar(256) NOT NULL,assignmentNumber int NOT NULL,title varchar(512) NOT NULL,description varchar(2048) DEFAULT NULL,type varchar(10), resources varchar(2048) DEFAULT NULL,deadline datetime NOT NULL,classCode varchar(40) DEFAULT NULL,facultyId varchar(256) DEFAULT NULL,PRIMARY KEY (assignmentId),UNIQUE KEY assignmentId (assignmentId),FOREIGN KEY (classCode) REFERENCES classes (classCode),FOREIGN KEY (facultyId) REFERENCES faculties (facultyId))')
    
def create_table_students():
    c.execute('CREATE TABLE IF NOT EXISTS students(srn varchar(20) NOT NULL,name varchar(40) NOT NULL,cr varchar(20) DEFAULT NULL,isCr tinyint(1) DEFAULT 0,classCode varchar(40) NOT NULL,PRIMARY KEY (srn,classCode),FOREIGN KEY (classCode) REFERENCES classes (classCode))')
    
def create_table_submissions():
    c.execute('CREATE TABLE IF NOT EXISTS submissions(response varchar(2048) NOT NULL,status int DEFAULT 0,marks int DEFAULT 0,srn varchar(20) NOT NULL,assignmentId varchar(256) NOT NULL,createdAt datetime NOT NULL,PRIMARY KEY (srn,assignmentId),FOREIGN KEY (srn) REFERENCES students (srn),FOREIGN KEY (assignmentId) REFERENCES assignments (assignmentId) )')

###################################################   ADD DATA   ##############################################################
    
def add_data_faculties(facultyId,firstName,lastName,email,DOB,age,address,institution,contact,password):
    c.execute('INSERT INTO faculties (facultyId,firstName,lastName,email,DOB,age,address,institution,contact,password) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);',(facultyId,firstName,lastName,email,DOB,age,address,institution,contact,password))
    mydb.commit()

def add_data_classes(classCode,course,subject,className,cr,facultyId):
    c.execute('INSERT INTO classes (classCode,course,subject,className,cr,facultyId) VALUES(%s,%s,%s,%s,%s,%s);',(classCode,course,subject,className,cr,facultyId))
    mydb.commit()
    
def add_data_assignments(assignmentId,assignmentNumber,title,description,typee, resources,deadline,classCode,facultyId):
    c.execute('INSERT INTO assignments(assignmentId,assignmentNumber,title,description,type, resources,deadline,classCode,facultyId) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s);',(assignmentId,assignmentNumber,title,description,typee, resources,deadline,classCode,facultyId))
    mydb.commit()

def add_data_students(srn,name,cr,isCr,classCode):
    c.execute('INSERT INTO students(srn,name,cr,isCr,classCode) VALUES(%s,%s,%s,%s,%s);',(srn,name,cr,isCr,classCode))
    mydb.commit()
    
def add_data_submissions(response,status,marks ,srn,assignmentId,createdAt):
    c.execute('INSERT INTO submissions(response,status,marks ,srn,assignmentId,createdAt) VALUES(%s,%s,%s,%s,%s,%s);',(response,status,marks ,srn,assignmentId,createdAt))
    mydb.commit()
    
#################################################   VIEW DATA   #########################################

def view_all_data_faculties():
    c.execute('SELECT * FROM faculties')
    data = c.fetchall()
    return data

def view_all_data_classes():
    c.execute('SELECT * FROM classes')
    data = c.fetchall()
    return data

def view_all_data_assignments():
    c.execute('SELECT * FROM assignments')
    data = c.fetchall()
    return data

def view_all_data_students():
    c.execute('SELECT * FROM students')
    data = c.fetchall()
    return data

def view_all_data_submissions():
    c.execute('SELECT * FROM submissions')
    data = c.fetchall()
    return data

#######################################################   UPDATE DETAILS   ####################################################

def update_details_faculties(new_facultyId,new_firstName,new_lastName,new_email,new_DOB,new_age,new_address,new_institution,new_contact,new_password,facultyId,firstName,lastName,email,DOB,age,address,institution,contact,password):
    c.execute("UPDATE faculties SET facultyId=%s, firstName=%s, lastName=%s, email=%s, DOB=%s, age=%s,address=%s,institution=%s,contact=%s,password=%s WHERE facultyId=%s and firstName=%s and lastName=%s and email=%s and DOB=%s and age=%s and address=%s and institution=%s and contact=%s and password=%s",
              (new_facultyId,new_firstName,new_lastName,new_email,new_DOB,new_age,new_address,new_institution,new_contact,new_password,facultyId,firstName,lastName,email,DOB,age,address,institution,contact,password))
    mydb.commit()
    c.execute("SELECT facultyId,firstName FROM faculties")
    data = c.fetchall()
    return data

def update_details_classes(new_classCode,new_course,new_subject,new_className,new_cr,new_facultyId,classCode,course,subject,className,cr,facultyId):
    c.execute('UPDATE classes SET classCode=%s,course=%s,subject=%s,className=%s,cr=%s,facultyId=%s WHERE classCode=%s and course=%s and subject=%s and className=%s and cr=%s and facultyId=%s',(new_classCode,new_course,new_subject,new_className,new_cr,new_facultyId,classCode,course,subject,className,cr,facultyId))
    mydb.commit()
    c.execute("SELECT classCode,className FROM classes")
    data=c.fetchall()
    return data 
#new_assignmentId,new_assignmentNumber,new_title,new_description,new_typee, new_resources,new_deadline,new_classCode,new_facultyId,assignmentId,assignmentNumber,title,description,typee, resources,deadline,classCode,facultyId
def update_details_assignments(new_assignmentId,new_assignmentNumber,new_title,new_description,new_typee, new_resources,new_deadline,new_classCode,new_facultyId,assignmentId,assignmentNumber,title,description,typee, resources,deadline,classCode,facultyId):
    c.execute('UPDATE assignments SET assignmentId=%s,assignmentNumber=%s,title=%s,description=%s,type=%s,resources=%s,deadline=%s,classCode=%s,facultyId=%s WHERE assignmentId=%s and assignmentNumber=%s and title=%s and description=%s and type=%s and resources=%s and deadline=%s and classCode=%s and facultyId=%s',(new_assignmentId,new_assignmentNumber,new_title,new_description,new_typee, new_resources,new_deadline,new_classCode,new_facultyId,assignmentId,assignmentNumber,title,description,typee, resources,deadline,classCode,facultyId))
    mydb.commit()
    c.execute("SELECT assignmentId,title FROM assignments")
    data=c.fetchall()
    return data 

def update_details_students(new_srn,new_name,new_cr,new_isCr,new_classCode,srn,name,cr,isCr,classCode):
    c.execute('UPDATE students SET srn=%s,name=%s,cr=%s,isCr=%s,classCode=%s WHERE srn=%s and name=%s and cr=%s and isCr=%s and classCode=%s ',(new_srn,new_name,new_cr,new_isCr,new_classCode,srn,name,cr,isCr,classCode))
    mydb.commit()
    c.execute("SELECT srn,name FROM students")
    data=c.fetchall()
    return data

def update_details_submissions(new_response,new_status,new_marks ,new_srn,new_assignmentId,new_createdAt,response,status,marks ,srn,assignmentId,createdAt):
    c.execute('UPDATE submissions SET response=%s,status=%s,marks=%s,srn=%s,assignmentId=%s,createdAt=%s WHERE response=%s and status=%s and marks=%s and srn=%s and assignmentId=%s and createdAt=%s',(new_response,new_status,new_marks ,new_srn,new_assignmentId,new_createdAt,response,status,marks ,srn,assignmentId,createdAt))
    mydb.commit()
    c.execute("SELECT srn,response FROM submissions")
    data=c.fetchall()
    return data

###############################################   DELETE TABLES   ###########################################################

def delete_data_faculties(facultyId):
    c.execute('DELETE FROM faculties WHERE facultyId="{}"'.format(facultyId))
    mydb.commit()
    
def delete_data_classess(classCode):
    c.execute('DELETE FROM classes WHERE classCode="{}"'.format(classCode))
    mydb.commit()
    
def delete_data_assignments(assignmentId):
    c.execute('DELETE FROM assignments WHERE assignmentId="{}"'.format(assignmentId))
    mydb.commit()
    
def delete_data_students(srn):
    c.execute('DELETE FROM students WHERE srn="{}"'.format(srn))
    mydb.commit()

def delete_data_submissions(srn):
    c.execute('DELETE FROM submissions WHERE srn="{}"'.format(srn))
    mydb.commit()
    
########################################   ADDITIONAL FUNCTIONS    #######################################
    
def view_only_facultiesId():
    c.execute('SELECT facultyId FROM faculties')
    data = c.fetchall()
    return data

def view_only_classCode():
    c.execute('SELECT classCode FROM classes')
    data= c.fetchall()
    return data

def view_only_srn():
    c.execute('SELECT srn FROM students')
    data = c.fetchall()
    return data

def view_only_assignmentId():
    c.execute('SELECT assignmentId FROM assignments')
    data = c.fetchall()
    return data 

def get_details_faculties(facultyId):
    c.execute('SELECT * FROM faculties WHERE facultyId="{}"'.format(facultyId))
    data = c.fetchall()
    return data

def get_details_classes(classCode):
    c.execute('SELECT * FROM classes WHERE classCode="{}"'.format(classCode))
    data = c.fetchall()
    return data

def get_details_assignments(assignmentId):
    c.execute('SELECT * FROM assignments WHERE assignmentId="{}"'.format(assignmentId))
    data = c.fetchall()
    return data

def get_details_students(srn):
    c.execute('SELECT * FROM students WHERE srn="{}"'.format(srn))
    data = c.fetchall()
    return data

def get_details_submissions(srn):
    c.execute('SELECT * FROM submissions WHERE srn="{}"'.format(srn))
    data = c.fetchall()
    return data

