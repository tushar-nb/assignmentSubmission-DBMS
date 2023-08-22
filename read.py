import pandas as pd
import streamlit as st
from db import view_all_data_faculties,view_all_data_classes,view_all_data_assignments,view_all_data_students,view_all_data_submissions    

def read_faculties():
    result = view_all_data_faculties()
    df = pd.DataFrame(result, columns=['facultyId','firstName','lastName','email','DOB','age','address','institution','contact','password'])
    with st.expander("View all faculties"):
        st.dataframe(df)
    # with st.expander("Faculties Details"):
    #     faculties_df = df['facultyId'].value_counts().to_frame()
    #     faculties_df = faculties_df.reset_index()
    #     st.dataframe(faculties_df)

def read_classes():
    result = view_all_data_classes()
    df = pd.DataFrame(result, columns=['classCode','course','subject','className','cr','facultyId'])
    with st.expander("View all existing classes"):
        st.dataframe(df)
    # with st.expander("Class Details"):
    #     classes_df = df['classCode'].value_counts().to_frame()
    #     classes_df = classes_df.reset_index()
    #     st.dataframe(classes_df)
    
def read_assignments():
    result = view_all_data_assignments()
    df = pd.DataFrame(result, columns=['assignmentId','assignmentNumber','title','description','type', 'resources','deadline','classCode','facultyId'])
    with st.expander("View all assignments"):
        st.dataframe(df)
    # with st.expander("Assignment details"):
    #     assignments_df = df['assignmentsId'].value_counts().to_frame()
    #     assignments_df = assignments_df.reset_index()
    #     st.dataframe(assignments_df)

def read_students():
    result = view_all_data_students()
    df = pd.DataFrame(result, columns=['srn','name','cr','isCr','classCode'])
    with st.expander("View all students"):
        st.dataframe(df)
    # with st.expander("students details"):
    #     students_df = df['isCr'].value_counts().to_frame()
    #     students_df = students_df.reset_index()
    #     st.dataframe(students_df)

def read_submissions():
    result = view_all_data_submissions()
    df = pd.DataFrame(result, columns=['response','status','marks' ,'srn','assignmentId','createdAt'])
    with st.expander("View all submissions"):
        st.dataframe(df)
    # with st.expander("submissions details"):
    #     submissions_df = df["response"].value_counts().to_frame()
    #     submissions_df = submissions_df.reset_index()
    #     st.dataframe(submissions_df)