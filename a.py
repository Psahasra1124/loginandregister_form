import streamlit as st
#header
st.header("Anurag University Student Records Management💻-Peddi Sahasra")
#Title of the app
st.title("Welcome to student management system")
#Subheader of the app
st.subheader("Manage student records efficiently and effectively")
#horizontal line
st.markdown("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
#text method to display information
st.text("This application allows you to perform CRUD operations on student records uing a mysql database")
#Write method to provide additional details
st.write("Hello streamlit")
st.write(123)
st.write([1,2,3])
st.write({"name":"Sumit","Role":"Trainer"})
#Markdown method to format text
st.markdown("### Features of the application:")
st.markdown("**Bold Text**")
st.markdown("**Italic Text**")
st.markdown("- Item 1\n- Item 2")
st.markdown("<h3 style='color:red'>Red Text</h3>",unsafe_allow_html=True)
#Caption method to add captions
st.caption("This is a caption for the student management system.")
#Code method to display snippets
st.code("""
        def add(a,b):
            return a+b
        """,language="python")
#latex method to render mathematical expressions
st.latex(r'''
         a^2+b^2=c^2
         ''')
#Divider method to seperate sections
st.divider()
#button method to create a button
if st.button("Click me"):
    st.write("Button clicked!")
    st.success("Operation successful!")
    st.balloons()
else:
    st.write("Button not clicked yet.")
    st.error("Connection error!")
#Text input method to get user input
name=st.text_input("Enter your name:")
if name=="":
    st.warning("Name cannot be empty❗")
elif not name.isalpha():
    st.error("Invalid input ❌ Please enter only alphabets (no numbers or symbols).")
else:
    st.success(f"Hello,{name}😊")
feedback=st.text_area("Enter feedback")
st.write(feedback)
#chckebox method to create a checkbox
if st.checkbox("I agree to the terms and conditions"):
    st.write("Thank you for agreeing!")
#Radio button method to create radio buttons
gender=st.radio("Select your gender:",("Male👨","Female🚺","Other"))
st.write(f"You selected:{gender}")
#Selectbox method to create dropdown
country=st.selectbox("Select your country:",("India","Dubai","Australia","Florida"))
st.write(f"You selected:{country}")
#Multiselect method
skills=st.multiselect(
    "Select skills",
    ["Python","SQL","ML","Streamlit"]
)
st.write("Skills:",skills)
#Slider method
age=st.slider("Select your age:",0,100,25)
st.write(f"You are {age} years old")
#Uploaading files
uploaded_file=st.file_uploader("Choose a file")
if uploaded_file is not None:
    st.success("File uploaded successfully!")
    st.write(f"Filename:{uploaded_file.name}")
st.divider()
#Form method to create a form
with st.form("my_form"):
    name=st.text_input("Name")
    age=st.number_input("Age",0,120,25)
    submit=st.form_submit_button("Submit")
if submit:
    st.write(name,age)
st.divider()
#form submit button
with st.form("Login"):
    user=st.text_input("user")
    password=st.text_input("password",type="password")
    login=st.form_submit_button("login")
if login:
    st.success("Login successful")
st.divider()
#columns method
col1,col2,col3=st.columns(3)
with col1:
    st.header("Column 1")
    st.write("This is column 1") 
with col2:
    st.header("Column 2")
    st.write("This is column 2")
with col3:
    st.header("Column 3")
    st.write("This is column 3") 
st.divider()
#container method
container = st.container()
container.write("This is inside the container")

if container.button("Click me", key="container_btn"):
    container.success("Container button clicked!")


#table method 
data = {
    'Name': ['Anurag', 'Sumit', 'Rohit'],
    'Age': [21, 22, 20],
    'Course': ['B.Tech', 'M.Tech', 'BBA']
}
st.table(data)
#sidebar method
st.sidebar.title("Menu")
option = st.sidebar.selectbox(
"Choose page",
["Home", "About", "Contact"]
)
st.sidebar.write(f"You selected: {option}")
@st.cache_data
def load_data():
    return [1,2,3,4]
data=load_data()
st.write(data)
