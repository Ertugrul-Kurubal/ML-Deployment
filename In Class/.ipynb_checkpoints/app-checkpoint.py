import streamlit as st

# text/file
st.title("Streamlit Tutorial")
st.text("Hello streamlit")

# header/subheader
st.header("This is a header")
st.subheader("This is a subheader")

# markdown
st.markdown("This is a markdown")
st.markdown("**This is a markdown**")

# colorful text
st.success("Successfull")
st.info("This is Information")

# help
st.warning("This is a warning")
st.error("Stop. That give an error")

# get help
st.help(range)

# writing text
st.write("Writing example text with write function")

# importing images
from PIL import Image
img = Image.open("Machine Learning.jpg")
st.image(img, width=200, caption="my_image")

# my_video=open(,rb)
# st.video(my_video)
st.video("https://www.youtube.com/watch?v=TUVcZfQe-Kw")

# checkbox
st.checkbox("Hide an Seek")

if st.checkbox("Hide / Seek"):
    st.text("You checked i show")

# radio button
status = st.radio("Select your status", ("Graduate","Student"))

if status == "Graduate":
    st.success("Congrats")
else:
    st.info("Keep working")
    
# selectbox
path = st.selectbox("Your path is", ["DS","FS","AWS"])
st.write("your path is", path)

# multiselect
team = st.multiselect("Select your profession",["ENGINEER", "TEACHER","NURSE","IT ENGINEER"])
st.write("Your profession are", team)

# slider
count = st.slider("How many years of ecperience in IT",1,10)
count = st.slider("How many years of ecperience in IT",1,10,2,2) # 2 den başlayıp 2 şer gidecek

# button
st.button('Press this button')

if st.button("About Program"):
    st.text("Streamlit is easy and fun")
else:
    st.text("Nothing to say")