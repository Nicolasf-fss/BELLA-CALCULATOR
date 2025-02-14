# Importación de librerías necesarias
import streamlit as st  # Para crear la interfaz web
import numpy as np  # Para operaciones matemáticas y manejo de matrices
import sympy as sp  # Para cálculo simbólico (derivadas)
import time  # Para simular tiempos de carga
from scipy import stats  # Para cálculos estadísticos (moda)

############## FUNCIONES PARA CALCULO ###########################################

# Función para evaluar una expresión matemática
def calcular_expresion(expresion):
    try:
        return eval(expresion)  # Evalúa la expresión y retorna el resultado
    except:
        return "Error"  # Retorna "Error" si la expresión no es válida

# Función para calcular la media de una lista de números
def calcular_media(datos):
    return np.mean(datos)  # Usa numpy para calcular la media

# Función para calcular la mediana de una lista de números
def calcular_mediana(datos):
    return np.median(datos)  # Usa numpy para calcular la mediana

# Función para calcular la moda de una lista de números
def calcular_moda(datos):
    moda_result = stats.mode(datos, keepdims=True)  # Usa scipy.stats para calcular la moda
    return moda_result.mode[0]  # Retorna el valor de la moda

# Función para calcular el rango de una lista de números
def calcular_rango(datos):
    return np.max(datos) - np.min(datos)  # Calcula la diferencia entre el máximo y el mínimo

# Función para calcular la varianza de una lista de números
def calcular_varianza(datos): 
    return np.var(datos)  # Usa numpy para calcular la varianza

# Función para calcular la desviación estándar de una lista de números
def calcular_desviacion_estandar(datos): 
    return np.std(datos)  # Usa numpy para calcular la desviación estándar

# Función para calcular la derivada de una expresión simbólica
def derivar_expresion(expresion):
    try:
        x = sp.Symbol('x')  # Define la variable simbólica 'x'
        derivada = sp.diff(expresion, x)  # Calcula la derivada de la expresión respecto a 'x'
        return str(derivada)  # Retorna la derivada como una cadena de texto
    except:
        return "Error"  # Retorna "Error" si la expresión no es válida

# Función para realizar operaciones matriciales (suma, resta, multiplicación)
def operar_matrices(a, b, operacion):
    try:
        if operacion == "Suma":
            return np.add(a, b)  # Suma las matrices
        elif operacion == "Resta":
            return np.subtract(a, b)  # Resta las matrices
        elif operacion == "Multiplicación":
            return np.dot(a, b)  # Multiplica las matrices
    except:
        return "Error en operación"  # Retorna "Error en operación" si algo falla

# Función para crear una matriz a partir de entradas del usuario
def input_matriz(nombre):
    filas = st.number_input(f"Filas de {nombre}", min_value=1, max_value=5, value=2, step=1)  # Define el número de filas
    columnas = st.number_input(f"Columnas de {nombre}", min_value=1, max_value=5, value=2, step=1)  # Define el número de columnas
    matriz = np.zeros((filas, columnas))  # Crea una matriz de ceros con las dimensiones especificadas
    for i in range(filas):
        cols = st.columns(columnas)  # Crea columnas en la interfaz para ingresar los valores
        for j in range(columnas):
            matriz[i, j] = cols[j].number_input(f"{nombre}[{i+1},{j+1}]", value=0, step=1, key=f"{nombre}_{i}_{j}")  # Ingresa los valores en la matriz
    return matriz  # Retorna la matriz creada

############## LOGICA DE LA PAGINA ###########################################

