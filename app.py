import streamlit as st

st.set_page_config(
    page_title="Diccionario de Cálculo 3",
    layout="wide"
)

st.title("📘 Diccionario de Cálculo 3")
st.subheader("Contenido interactivo")

# ==================================================
# CONCEPTOS (FORMATO DICCIONARIO)
# ==================================================

conceptos = [

    # Funciones homogéneas
    "Función homogénea",
    "Grado de homogeneidad de una función",
    "Homogeneidad positiva",
    "Homogeneidad local",
    "Homogeneidad global",
    "Dominio natural de una función homogénea",
    "Funciones definidas por partes",
    "Criterio de homogeneidad",
    "Funciones no homogéneas",
    "Contraejemplos de homogeneidad",

    # Derivadas parciales
    "Derivada parcial de una función respecto a una variable",
    "Derivadas parciales de primer orden",
    "Interpretación geométrica de la derivada parcial",

    # Derivadas parciales de orden superior
    "Derivadas parciales de segundo orden",
    "Derivadas parciales mixtas",
    "Derivadas parciales iteradas",

    # Teoremas fundamentales
    "Teorema de Clairaut sobre derivadas mixtas",
    "Teorema de Schwarz",

    # Diferenciabilidad
    "Diferenciabilidad de funciones de varias variables",
    "Incremento total de una función",
    "Aproximación lineal de una función",

    # Gradiente
    "Vector gradiente",
    "Interpretación geométrica del gradiente",
    "Gradiente como vector normal a curvas de nivel",
    "Dirección de máximo crecimiento",

    # Derivadas direccionales
    "Derivada direccional de una función",
    "Derivada direccional en la dirección de un vector unitario",
    "Relación entre gradiente y derivada direccional",

    # Plano tangente
    "Plano tangente a una superficie",
    "Ecuación del plano tangente",
    "Interpretación geométrica del plano tangente",

    # Optimización
    "Punto crítico de una función",
    "Punto singular",
    "Extremos locales de una función",
    "Máximo local",
    "Mínimo local",
    "Punto de silla",

    # Matriz Hessiana
    "Matriz Hessiana de una función",
    "Simetría de la matriz Hessiana",
    "Evaluación de la Hessiana en puntos críticos",

    # Criterio de la segunda derivada
    "Criterio de la segunda derivada para funciones de dos variables",
    "Determinantes principales de la Hessiana",
    "Clasificación de puntos críticos mediante la Hessiana",

    # Optimización con restricciones
    "Optimización de funciones con restricciones",
    "Restricción explícita",
    "Restricción implícita",

    # Multiplicadores de Lagrange
    "Método de los multiplicadores de Lagrange",
    "Función objetivo",
    "Función de restricción",
    "Sistema de ecuaciones de Lagrange",

    # Interpretación geométrica
    "Curvas de nivel",
    "Superficies de nivel",
    "Interpretación geométrica del método de Lagrange"
]

# ==================================================
# BUSCADOR TIPO DICCIONARIO
# ==================================================

busqueda = st.text_input("Buscar concepto")

if busqueda:
    conceptos_filtrados = [
        c for c in conceptos if busqueda.lower() in c.lower()
    ]
else:
    conceptos_filtrados = conceptos

if conceptos_filtrados:
    st.selectbox(
        "Selecciona un concepto",
        conceptos_filtrados
    )
else:
    st.warning("No se encontraron conceptos.")
