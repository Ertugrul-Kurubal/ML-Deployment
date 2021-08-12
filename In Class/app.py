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
st.succes("Successfull")
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