# Función principal de la aplicación
def main():
    st.set_page_config(page_title="BELLA - Calculadora", layout="centered", page_icon="🐈")  # Configura la página de Streamlit
    st.title("Calculadora - BELLA")  # Título de la aplicación
    
    tabs = st.tabs(["Calculo", "Tendencia central", "Calculos de dispersion", "Derivadas", "Operaciones Matriciales"])  # Crea pestañas en la interfaz

    # Pestaña de cálculos simples
    with tabs[0]:
        st.subheader("Calculos Simples")  # Subtítulo de la pestaña
        expresion = st.text_input("Ingrese una operacion matematica simple (2*3/4)")  # Entrada de texto para la expresión
        if st.button("Calcular"):  # Botón para calcular
            resultado = calcular_expresion(expresion)  # Calcula la expresión
            progress_text = "Cargando operacion"  # Texto para la barra de progreso
            my_bar = st.progress(0, text=progress_text)  # Crea una barra de progreso
            for percent_complete in range(100):
                time.sleep(0.01)  # Simula un tiempo de carga
                my_bar.progress(percent_complete + 1, text=progress_text)  # Actualiza la barra de progreso
            time.sleep(0.5)  # Espera adicional
            my_bar.empty()  # Limpia la barra de progreso
            st.write(f"Resultado: {resultado}")  # Muestra el resultado

    # Pestaña de tendencia central
    with tabs[1]:
        st.subheader("Tendencia central")  # Subtítulo de la pestaña
        opcion = st.selectbox("Elige una medida de tendencia central:", ["Media", "Mediana", "Moda"])  # Selector de opciones
        
        datos = st.text_input("Ingrese los datos separados por comas (ejemplo: 1, 2, 3, 4, 5)")  # Entrada de datos
        if st.button("Calcular tendencia"):  # Botón para calcular
            try:
                numeros = datos.split(",") # Convierte los datos a una lista de números
                lista_numeros = []
                for numero in numeros:
                    lista_numeros.append(float(numero)) 

                if opcion == "Media":
                    resultado = calcular_media(lista_numeros)  # Calcula la media
                elif opcion == "Mediana":
                    resultado = calcular_mediana(lista_numeros)  # Calcula la mediana
                elif opcion == "Moda":
                    resultado = calcular_moda(lista_numeros)  # Calcula la moda
                
                progress_text = "Cargando operacion"  # Texto para la barra de progreso
                my_bar = st.progress(0, text=progress_text)  # Crea una barra de progreso
                for percent_complete in range(100):
                    time.sleep(0.01)  # Simula un tiempo de carga
                    my_bar.progress(percent_complete + 1, text=progress_text)  # Actualiza la barra de progreso
                time.sleep(1)  # Espera adicional
                my_bar.empty()  # Limpia la barra de progreso
                st.write(f"Resultado de la {opcion}: {resultado}")  # Muestra el resultado
            except:
                st.error("Error: Asegúrate de ingresar datos válidos separados por comas.")  # Mensaje de error

    # Pestaña de cálculos de dispersión
    with tabs[2]:
        st.subheader("Cálculos de dispersión")  # Subtítulo de la pestaña
        opcion_dispersion = st.selectbox("Elige una medida de dispersión:", ["Rango", "Varianza", "Desviación estándar"])  # Selector de opciones
        datos_dispersion = st.text_input("Ingrese los datos separados por comas (ejemplo: 1, 2, 3, 4, 5)", key="dispersion_input")  # Entrada de datos
        
        if st.button("Calcular dispersión"):  # Botón para calcular
            try:
                numeros_dis = datos_dispersion.split(",") # Convierte los datos a una lista de números
                lista_numeros_dis = []
                for numero in numeros_dis:
                    lista_numeros_dis.append(float(numero))  # Convierte los datos a una lista de números
                if opcion_dispersion == "Rango":
                    resultado = calcular_rango(lista_numeros_dis)  # Calcula el rango
                elif opcion_dispersion == "Varianza":
                    resultado = calcular_varianza(lista_numeros_dis)  # Calcula la varianza
                elif opcion_dispersion == "Desviación estándar":
                    resultado = calcular_desviacion_estandar(lista_numeros_dis)  # Calcula la desviación estándar
                
                progress_text = "Cargando operación"  # Texto para la barra de progreso
                my_bar = st.progress(0, text=progress_text)  # Crea una barra de progreso
                for percent_complete in range(100):
                    time.sleep(0.01)  # Simula un tiempo de carga
                    my_bar.progress(percent_complete + 1, text=progress_text)  # Actualiza la barra de progreso
                time.sleep(1)  # Espera adicional
                my_bar.empty()  # Limpia la barra de progreso
                st.write(f"Resultado de {opcion_dispersion}: {resultado}")  # Muestra el resultado
            except:
                st.error("Error: Asegúrate de ingresar datos válidos separados por comas.")  # Mensaje de error
    
    # Pestaña de cálculo de derivadas
    with tabs[3]:
        st.subheader("Cálculo de Derivadas")  # Subtítulo de la pestaña
        expresion_derivada = st.text_input("Ingrese la función a derivar (en términos de x)")  # Entrada de texto para la función
        if st.button("Calcular Derivada"):  # Botón para calcular
            resultado = derivar_expresion(expresion_derivada)  # Calcula la derivada
            progress_text = "Cargando operacion"  # Texto para la barra de progreso
            my_bar = st.progress(0, text=progress_text)  # Crea una barra de progreso
            for percent_complete in range(100):
                time.sleep(0.01)  # Simula un tiempo de carga
                my_bar.progress(percent_complete + 1, text=progress_text)  # Actualiza la barra de progreso
            time.sleep(1)  # Espera adicional
            my_bar.empty()  # Limpia la barra de progreso
            st.write(f"Resultado: {resultado}")  # Muestra el resultado   

    # Pestaña de operaciones matriciales


# Punto de entrada de la aplicación
if __name__ == "__main__":
    main()  # Ejecuta la función principal
