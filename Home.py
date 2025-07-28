import streamlit as st

st.set_page_config(page_title="Home",
                   layout='wide',
                   page_icon='D:\pop\copy\JPGs\1_datapreparation\webapp\images\home.png')


st.title("Hardware Tool Kit List")
st.caption('Hardware Tools')
st.page_link("pages/1_yolo_for_image.py", label="👉 Click here for add image")


st.markdown("""

Below give are the objects the our model will detect
   
             1. Hammers
   
             2. Spanners
            
""")

