"""
import time

st.success("Todo correcto")
mensaje_error=st.error("Algo no ha ido bién")
time.sleep(3)
mensaje_error.empty()
st.toast("mensaje¡ ¡flotanteeeee",duration="long")
"""
##Solicitud de datos

import streamlit as st
nombre=st.text_input("Introduce tu nombre")
edad=st.number_input("Introduce tu edad", value=0)
afiliado=st.checkbox("Afiliado")
curso=st.radio("Elige un curso: ",["Python","C++","Java"])
centro=st.selectbox("Elige centro: ",["Leganés","Getafe","Alcobendas","San Blas"]) 
if st.button("Pulsar"):
    st.success(f"te llamas {nombre}, tienes {edad} años, has elegido el curso {curso} en el centro {centro}")
    
    aula = [
        {},
        {},
        {}
    ]
    st.table(aula)