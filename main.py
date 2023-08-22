import streamlit as st 
import mysql.connector

from db import create_table_faculties,create_table_classes,create_table_assignments,create_table_students,create_table_submissions
from create import create_faculties,create_classes,create_assignments,create_students,create_submissions
from read import read_faculties,read_classes,read_assignments,read_students,read_submissions
from update import update_faculties,update_classes,update_assignments,update_students,update_submissions
from delete import delete_faculties,delete_classes,delete_assignments,delete_students,delete_submissions
# from delete import delete
# from read import read
# from update import update

def main():
    st.subheader("          PES1UG20CS608")
    st.title("ASSIGNMENT SUBMISSION MANAGEMENT SYSTEM")
    Faculty_menu = ["---Select any One---","Add a new Faculty","Display Faculty","Edit faculty details","Remove a faculty"]
    choice1 = st.sidebar.selectbox("Faculty Menu",Faculty_menu)
    create_table_faculties()
    if choice1 == "Add a new Faculty":
        st.subheader("Add a new faculty:")
        create_faculties()
        choice1="---Select any One---"
        
    elif choice1 == "Display Faculty":
        st.subheader("View all faculties:")
        read_faculties()
        
    elif choice1 == "Edit faculty details":
        st.subheader("Edit a faculty details:")
        update_faculties()
        
    elif choice1 == "Remove a faculty":
        st.subheader("Remove a faculty:")
        delete_faculties()
             
    Class_menu = ["---Select any One---","Create a new class","List all the classes","Edit a class","Delete a class "]
    choice2 = st.sidebar.selectbox("Class Menu",Class_menu)
    create_table_classes() 
    if choice2 == "Create a new class":
        st.subheader("Create a new class:")
        create_classes()
        
    elif choice2 == "List all the classes":
        st.subheader("View all existing classes:")
        read_classes()
        
    elif choice2 == "Edit a class":
        st.subheader("Edit a class details:")
        update_classes()
        
    elif choice2 == "Delete a class ":
        st.subheader("Delete a class:")
        delete_classes()
    
    Assignment_menu = ["---Select any One---","Create a new assignment","Display all the assignments","Edit assignment details","Delete a assignment"]
    choice3 = st.sidebar.selectbox("Assignment Menu",Assignment_menu)
    create_table_assignments() 
    if choice3 == "Create a new assignment":
        st.subheader("Create a new assignment:")
        create_assignments()
        
    elif choice3 == "Display all the assignments":
        st.subheader("View all the assignments:")
        read_assignments()
        
    elif choice3 == "Edit assignment details":
        st.subheader("Edit a assignment details:")
        update_assignments()
        
    elif choice3 == "Delete a assignment":
        st.subheader("Delete a assignment:")
        delete_assignments()
    
    Student_menu = ["---Select any One---","Add a new Student","Display all students","Edit student details","Remove a student"]
    choice4 = st.sidebar.selectbox("Student Menu",Student_menu)
    create_table_students() 
    if choice4 == "Add a new Student":
        st.subheader("Add a new student:")
        create_students()
        
    elif choice4 == "Display all students":
        st.subheader("View all students:")
        read_students()
        
    elif choice4 == "Edit student details":
        st.subheader("Edit the details of a student:")
        update_students()
        
    elif choice4 == "Remove a student":
        st.subheader("Remove a student:")
        delete_students()
    
    Submission_menu = ["---Select any One---","Add entry to submissions","View all submissions","Edit a submission","Remove a submission"]
    choice5 = st.sidebar.selectbox("Submissions Menu",Submission_menu)
    create_table_submissions() 
    if choice5 =="Add entry to submissions":
        st.subheader("Add a entry to submission: ")
        create_submissions()
    elif choice5 == "View all submissions":
        st.subheader("View all submissions:")
        read_submissions()
    elif choice5 =="Edit a submission":
        st.subheader("Edit a submission:")
        update_submissions()
    elif choice5 =="Remove a submission":
        st.subheader("Remove/Delete a submission:")
        delete_submissions()
    
if __name__ == '__main__':
    main()