import streamlit as st
import pandas as pd
from db import add_data_faculties,add_data_classes,add_data_assignments,add_data_students,add_data_submissions
from db import view_all_data_faculties,view_only_facultiesId,view_only_classCode,view_all_data_classes,view_all_data_students,view_only_srn,view_all_data_assignments,view_only_assignmentId

def create_faculties():
    col1, col2 = st.columns(2)
    with col1:
        facultyId = st.text_input("Faculty ID : ")
        firstName = st.text_input("First Name : ")
        lastName = st.text_input("Last Name : ")
        age = st.text_input("Age: ")
        address = st.text_area("Address: ")

    with col2:
        DOB = st.date_input("DOB: ")
        contact = st.text_input("Phone Number:")
        institution = st.text_input("Institution: ")
        email = st.text_input("Email ID : ")
        password = st.text_input("Enter a password", type="password")

    if st.button("Add faculty"):
        add_data_faculties(facultyId,firstName,lastName,email,DOB,age,address,institution,contact,password)
        st.success("Successfully added faculty: {}".format(facultyId))
        
def create_classes():
    col1, col2 = st.columns(2)
    with col1:
        classCode = st.text_input("Class code : ")
        className = st.text_input("Class Name : ")
        subject = st.text_input("Subject : ")

    with col2:
        course= st.text_input("Course: ")
        cr = st.text_input("CR:")
        result = view_all_data_faculties()
        df = pd.DataFrame(result, columns=['facultyId','firstName','lastName','email','DOB','age','address','institution','contact','password'])
        # with st.expander("Current faculties"):
        #     st.dataframe(df)
        list_of_faculties = [i[0] for i in view_only_facultiesId()]
        facultyId = st.selectbox("Select a faculty", list_of_faculties)

    if st.button("Create/Add class"):
        add_data_classes(classCode,course,subject,className,cr,facultyId)
        st.success("Successfully created class: {}".format(className))
    
def create_assignments():
    col1, col2 = st.columns(2)
    with col1:
        assignmentId = st.text_input("Assignment ID : ")
        assignmentNumber = st.text_input("Assignment Number : ")
        title = st.text_input("Title of assignment : ")
        description = st.text_area("Description")

    with col2:
        typee= st.text_input("Type of submission: ")
        resources = st.text_input("Resources :")
        deadline = st.date_input("Deadline: ")

        result = view_all_data_faculties()
        df = pd.DataFrame(result, columns=['facultyId','firstName','lastName','email','DOB','age','address','institution','contact','password'])
        # with st.expander("Current faculties"):
        #     st.dataframe(df['facultyId'])
        list_of_faculties = [i[0] for i in view_only_facultiesId()]
        facultyId = st.selectbox("Select a faculty", list_of_faculties)

        result1 = view_all_data_classes()
        df1 = pd.DataFrame(result1, columns=['classCode','course','subject','className','cr','facultyId'])
        # with st.expander("Existing Classes"):
        #     st.dataframe(df1)
        list_of_class = [i[0] for i in view_only_classCode()]
        classCode = st.selectbox("Select class", list_of_class)
    if st.button("post assignment"):
        add_data_assignments(assignmentId,assignmentNumber,title,description,typee, resources,deadline,classCode,facultyId)
        st.success("Successfully posted assignment: {}".format(title))
    
def create_students():
    col1, col2 = st.columns(2)
    with col1:
        srn = st.text_input("SRN: ")
        name = st.text_input("Name : ")
        cr = st.text_input("CR : ")

    with col2:
        isCr = st.radio("Is CR?",["Yes","No"])
        result1 = view_all_data_classes()
        df1 = pd.DataFrame(result1, columns=['classCode','course','subject','className','cr','facultyId'])
        # with st.expander("Existing Classes"):
        #     st.dataframe(df1)
        list_of_class = [i[0] for i in view_only_classCode()]
        classCode = st.selectbox("Select a faculty", list_of_class)

    if st.button("Add student "):
        add_data_students(srn,name,cr,isCr,classCode)
        st.success("Successfully added student with SRN: {}".format(srn))
        
def create_submissions():
    col1, col2 = st.columns(2)
    with col1:
        response = st.radio("Submitted?",["Yes","No"])
        marks = st.number_input("Marks")
        result1 = view_all_data_students()
        df1 = pd.DataFrame(result1, columns=['srn','name','cr','isCr','classCode'])
        # with st.expander("students"):
        #     st.dataframe(df1)
        list_of_srn = [i[0] for i in view_only_srn()]
        srn = st.selectbox("Select a SRN", list_of_srn)
        status = st.radio("Status:",["OK","ReSubmit"])

    with col2:
        createdAt = st.date_input("Created/Posted On: ")
        result = view_all_data_assignments()
        df = pd.DataFrame(result, columns=['assignmentId','assignmentNumber','title','description','type', 'resources','deadline','classCode','facultyId'])
        # with st.expander("Existing Assignments"):
        #     st.dataframe(df)
        list_of_assignments = [i[0] for i in view_only_assignmentId()]
        assignmentId = st.selectbox("Select the assignment", list_of_assignments)

    if st.button("Create Submission"):
        add_data_submissions(response,status,marks ,srn,assignmentId,createdAt)
        st.success("Successfully added submission,status: {}".format(response))
        