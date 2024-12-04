import streamlit as st
import numpy as np
import pandas as pd
notas=[]
ponderaciones=[]
seguir = False
st.title("Bienvenido a tu sufrimiento")
seguir_nota = True
seguir_ponderacion = True
comprobar = 0
seguir_nota_aprueba=False
seguir_nota_max=False
seguir_nota_min=False
seguir_porcentaje=False
seguir_puntaje_max=False
def cambiar_color(nota):
    if nota!='':
        if float(nota) < 4:
            return f'<span style="color: red">{nota}</span>'
        else:
            return f'<span style="color: blue">{nota}</span>'
    else:
        return ''

if st.checkbox("Calculo de notas"):
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
                seguir = True
            else:
                if seguir_nota== False:
                    st.subheader("Las notas deben ser valores positivos")
                if seguir_ponderacion == False:
                    st.subheader("Las ponderaciones deben ser valores positivos y deben de sumar 100%")

    except ValueError:
        st.write("complete los datos")

if st.checkbox("Escala de notas"):
    #try:
        puntajes= []
        nota_max = st.text_input("Nota maxima?")
        nota_min = st.text_input("Nota minima?")
        nota_aprueba=st.text_input("Nota con la que apruebas?")
        porcentaje = st.text_input("Exigencia")
        puntaje_maximo = st.text_input("Puntaje maximo?")
        if porcentaje != '':
            porcentaje = float(porcentaje)/100
            if porcentaje>0:
                seguir_porcentaje=True
            else:
                st.error("los datos deben ser positivos") 
        if nota_max != '':
            nota_max = float(nota_max)
            if nota_max>=0:
                seguir_nota_max=True
            else:
                st.error("los datos deben ser positivos y con '.' ")
        if nota_min != '':
            nota_min = float(nota_min)
            if nota_min>=0:
                seguir_nota_min=True
            else:
                st.error("los datos deben ser positivos y con '.' ")
        if nota_aprueba != '':
            nota_aprueba = float(nota_aprueba)
            if nota_aprueba>0:
                seguir_nota_aprueba=True
            else:
                st.error("los datos deben ser positivos y con '.' ")
        if puntaje_maximo!='':
            if float(puntaje_maximo)>0:
                seguir_puntaje_max=True
            else:
                st.error("los datos deben ser positivos ")
        if seguir_nota_aprueba and seguir_nota_max and seguir_nota_min and seguir_porcentaje and seguir_puntaje_max:
            seguir = True
        if seguir == True:
            for i in range(0,int(puntaje_maximo)+1):
            
                if float(i) < float(puntaje_maximo)*porcentaje:
                    nota=((nota_aprueba-nota_min)*(i/(float(puntaje_maximo)*porcentaje)))+nota_min
                    print(nota)
                    puntajes.append(nota)
                else:
                    print("hola")
                    nota=((nota_max-nota_aprueba)*((i-(porcentaje*float(puntaje_maximo)))/(float(puntaje_maximo)*(1-porcentaje))))+nota_aprueba
                    puntajes.append(nota)
            print("___________")
            print(nota_aprueba-nota_min)
            print(nota_aprueba)
            print(nota_min)
            print(nota_max)
            print(puntaje_maximo)
            print(porcentaje)
            notas_1=[]
            puntaje_1=[]
            notas_2=[]
            puntaje_2=[]
            notas_3=[]
            puntajes_3=[]
            notas_4=[]
            puntajes_4=[]
            notas_df=pd.DataFrame()
            for i in range(0, len(puntajes)):
                if i<len(puntajes)/4:
                    puntaje_1.append(str(i))
                    notas_1.append(str(np.round(puntajes[i],decimals=1)))
                elif i<(len(puntajes)/2):
                    puntaje_2.append(str(i))
                    notas_2.append(str((np.round(puntajes[i],decimals=1))))
                elif i<((len(puntajes)/4)*3) : 
                    puntajes_3.append(str(i))
                    notas_3.append(str((np.round(puntajes[i],decimals=1))))
                else:
                    puntajes_4.append(str(i))
                    notas_4.append(str((np.round(puntajes[i],decimals=1))))
                if i==len(puntajes)-1:
                        if len(notas_2)==len(notas_1)-1:
                            puntaje_2.append('')
                            notas_2.append('')
                        if len(notas_3)==len(notas_1)-1:
                            puntajes_3.append('')
                            notas_3.append('')
                        if len(notas_4)==len(notas_1)-1:
                            puntajes_4.append('')
                            notas_4.append('')
            notas_df["Puntaje"] = puntaje_1
            notas_df["Notas"] = notas_1
            notas_df['Notas'] = notas_df['Notas'].apply(cambiar_color)
            notas_df['']=''
            notas_df["Puntaje "] = puntaje_2
            notas_df["Notas "] = notas_2
            notas_df['Notas '] = notas_df['Notas '].apply(cambiar_color)
            notas_df[' ']=''
            notas_df["Puntaje  "] = puntajes_3
            notas_df["Notas  "] = notas_3
            notas_df['Notas  '] = notas_df['Notas  '].apply(cambiar_color)
            notas_df['  ']=''
            notas_df["Puntaje   "] = puntajes_4
            notas_df["Notas   "] = notas_4
            notas_df['Notas   '] = notas_df['Notas   '].apply(cambiar_color)
            st.write(notas_df.to_html(index=False,escape=False),unsafe_allow_html=True)
    #except Exception:
        #st.warning("Complete los datos")