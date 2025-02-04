import streamlit as st
import numpy as np
import sympy as sp
import time
from scipy import stats  

def calcular_expresion(expresion):
    try:
        return eval(expresion)
    except:
        return "Error"

def calcular_media(datos):
    return np.mean(datos)

def calcular_mediana(datos):
    return np.median(datos)

def calcular_moda(datos):
    moda_result = stats.mode(datos, keepdims=True)  
    return moda_result.mode[0]  

def calcular_rango(datos):
    return np.max(datos) - np.min(datos)

def calcular_varianza(datos, poblacional=False):
    ddof = 0 if poblacional else 1
    return np.var(datos, ddof=ddof)

def calcular_desviacion_estandar(datos, poblacional=False):
    ddof = 0 if poblacional else 1
    return np.std(datos, ddof=ddof)

def derivar_expresion(expresion):
    try:
        x = sp.Symbol('x')
        derivada = sp.diff(expresion, x)
        return str(derivada)
    except:
        return "Error"

def operar_matrices(a, b, operacion):
    try:
        if operacion == "Suma":
            return np.add(a, b)
        elif operacion == "Resta":
            return np.subtract(a, b)
        elif operacion == "Multiplicación":
            return np.dot(a, b)
    except:
        return "Error en operación"

def input_matriz(nombre):
    filas = st.number_input(f"Filas de {nombre}", min_value=1, max_value=5, value=2, step=1)
    columnas = st.number_input(f"Columnas de {nombre}", min_value=1, max_value=5, value=2, step=1)
    matriz = np.zeros((filas, columnas))
    for i in range(filas):
        cols = st.columns(columnas)
        for j in range(columnas):
            matriz[i, j] = cols[j].number_input(f"{nombre}[{i+1},{j+1}]", value=0, step=1, key=f"{nombre}_{i}_{j}")
    return matriz

def main():
    st.set_page_config(page_title="BELLA - Calculadora", layout="centered")
    st.title("Calculadora BELLA")
    
    tabs = st.tabs(["Calculo", "Tendencia central", "Calculos de dispersion", "Derivadas", "Operaciones Matriciales"])

    with tabs[0]:
        st.subheader("Calculos Simples")
        expresion_derivada = st.text_input("Ingrese una operacion matematica simple (2*3/4)")
        if st.button("Calcular"):
            resultado = calcular_expresion(expresion_derivada)
            progress_text = "Cargando operacion"
            my_bar = st.progress(0, text=progress_text)
            for percent_complete in range(100):
                time.sleep(0.01)
                my_bar.progress(percent_complete + 1, text=progress_text)
            time.sleep(0.5)
            my_bar.empty()
            st.write(f"Resultado: {resultado}")

    with tabs[1]:
        st.subheader("Tendencia central")
        opcion = st.selectbox("Elige una medida de tendencia central:", ["Media", "Mediana", "Moda"])
        
        datos = st.text_input("Ingrese los datos separados por comas (ejemplo: 1, 2, 3, 4, 5)")
        if st.button("Calcular tendencia"):
            try:
                datos = [float(x) for x in datos.split(",")] 
                if opcion == "Media":
                    resultado = calcular_media(datos)
                elif opcion == "Mediana":
                    resultado = calcular_mediana(datos)
                elif opcion == "Moda":
                    resultado = calcular_moda(datos)
                
                progress_text = "Cargando operacion"
                my_bar = st.progress(0, text=progress_text)
                for percent_complete in range(100):
                    time.sleep(0.01)
                    my_bar.progress(percent_complete + 1, text=progress_text)
                time.sleep(1)
                my_bar.empty()
                st.write(f"Resultado de la {opcion}: {resultado}")
            except:
                st.error("Error: Asegúrate de ingresar datos válidos separados por comas.")

    with tabs[2]:
        st.subheader("Cálculos de dispersión")
        opcion_dispersion = st.selectbox("Elige una medida de dispersión:", ["Rango", "Varianza", "Desviación estándar"])
        datos_dispersion = st.text_input("Ingrese los datos separados por comas (ejemplo: 1, 2, 3, 4, 5)", key="dispersion_input")
        
        if st.button("Calcular dispersión"):
            try:
                datos_dispersion = [float(x) for x in datos_dispersion.split(",")]
                if opcion_dispersion == "Rango":
                    resultado = calcular_rango(datos_dispersion)
                elif opcion_dispersion == "Varianza":
                    resultado = calcular_varianza(datos_dispersion)
                elif opcion_dispersion == "Desviación estándar":
                    resultado = calcular_desviacion_estandar(datos_dispersion)
                
                progress_text = "Cargando operación"
                my_bar = st.progress(0, text=progress_text)
                for percent_complete in range(100):
                    time.sleep(0.01)
                    my_bar.progress(percent_complete + 1, text=progress_text)
                time.sleep(1)
                my_bar.empty()
                st.write(f"Resultado de {opcion_dispersion}: {resultado}")
            except:
                st.error("Error: Asegúrate de ingresar datos válidos separados por comas.")
    
    with tabs[3]:
        st.subheader("Cálculo de Derivadas")
        expresion_derivada = st.text_input("Ingrese la función a derivar (en términos de x)")
        if st.button("Calcular Derivada"):
            resultado = derivar_expresion(expresion_derivada)
            progress_text = "Cargando operacion"
            my_bar = st.progress(0, text=progress_text)
            for percent_complete in range(100):
                time.sleep(0.01)
                my_bar.progress(percent_complete + 1, text=progress_text)
            time.sleep(1)
            my_bar.empty()
            st.write(f"Resultado: {resultado}")   

    with tabs[4]:
        st.subheader("Operaciones Matriciales")
        st.write("Ingrese las matrices en la cuadrícula")
        matriz_a = input_matriz("Matriz A")
        st.write("Matriz A:")
        st.dataframe(matriz_a)
        
        matriz_b = input_matriz("Matriz B")
        st.write("Matriz B:")
        st.dataframe(matriz_b)
        
        operacion = st.selectbox("Seleccione la operación", ["Suma", "Resta", "Multiplicación"])
        if st.button("Calcular Matriz"):
            resultado = operar_matrices(matriz_a, matriz_b, operacion)
            progress_text = "Cargando operacion"
            my_bar = st.progress(0, text=progress_text)
            for percent_complete in range(100):
                time.sleep(0.01)
                my_bar.progress(percent_complete + 1, text=progress_text)
            time.sleep(1)
            my_bar.empty()
            st.write("Resultado:")
            st.dataframe(resultado)

if __name__ == "__main__":
    main()