# =========================================================
# PARTE 1 — INTRODUCCIÓN, VECTORES Y GEOMETRÍA DEL ESPACIO
# =========================================================

import streamlit as st

# ---------------------------------------------------------
# CONFIGURACIÓN GENERAL
# ---------------------------------------------------------
st.set_page_config(
    page_title="Diccionario de Cálculo 3",
    layout="wide"
)

st.title("📘 Diccionario de Cálculo 3")
st.subheader("PARTE 1 — Introducción, Vectores y Geometría del Espacio")

st.markdown("""
### ¿Qué estudia Cálculo 3?

Cálculo 3 es la continuación natural del cálculo diferencial e integral
de una variable, pero ahora los objetos matemáticos **viven en el espacio**
y **dependen de varias variables**.

Mientras que en Cálculo 1 trabajamos funciones del tipo  
f(x),  
y en Cálculo 2 se profundiza en técnicas de integración y series,  
en **Cálculo 3** estudiamos:

- objetos geométricos en ℝ² y ℝ³,
- curvas y superficies,
- funciones f(x,y) y f(x,y,z),
- campos vectoriales,
- integrales sobre regiones y superficies,
- optimización en varias variables,
- y teoremas fundamentales que conectan derivadas e integrales.

El enfoque cambia: **ya no basta calcular**, ahora hay que **entender la geometría**.
""")

st.markdown("""
---

### ¿Por qué son importantes los vectores?

Los vectores son el lenguaje natural de Cálculo 3.

Con ellos se describen:
- posiciones,
- desplazamientos,
- velocidades,
- aceleraciones,
- fuerzas,
- normales a superficies,
- campos físicos (gravedad, electricidad, fluidos).

Sin vectores no existirían:
- derivadas direccionales,
- gradiente,
- integrales de línea,
- integrales de superficie,
- ni los teoremas de Green, Gauss y Stokes.
""")

# =========================================================
# BASE DE DATOS — PARTE 1
# =========================================================

