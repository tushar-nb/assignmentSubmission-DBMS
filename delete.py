import pandas as pd
import streamlit as st
from db import view_all_data_faculties, view_only_facultiesId, delete_data_faculties
from db import view_all_data_classes, view_only_classCode, delete_data_classess
from db import view_all_data_assignments, view_only_assignmentId, delete_data_assignments
from db import view_all_data_students, view_only_srn, delete_data_students
from db import view_all_data_submissions, view_only_srn, delete_data_submissions


def delete_faculties():
    result = view_all_data_faculties()
    df = pd.DataFrame(result, columns=['facultyId','firstName','lastName','email','DOB','age','address','institution','contact','password'])
    with st.expander("Current data"):
        st.dataframe(df)

    list_of_facultyId = [i[0] for i in view_only_facultiesId()]
    selected_faculties = st.selectbox("Faculty ID to be deleted", list_of_facultyId)
    st.warning("Do you want to delete ::{}".format(selected_faculties))
    if st.button("Delete faculty"):
        delete_data_faculties(selected_faculties) 
        st.success("Faculty entry has been deleted successfully")
    new_result = view_all_data_faculties()
    df2 = pd.DataFrame(new_result, columns=['facultyId','firstName','lastName','email','DOB','age','address','institution','contact','password'])
    with st.expander("Updated table"):
        st.dataframe(df2)
        
def delete_classes():
    result = view_all_data_classes()
    df = pd.DataFrame(result, columns=['classCode','course','subject','className','cr','facultyId'])
    with st.expander("Current data"):
        st.dataframe(df)

    list_of_classCode = [i[0] for i in view_only_classCode()]
    selected_classCode = st.selectbox("ClassCode to be deleted", list_of_classCode)
    st.warning("Do you want to delete ::{}".format(selected_classCode))
    if st.button("Delete Class"):
        delete_data_classess(selected_classCode) 
        st.success("Class entry has been deleted successfully")
    new_result = view_all_data_classes()
    df2 = pd.DataFrame(new_result, columns=['classCode','course','subject','className','cr','facultyId'])
    with st.expander("Updated table"):
        st.dataframe(df2)
        
def delete_assignments():
    result = view_all_data_assignments()
    df = pd.DataFrame(result, columns=['assignmentId','assignmentNumber','title','description','type', 'resources','deadline','classCode','facultyId'])
    with st.expander("Current data"):
        st.dataframe(df)

    list_of_assignmentId = [i[0] for i in view_only_assignmentId()]
    selected_assignmentId = st.selectbox("Assignment to be deleted", list_of_assignmentId)
    st.warning("Do you want to delete ::{}".format(selected_assignmentId))
    if st.button("Delete Assignment"):
        delete_data_assignments(selected_assignmentId) 
        st.success("Assignment entry has been deleted successfully")
    new_result = view_all_data_assignments()
    df2 = pd.DataFrame(new_result, columns=['assignmentId','assignmentNumber','title','description','type', 'resources','deadline','classCode','facultyId'])
    with st.expander("Updated table"):
        st.dataframe(df2)
        
def delete_students():
    result = view_all_data_students()
    df = pd.DataFrame(result, columns=['srn','name','cr','isCr','classCode'])
    with st.expander("Current data"):
        st.dataframe(df)

    list_of_srn = [i[0] for i in view_only_srn()]
    selected_srn = st.selectbox("SRN to be deleted", list_of_srn)
    st.warning("Do you want to delete ::{}".format(selected_srn))
    if st.button("Delete Student"):
        delete_data_students(selected_srn) 
        st.success("Student entry has been deleted successfully")
    new_result = view_all_data_students()
    df2 = pd.DataFrame(new_result, columns=['srn','name','cr','isCr','classCode'])
    with st.expander("Updated table"):
        st.dataframe(df2)
        
def delete_submissions():
    result = view_all_data_submissions()
    df = pd.DataFrame(result, columns=['response','status','marks' ,'srn','assignmentId','createdAt'])
    with st.expander("Current data"):
        st.dataframe(df)

    list_of_srn = [i[0] for i in view_only_srn()]
    selected_srn = st.selectbox("Submission to be deleted", list_of_srn)
    st.warning("Do you want to delete ::{}".format(selected_srn))
    if st.button("Delete Submission"):
        delete_data_submissions(selected_srn) 
        st.success("Student entry has been deleted successfully")
    new_result = view_all_data_submissions()
    df2 = pd.DataFrame(new_result, columns=['response','status','marks' ,'srn','assignmentId','createdAt'])
    with st.expander("Updated table"):
        st.dataframe(df2)