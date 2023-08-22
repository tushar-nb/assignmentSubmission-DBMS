import datetime

import pandas as pd
import streamlit as st
from db import view_all_data_faculties, view_only_facultiesId, get_details_faculties, update_details_faculties
from db import view_all_data_classes, view_only_classCode, get_details_classes, update_details_classes
from db import view_all_data_assignments, view_only_assignmentId, get_details_assignments, update_details_assignments
from db import view_all_data_students, view_only_srn, get_details_students, update_details_students
from db import view_all_data_submissions, view_only_srn, get_details_submissions, update_details_submissions


def update_faculties():
    result = view_all_data_faculties()
    # st.write(result)
    df = pd.DataFrame(result, columns=['facultyId','firstName','lastName','email','DOB','age','address','institution','contact','password'])
    with st.expander("Existing faculties"):
        st.dataframe(df)
    list_of_facultiesId = [i[0] for i in view_only_facultiesId()]
    selected_facultyId = st.selectbox("Faculty ID To Edit", list_of_facultiesId)
    selected_result = get_details_faculties(selected_facultyId)
    # st.write(selected_result)
    if selected_result:
        facultyId = selected_result[0][0]
        firstName = selected_result[0][1]
        lastName = selected_result[0][2]
        email = selected_result[0][3]
        DOB = selected_result[0][4]
        age = selected_result[0][5]
        address = selected_result[0][6]
        institution = selected_result[0][7]
        contact = selected_result[0][8]
        password = selected_result[0][9]

        # Layout of Create

        col1, col2 = st.columns(2)
        with col1:
            new_facultyId = st.text_input("Faculty ID: ",facultyId)
            # st.write("Faculty ID: ",facultyId)
            new_firstName = st.text_input("First Name : ", firstName)
            new_lastName = st.text_input("Last Name: ",lastName)
            new_email = st.text_input("Email: ",email)
            new_DOB = st.text_input("DOB ",DOB)
        with col2:
            new_age = st.text_input("Age : ", age)
            new_address = st.text_input("Address: ",address)
            new_institution = st.text_input("Institution : ", institution)
            new_password = st.text_input("password : ", password,type='password')
            new_contact = st.text_input("contact : ", contact)

        if st.button("Update Faculty"):
            update_details_faculties(new_facultyId,new_firstName,new_lastName,new_email,new_DOB,new_age,new_address,new_institution,new_contact,new_password,facultyId,firstName,lastName,email,DOB,age,address,institution,contact,password)
            st.success("Successfully updated:: {} ::{}".format(new_facultyId, new_firstName))

    result2 = view_all_data_faculties()
    df2 = pd.DataFrame(result2, columns=['facultyId','firstName','lastName','email','DOB','age','address','institution','contact','password'])
    with st.expander("Updated data"):
        st.dataframe(df2)
        
def update_classes():
    result = view_all_data_classes()
    # st.write(result)
    df = pd.DataFrame(result, columns=['classCode','course','subject','className','cr','facultyId'])
    with st.expander("Existing classes"):
        st.dataframe(df)
    list_of_classCode = [i[0] for i in view_only_classCode()]
    selected_classCode = st.selectbox("Class To Edit", list_of_classCode)
    selected_result = get_details_classes(selected_classCode)
    # st.write(selected_result)
    if selected_result:
        classCode = selected_result[0][0]
        course = selected_result[0][1]
        subject = selected_result[0][2]
        className = selected_result[0][3]
        cr = selected_result[0][4]
        facultyId = selected_result[0][5]
        # Layout of Create

        col1, col2 = st.columns(2)
        with col1:
            new_facultyId = st.text_input("Faculty ID: ",facultyId)
            # st.write("Faculty ID: ",facultyId)
            new_classCode = st.text_input("Class code : ", classCode)
            new_course = st.text_input("Course Name: ",course)
            
        with col2:
            new_subject = st.text_input("subject : ", subject)
            new_className = st.text_input("Class Name: ",className)
            new_cr = st.text_input("CR : ", cr)

        if st.button("Update Class"):
            update_details_classes(new_classCode,new_course,new_subject,new_className,new_cr,new_facultyId,classCode,course,subject,className,cr,facultyId)
            st.success("Successfully updated:: {} ::{}".format(new_classCode, new_className))

    result2 = view_all_data_classes()
    df2 = pd.DataFrame(result2, columns=['classCode','course','subject','className','cr','facultyId'])
    with st.expander("Updated data"):
        st.dataframe(df2)
        
