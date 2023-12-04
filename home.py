import streamlit as st

st.set_page_config(
    page_title="Portfolio | faisal",
    page_icon="👨‍🎓",
    layout="wide"
)

st.title("SELAMAT DATANG DI PORTFOLIO SAYA 👨‍🎓")

st.sidebar.success("SILAHKAN PILIH MENU DI ATAS")

import streamlit as st

col1, col2 = st.columns(2)

with col1:
   st.header("About Me")
   st.image("me.JPG", width= 290)

with col2:
   st.header("My Biodata")
   st.subheader("NAMA : MUHAMMAD FAISAL")
   st.caption("NIM : 0402201087")
   st.write(
            """
            - Tempat Tanggal Lahir : Brebes 16 April 2002 
            - Alamat               : Kecipir Losari Brebes
            - Hobi                 : Torik Torik
            - Cita-cita            : Jadi Orang Manfaat
            - Hal yang disukai     : TIDUR
            - Status               : Sudah Di Miliki
            """
        )
   st.subheader("My socil media")
with st.container():
    col1, col2, col3 , col4 , = st.columns(4)
    with col1:
        st.write("Facebook")
        st. image("fb.png",width= 50)
        st.link_button("Facebook", "http://localhost:8501/contact")

        
    with col2:
            st.write("Instagram")
            st. image("ig.png",width= 50 )
            st.link_button("Blog", "http://localhost:8501/contact")


    with col3:
            st.write("Watthsap")
            st. image("ig.png",width= 50 )
            st.link_button("whattsap", "http://localhost:8501/contact")


    with col4:
            st.write("Bloog")
            st. image("ig.png",width= 50 )
            st.link_button("Go to contact", "http://localhost:8501/contact")
   

            
        



st.header("*Call Me If You Want*")
st.link_button("Go to contact", "http://localhost:8501/contact")