TERMS = [

{
    "name": "Vector",
    "definition": (
        "Un vector es un objeto matemático que posee **magnitud, dirección y sentido**.\n\n"
        "En ℝ² o ℝ³, un vector puede interpretarse de varias maneras:\n"
        "• como un desplazamiento de un punto a otro,\n"
        "• como una fuerza aplicada,\n"
        "• como una velocidad o aceleración,\n"
        "• o como una flecha dibujada en el espacio.\n\n"
        "Formalmente, un vector se representa como una n-tupla ordenada de números reales.\n\n"
        "En Cálculo 3, los vectores no solo se estudian algebraicamente, sino que "
        "se interpretan constantemente de forma geométrica."
    ),
    "formula": r"\vec v = \langle v_1, v_2, v_3 \rangle",
    "example": (
        "El vector ⟨2, −1, 3⟩ puede verse como el desplazamiento"
        " desde el origen hasta el punto (2, −1, 3)."
    )
},

{
    "name": "Magnitud (norma) de un vector",
    "definition": (
        "La magnitud o norma de un vector representa su longitud.\n\n"
        "Geométricamente, es la distancia desde el origen hasta el punto "
        "determinado por el vector.\n\n"
        "Se calcula usando una generalización del Teorema de Pitágoras.\n\n"
        "La norma es fundamental para:\n"
        "• definir vectores unitarios,\n"
        "• medir velocidades y fuerzas,\n"
        "• normalizar direcciones,\n"
        "• calcular derivados direccionales."
    ),
    "formula": r"\|\vec v\| = \sqrt{v_1^2 + v_2^2 + v_3^2}",
    "example": (
        "Si v = ⟨3,4,0⟩ entonces \n"
        "||v|| = √(3² + 4² + 0²) = 5."
    )
},

{
    "name": "Vector unitario",
    "definition": (
        "Un vector unitario es un vector de magnitud uno.\n\n"
        "Su principal función es **indicar dirección sin alterar magnitud**.\n\n"
        "Para obtener el vector unitario asociado a un vector no nulo, "
        "se divide el vector entre su norma.\n\n"
        "Los vectores unitarios son esenciales en:\n"
        "• derivadas direccionales,\n"
        "• descomposición de fuerzas,\n"
        "• sistemas de coordenadas."
    ),
    "formula": r"\hat u = \frac{\vec v}{\|\vec v\|}",
    "example": (
        "Si v = ⟨3,4,0⟩, el vector unitario asociado es ⟨3/5,4/5,0⟩."
    )
},

{
    "name": "Producto punto",
    "definition": (
        "El producto punto (o producto escalar) de dos vectores produce un número real.\n\n"
        "Mide qué tan alineados están dos vectores:\n"
        "• si es positivo, apuntan aproximadamente en la misma dirección,\n"
        "• si es cero, son perpendiculares,\n"
        "• si es negativo, apuntan en direcciones opuestas.\n\n"
        "Tiene interpretación geométrica directa en términos del ángulo entre vectores "
        "y es fundamental en proyecciones y derivadas direccionales."
    ),
    "formula": r"\vec a \cdot \vec b = \|\vec a\|\,\|\vec b\|\cos\theta",
    "example": (
        "Si a·b = 0, entonces cosθ = 0 y los vectores son ortogonales."
    )
},

{
    "name": "Proyección de un vector",
    "definition": (
        "La proyección de un vector sobre otro mide la componente del primero "
        "en la dirección del segundo.\n\n"
        "Es ampliamente usada en física y en descomposición de fuerzas."
    ),
    "formula": r"\text{proj}_{\vec b} \vec a = \frac{\vec a \cdot \vec b}{\|\vec b\|^2}\vec b",
    "example": (
        "Permite expresar vectores como suma de componentes paralelas y perpendiculares."
    )
},

{
    "name": "Producto cruz",
    "definition": (
        "El producto cruz de dos vectores en ℝ³ produce un vector perpendicular a ambos.\n\n"
        "Su magnitud representa el área del paralelogramo que forman los vectores.\n\n"
        "El sentido del vector se determina mediante la regla de la mano derecha.\n\n"
        "Es fundamental para:\n"
        "• encontrar normales a planos,\n"
        "• calcular torque,\n"
        "• integrar sobre superficies."
    ),
    "formula": r"\vec a \times \vec b",
    "example": (
        "Si a y b son paralelos, a × b = 0."
    )
},

{
    "name": "Recta en el espacio",
    "definition": (
        "Una recta en ℝ³ se describe mediante un punto inicial y un vector director.\n\n"
        "El parámetro t indica cuánto se avanza en la dirección del vector.\n\n"
        "Esta representación es clave para modelar movimiento uniforme y trayectorias."
    ),
    "formula": r"\vec r(t) = \vec r_0 + t\vec v",
    "example": (
        "Cuando t aumenta, el punto se desplaza linealmente a lo largo de la recta."
    )
},

{
    "name": "Plano",
    "definition": (
        "Un plano es una superficie plana infinita en ℝ³.\n\n"
        "Puede describirse usando:\n"
        "• un punto y un vector normal,\n"
        "• o mediante una ecuación cartesiana.\n\n"
        "Los planos aparecen constantemente como planos tangentes a superficies."
    ),
    "formula": r"ax + by + cz = d",
    "example": (
        "El vector ⟨a,b,c⟩ es normal al plano."
    )
}

]

# =========================================================
# INTERFAZ
# =========================================================

st.markdown("---")
st.markdown("### 📚 Contenido interactivo")

nombres = [t["name"] for t in TERMS]
seleccion = st.selectbox("Selecciona un concepto", nombres)

concepto = next(t for t in TERMS if t["name"] == seleccion)

st.subheader(concepto["name"])
st.write(concepto["definition"])
st.latex(concepto["formula"])
st.info(concepto["example"])

st.caption("Diccionario de Cálculo 3 — Parte 1 (versión ultra desarrollada)")