def update_assignments():
    result = view_all_data_assignments()
    # st.write(result)
    df = pd.DataFrame(result, columns=['assignmentId','assignmentNumber','title','description','type', 'resources','deadline','classCode','facultyId'])
    with st.expander("Existing assignments"):
        st.dataframe(df)
    list_of_assignments = [i[0] for i in view_only_assignmentId()]
    selected_assignments = st.selectbox("Assignment To Edit", list_of_assignments)
    selected_result = get_details_assignments(selected_assignments)
    # st.write(selected_result)
    if selected_result:
        assignmentId = selected_result[0][0]
        assignmentNumber = selected_result[0][1]
        title = selected_result[0][2]
        description = selected_result[0][3]
        typee = selected_result[0][4]
        resources = selected_result[0][5]
        deadline = selected_result[0][6]
        classCode = selected_result[0][7]
        facultyId = selected_result[0][8]
        # Layout of Create

        col1, col2 = st.columns(2)
        with col1:
            new_assignmentId = st.text_input("Assignment ID: ",assignmentId)
            # st.write("Faculty ID: ",facultyId)
            new_assignmentNumber = st.text_input("Assignment Number : ", assignmentNumber)
            new_title = st.text_input("Title: ",title)
            new_description = st.text_area("Description: ",description)
            new_typee = st.text_input("Type: ",typee)
            
        with col2:
            new_resources = st.text_input("Resources : ", resources)
            new_deadline = st.text_input("Deadline: ",deadline)
            new_classCode = st.text_input("Class code : ", classCode)
            new_facultyId = st.text_input("Faculty ID : ", facultyId)

        if st.button("Update assignment"):
            update_details_assignments(new_assignmentId,new_assignmentNumber,new_title,new_description,new_typee, new_resources,new_deadline,new_classCode,new_facultyId,assignmentId,assignmentNumber,title,description,typee, resources,deadline,classCode,facultyId)
            st.success("Successfully updated:: {}  ::{}".format(new_assignmentId, new_title))

    result2 = view_all_data_assignments()
    df2 = pd.DataFrame(result2, columns=['assignmentId','assignmentNumber','title','description','type', 'resources','deadline','classCode','facultyId'])
    with st.expander("Updated data"):
        st.dataframe(df2)
        
def update_students():
    result = view_all_data_students()
    # st.write(result)
    df = pd.DataFrame(result, columns=['srn','name','cr','isCr','classCode'])
    with st.expander("Existing Students"):
        st.dataframe(df)
    list_of_students = [i[0] for i in view_only_srn()]
    selected_students = st.selectbox("Student To Edit", list_of_students)
    selected_result = get_details_students(selected_students)
    # st.write(selected_result)
    if selected_result:
        srn = selected_result[0][0]
        name = selected_result[0][1]
        cr = selected_result[0][2]
        isCr = selected_result[0][3]
        classCode = selected_result[0][4]
        # Layout of Create

        col1, col2 = st.columns(2)
        with col1:
            new_srn = st.text_input("SRN: ",srn)
            # st.write("Faculty ID: ",facultyId)
            new_name = st.text_input("Name : ", name)
            new_cr = st.text_input("CR: ",cr)
            
        with col2:
            new_isCr = st.text_input("IsCR: ",isCr)
            new_classCode = st.text_input("Class code : ", classCode)
            
        if st.button("Update student"):
            update_details_students(new_srn,new_name,new_cr,new_isCr,new_classCode,srn,name,cr,isCr,classCode)
            st.success("Successfully updated:: {} ::{}".format(new_srn, new_name))

    result2 = view_all_data_students()
    df2 = pd.DataFrame(result2, columns=['srn','name','cr','isCr','classCode'])
    with st.expander("Updated data"):
        st.dataframe(df2)

def update_submissions():
    result = view_all_data_submissions()
    # st.write(result)
    df = pd.DataFrame(result, columns=['response','status','marks' ,'srn','assignmentId','createdAt'])
    with st.expander("Submissions"):
        st.dataframe(df)
    list_of_submissions = [i[0] for i in view_only_srn()]
    selected_submissions = st.selectbox("Submissions To Edit", list_of_submissions)
    selected_result = get_details_submissions(selected_submissions)
    # st.write(selected_result)
    if selected_result:
        response = selected_result[0][0]
        status = selected_result[0][1]
        marks = selected_result[0][2]
        srn = selected_result[0][3]
        assignmentId = selected_result[0][4]
        createdAt = selected_result[0][5]
        # Layout of Create

        col1, col2 = st.columns(2)
        with col1:
            new_response = st.text_input("Response: ",response)
            # st.write("Faculty ID: ",facultyId)
            # new_status = st.radio("Status : ",["Ok","Resubmit"])
            new_status = st.text_input("Status : ",status)
            new_marks = st.text_input("Marks: ",marks)
            
        with col2:
            new_srn = st.text_input("SRN: ",srn)
            new_assignmentId = st.text_input("Assignment ID : ", assignmentId)
            new_createdAt = st.date_input("Created at : ", createdAt)
            
        if st.button("Update submission"):
            update_details_submissions(new_response,new_status,new_marks ,new_srn,new_assignmentId,new_createdAt,response,status,marks ,srn,assignmentId,createdAt)
            st.success("Successfully updated:: {} to ::{}".format(new_srn, new_response))

    result2 = view_all_data_submissions()
    df2 = pd.DataFrame(result2, columns=['response','status','marks' ,'srn','assignmentId','createdAt'])
    with st.expander("Updated data"):
        st.dataframe(df2)
