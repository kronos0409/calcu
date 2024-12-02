import streamlit as st
import numpy as np
notas=[]
ponderaciones=[]

st.title("Bienvenido a tu sufrimiento")
seguir_nota = True
seguir_ponderacion = True
comprobar = 0
cant_notas = st.number_input("Cuantas notas tienes?", min_value=1, max_value=10)
eximicion = st.text_input("Con que nota te eximes?")
c1,c2,c3 = st.columns(3)
try:
    for i in range(0, cant_notas):
        if i < (cant_notas/2):
            with c1:
                nota = st.text_input(f"Introduce tu nota {i+1}", key=f"{i}")
                ponderacion = st.text_input(f"Introduce el porcentaje de tu nota {i+1}", key=f"{-i-1}")
        else:
            with c2:
                nota = st.text_input(f"Introduce tu nota {i+1}", key=f"{i}")
                ponderacion = st.text_input(f"Introduce el porcentaje de tu nota {i+1}", key=f"{-i-1}")
        notas.append(float(nota))
        ponderaciones.append(float(ponderacion)/100)
        promedio = 0
        for i in range(0,len(notas)):
            promedio+=notas[i]*ponderaciones[i]
    with c1: 
        ponderacion = st.text_input("Introduce el porcentaje de tu nota que necesitas", key="B")
        for i in range(0, len(notas)):
            if float(notas[i])<=0:
                seguir_nota = False
            if float(ponderaciones[i])<=0 or float(ponderacion)<=0:
                seguir_ponderacion = False
            comprobar +=float(ponderaciones[i])
        print(np.round(comprobar,decimals=3))
        if np.round(comprobar,decimals=3) + (float(ponderacion)/100) != 1:
            seguir_ponderacion= False 
    with c3:
        if seguir_nota and seguir_ponderacion:
            nota_necesaria = float((-promedio+float(eximicion)))/(float(ponderacion)/100)
            if nota_necesaria<0:
                st.write("ya pasaste")
            if float(nota_necesaria)>=6.0:
                st.image("8634ecb456af4ded64541504fb9a67c7.jpg")
                st.write(f"KGASTE, necesitas un {np.round(nota_necesaria,decimals=1)}")
                st.write(f"Con un {np.round(nota_necesaria,decimals=1)} al {ponderacion}% te sumaria {np.round(nota_necesaria*(float(ponderacion)/100),decimals=2)}")
            elif float(nota_necesaria)>=2.0:
                st.image("30100440.jpg")
                st.write(f"Tu puedess, necesitas un {np.round(nota_necesaria,decimals=1)}")
                st.write(f"Con un {np.round(nota_necesaria,decimals=1)} al {ponderacion}% te sumaria {np.round(nota_necesaria*(float(ponderacion)/100),decimals=2)}")
            else:
                st.image("1522304.jpg")
                st.write(f"necesitas un {np.round(nota_necesaria,decimals=1)}")
                st.write(f"Con un {np.round(nota_necesaria,decimals=1)} al {ponderacion}% te sumaria {np.round(nota_necesaria*(float(ponderacion)/100),decimals=2)}")
            st.write(f"Tu promedio actual es:    {np.round(promedio,decimals=2)}")
        else:
            if seguir_nota== False:
                st.subheader("Las notas deben ser valores positivos")
            if seguir_ponderacion == False:
                st.subheader("Las ponderaciones deben ser valores positivos y deben de sumar 100%")
    
except ValueError:
    st.write("complete los datos")
