import streamlit as st
import info1
import pandas as pd

### PS C:\Users\micha> cd Downloads
### PS C:\Users\micha\Downloads> cd "Lab03 in Downloads"
### PS C:\Users\micha\Downloads\Lab03> streamlit run portfolio.py

# About Me Section
def aboutMeSection():
    st.header("About Me")
    st.image(info1.profile_picture, width = 200)
    st.write(info1.about_me)
    st.write('---')
aboutMeSection()

def linksSection():
    st.sidebar.header("Links")
    st.sidebar.text("Connect with me on LinkedIn")
    linkedin_link=f'<a href="{info1.my_linkedin_url}"><img src="{info1.linkedin_image_url}" alt="LinkedIn" width="75" height="75">'
    st.sidebar.markdown(linkedin_link,unsafe_allow_html=True)
    st.sidebar.text("Checkout my work")
    github_link=f'<a href="{info1.my_github_url}"><img src="{info1.github_image_url}" alt="Github" width="65" height="65">'
    st.sidebar.markdown(github_link,unsafe_allow_html=True)
    st.sidebar.text("Or email me!")
    email_html=f'<a href="mailto:{info1.my_email_address}"><img src="{info1.email_image_url}" alt="Email" width="75" height="75">'
    st.sidebar.markdown(email_html,unsafe_allow_html=True)
linksSection()

# Education
def educationSection(education_data, course_data):
    st.header("Edcuation")
    st.subheader(f'{education_data["Institution"]}')
    st.write(f'**Degree:**{education_data["Degree"]}')
    st.write(f'**GPA:**{education_data["GPA"]}')
    st.write('**Relevant Coursework:**')
    coursework=pd.DataFrame(course_data)
    st.dataframe(coursework, column_config={
        "code":"Course Code",
        "names":"Course Names",
        "semester-taken": "Semester Taken",
        "skill": "What I Learned"},
        hide_index=True,
        )
    st.write("---")
educationSection(info1.education_data, info1.course_data)

# Professional Experience
def experienceSection(experience_data):
    st.header("Professional Experience")
    for job_title, (job_description, image) in experience_data.items():
        expander = st.expander(f"{job_title}")
        expander.image(image, width=250)
        for bullet in job_description:
            expander.write(bullet)
    st.write("---")
experienceSection(info1.experience_data)

# Projects
def projectSections(projects_data):
    st.header("Projects")
    for project_name, project_Description in projects_data.items():
        expander=st.expander(f"{project_name}")
        expander.write(project_Description)
    st.write("---")
projectSections(info1.projects_data)
    
# Skills
def skillSection(sales_methods, spoken_data):
    st.header("Skills")
    st.subheader("Sales Skills")
    for skill, percentage in sales_methods.items():
        st.write(f"{skill}")
        st.progress(percentage)
    st.subheader("Spoken Languages")
    for spoken, proficiency in spoken_data.items():
        st.write(f"{spoken}: {proficiency}")
    st.write("---")
skillSection(info1.sales_methods, info1.spoken_data)


# Activites
def activitiesSection(leadership_data, activity_data):
    st.header("Activities")
    tab1, tab2 = st.tabs(["Leadership", "Community Service"])
    with tab1:
        st.subheader("Leadership")
        for title, (details, image) in leadership_data.items():
            expander = st.expander(f"{title}")
            expander.image(image, width=250)
            for bullet in details:
                expander.write(bullet)
    with tab2:
        st.subheader("Community Service")
        for title, details in activity_data.items():
            expander = st.expander(f"{title}")
            for bullet in details:
                expander.write(bullet)

    st.write("---")

activitiesSection(info1.leadership_data, info1.activity_data)
