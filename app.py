import streamlit as st

st.set_page_config(page_title="Diccionario Cálculo 3", layout="wide")

st.title("📘 Diccionario de Cálculo 3 (Tarea)")
st.write("Selecciona un término para ver su concepto.")

# ==================================================
# DICCIONARIO: TERMINO + CONCEPTO
# (solo temas de la tarea)
# ==================================================

CONCEPTOS = [
    # -------- HOMOGENEIDAD --------
    {
        "name": "Función homogénea",
        "definition": (
            "Una función f(x, y) es homogénea de grado k si, para todo λ > 0, se cumple\n"
            "f(λx, λy) = λ^k f(x, y).\n\n"
            "Es decir, al escalar las variables por un factor λ, el valor de la función "
            "se escala por λ^k. El número k se llama grado de homogeneidad."
        )
    },
    {
        "name": "Grado de homogeneidad de una función",
        "definition": (
            "Es el número real k tal que f(λx, λy) = λ^k f(x, y) para todo λ > 0.\n"
            "Si no existe tal k, la función no es homogénea."
        )
    },
    {
        "name": "Homogeneidad positiva",
        "definition": (
            "Propiedad de una función homogénea en la que la condición\n"
            "f(λx, λy) = λ^k f(x, y) se exige solo para λ > 0.\n"
            "Es la versión más común en aplicaciones de Cálculo y Economía."
        )
    },
    {
        "name": "Homogeneidad local",
        "definition": (
            "La función solo cumple la relación de homogeneidad en una región del dominio, "
            "por ejemplo cerca del origen o en un subconjunto específico, no en todo ℝ²."
        )
    },
    {
        "name": "Homogeneidad global",
        "definition": (
            "La función cumple f(λx, λy) = λ^k f(x, y) para todo λ > 0 y para todos los "
            "puntos del dominio. Es la forma más fuerte de homogeneidad."
        )
    },
    {
        "name": "Dominio natural de una función homogénea",
        "definition": (
            "Es el conjunto de puntos donde la función está bien definida y tiene sentido "
            "verificar la homogeneidad. Por ejemplo, si aparece una raíz o un logaritmo, "
            "puede ser necesario restringir x, y o λ."
        )
    },
    {
        "name": "Función definida por partes",
        "definition": (
            "Función cuyo dominio se divide en varias regiones y en cada región se da una "
            "expresión distinta. Para estudiar homogeneidad o continuidad se debe analizar "
            "cada pieza y cómo se unen en las fronteras."
        )
    },
    {
        "name": "Contraejemplo de homogeneidad",
        "definition": (
            "Es una función para la cual NO existe un grado k que satisfaga la relación "
            "f(λx, λy) = λ^k f(x, y). Se usa para mostrar que una función no es homogénea."
        )
    },

    # -------- DERIVADAS PARCIALES --------
    {
        "name": "Derivada parcial de una función respecto a una variable",
        "definition": (
            "Es la derivada de f respecto a una variable (por ejemplo x), "
            "manteniendo las demás constantes.\n"
            "Mide cómo cambia la función cuando se mueve solo en esa dirección."
        )
    },
    {
        "name": "Derivadas parciales de primer orden",
        "definition": (
            "Son las derivadas parciales f_x, f_y, f_z, etc. Se obtienen derivando una vez "
            "respecto a cada variable independiente."
        )
    },

    # -------- DERIVADAS DE ORDEN SUPERIOR --------
    {
        "name": "Derivadas parciales de segundo orden",
        "definition": (
            "Se obtienen derivando de nuevo una derivada parcial.\n"
            "Incluyen f_xx, f_yy y las derivadas mixtas f_xy, f_yx."
        )
    },
    {
        "name": "Derivadas parciales mixtas",
        "definition": (
            "Derivadas en las que se derivan dos veces, pero respecto a variables distintas, "
            "por ejemplo f_xy y f_yx."
        )
    },
    {
        "name": "Derivadas parciales iteradas",
        "definition": (
            "Nombre general para las derivadas de orden superior obtenidas aplicando el "
            "operador de derivada parcial varias veces (f_xx, f_xyy, f_yxx, etc.)."
        )
    },

    # -------- TEOREMAS --------
    {
        "name": "Teorema de Clairaut sobre derivadas mixtas",
        "definition": (
            "Si f tiene derivadas parciales de segundo orden continuas en una vecindad, "
            "entonces las derivadas mixtas coinciden: f_xy = f_yx.\n"
            "Esto implica que la Hessiana es simétrica."
        )
    },
    {
        "name": "Teorema de Schwarz",
        "definition": (
            "Nombre alternativo del teorema de Clairaut que asegura la igualdad de las "
            "derivadas parciales mixtas bajo hipótesis de continuidad."
        )
    },

    # -------- DIFERENCIABILIDAD --------
    {
        "name": "Diferenciabilidad de funciones de varias variables",
        "definition": (
            "f es diferenciable en un punto si puede aproximarse localmente por una función "
            "lineal (su plano tangente).\n"
            "Esto es más fuerte que solo tener derivadas parciales en el punto."
        )
    },
    {
        "name": "Incremento total de una función",
        "definition": (
            "Es el cambio f(x+h) − f(x) cuando la variable pasa de x a x+h.\n"
            "En funciones diferenciables se descompone como parte lineal + un error pequeño."
        )
    },
    {
        "name": "Aproximación lineal de una función",
        "definition": (
            "Es la aproximación de f cerca de un punto usando su plano tangente:\n"
            "f(x,y) ≈ f(a,b) + f_x(a,b)(x−a) + f_y(a,b)(y−b).\n"
            "Se usa para estimar valores y analizar errores."
        )
    },

    # -------- GRADIENTE / DERIVADAS DIRECCIONALES --------
    {
        "name": "Vector gradiente",
        "definition": (
            "Es el vector formado por todas las derivadas parciales de primer orden:\n"
            "∇f = (f_x, f_y, ...).\n"
            "Se interpreta como la dirección de máximo crecimiento de la función."
        )
    },
    {
        "name": "Interpretación geométrica del gradiente",
        "definition": (
            "El gradiente es perpendicular (normal) a las curvas o superficies de nivel de f "
            "y señala hacia donde f aumenta más rápido."
        )
    },
    {
        "name": "Gradiente como vector normal a curvas de nivel",
        "definition": (
            "En dos variables, en un punto (x,y) de la curva de nivel f(x,y)=c, el vector ∇f(x,y) "
            "es perpendicular a la curva. En tres variables es normal a la superficie de nivel."
        )
    },
    {
        "name": "Dirección de máximo crecimiento",
        "definition": (
            "Es la dirección del gradiente. Entre todas las direcciones posibles, la derivada "
            "direccional es máxima cuando el vector dirección coincide con ∇f."
        )
    },
    {
        "name": "Derivada direccional de una función",
        "definition": (
            "Mide la tasa de cambio de f en una dirección dada u. Se define como el límite del "
            "cociente incremental cuando se avanza desde el punto en la dirección del vector u."
        )
    },
    {
        "name": "Derivada direccional en la dirección de un vector unitario",
        "definition": (
            "Es la derivada direccional cuando el vector dirección u tiene norma 1. En ese caso:\n"
            "D_u f = ∇f · u."
        )
    },
    {
        "name": "Relación entre gradiente y derivada direccional",
        "definition": (
            "La derivada direccional en la dirección del vector unitario u es el producto punto "
            "∇f · u. Esto muestra que el gradiente contiene toda la información sobre las "
            "tendencias de cambio de f en cualquier dirección."
        )
    },

    # -------- PLANO TANGENTE --------
    {
        "name": "Plano tangente a una superficie",
        "definition": (
            "Para z=f(x,y), el plano tangente en (a,b) es el plano que mejor aproxima la "
            "superficie cerca de ese punto y que la toca sin cortarla localmente."
        )
    },
    {
        "name": "Ecuación del plano tangente",
        "definition": (
            "Se escribe como:\n"
            "z = f(a,b) + f_x(a,b)(x−a) + f_y(a,b)(y−b).\n"
            "Es la versión explícita de la aproximación lineal."
        )
    },
    {
        "name": "Interpretación geométrica del plano tangente",
        "definition": (
            "El plano tangente es la generalización de la recta tangente de Cálculo 1: "
            "localmente, la superficie se ve casi igual a ese plano."
        )
    },

    # -------- OPTIMIZACIÓN --------
    {
        "name": "Punto crítico de una función",
        "definition": (
            "Punto del dominio donde el gradiente se anula (∇f = 0) o no existe. "
            "Los máximos, mínimos y puntos de silla solo pueden ocurrir en puntos críticos "
            "o en la frontera del dominio."
        )
    },
    {
        "name": "Punto singular",
        "definition": (
            "Punto crítico donde alguna derivada parcial no existe o la función no es suave. "
            "Requiere un análisis especial para clasificar el comportamiento de f."
        )
    },
    {
        "name": "Extremos locales de una función",
        "definition": (
            "Máximos o mínimos locales: valores de f que son mayores o menores que los de "
            "puntos cercanos, dentro de una vecindad del dominio."
        )
    },
    {
        "name": "Máximo local",
        "definition": (
            "Punto donde f(x0) es mayor o igual que los valores de f en puntos cercanos. "
            "En ese punto la función alcanza un pico local."
        )
    },
    {
        "name": "Mínimo local",
        "definition": (
            "Punto donde f(x0) es menor o igual que los valores de f en una vecindad. "
            "En ese punto la función presenta un valle local."
        )
    },
    {
        "name": "Punto de silla",
        "definition": (
            "Punto crítico que no es máximo ni mínimo local. La función tiene direcciones "
            "en las que crece y direcciones en las que decrece (por ejemplo, f(x,y)=x^2−y^2 en (0,0))."
        )
    },

    # -------- HESSIANA / SEGUNDA DERIVADA --------
    {
        "name": "Matriz Hessiana de una función",
        "definition": (
            "Es la matriz cuadrada formada por todas las derivadas parciales de segundo orden "
            "de una función. En dos variables:\n"
            "Hf = [[f_xx, f_xy], [f_yx, f_yy]]."
        )
    },
    {
        "name": "Simetría de la matriz Hessiana",
        "definition": (
            "Cuando se cumple el teorema de Clairaut (f_xy = f_yx), la Hessiana es simétrica. "
            "Esto permite usar herramientas de álgebra lineal para clasificar puntos críticos."
        )
    },
    {
        "name": "Evaluación de la Hessiana en puntos críticos",
        "definition": (
            "Consiste en sustituir las coordenadas del punto crítico en la matriz Hessiana "
            "para estudiar la forma cuadrática asociada y determinar el tipo de extremo."
        )
    },
    {
        "name": "Criterio de la segunda derivada para funciones de dos variables",
        "definition": (
            "Usa la Hessiana en un punto crítico para clasificarlo:\n"
            "• si el determinante de H es > 0 y f_xx > 0 → mínimo local;\n"
            "• si el determinante de H es > 0 y f_xx < 0 → máximo local;\n"
            "• si el determinante de H es < 0 → punto de silla."
        )
    },
    {
        "name": "Determinantes principales de la Hessiana",
        "definition": (
            "Son los determinantes de las submatrices principales de la Hessiana. "
            "En dos variables solo se usa el determinante de la matriz completa, "
            "en más variables se consideran varios para aplicar criterios de positividad."
        )
    },
    {
        "name": "Clasificación de puntos críticos mediante la Hessiana",
        "definition": (
            "Procedimiento que, usando la Hessiana, permite decidir si un punto crítico "
            "es máximo, mínimo o punto de silla, según el signo de la forma cuadrática asociada."
        )
    },

    # -------- RESTRICCIONES / LAGRANGE --------
    {
        "name": "Optimización de funciones con restricciones",
        "definition": (
            "Problemas en los que se busca el máximo o mínimo de una función f(x,y,...) "
            "sujeta a una o varias ecuaciones g(x,y,...) = c que limitan el dominio."
        )
    },
    {
        "name": "Restricción explícita",
        "definition": (
            "Restricción en la que se puede despejar una variable en función de las otras "
            "y sustituir en la función, reduciendo el problema a menos variables."
        )
    },
    {
        "name": "Restricción implícita",
        "definition": (
            "Restricción dada por una relación g(x,y,...) = 0 donde no es fácil despejar. "
            "En estos casos se usa el método de los multiplicadores de Lagrange."
        )
    },
    {
        "name": "Método de los multiplicadores de Lagrange",
        "definition": (
            "Técnica para encontrar máximos y mínimos de f con restricciones g = 0. "
            "Se introduce un parámetro λ y se resuelve el sistema ∇f = λ∇g junto con g = 0."
        )
    },
    {
        "name": "Función objetivo",
        "definition": (
            "Es la función f(x,y,...) cuyo valor se desea maximizar o minimizar "
            "en el problema de optimización."
        )
    },
    {
        "name": "Función de restricción",
        "definition": (
            "Es la función g(x,y,...) = 0 que impone la condición que deben cumplir "
            "las soluciones aceptables del problema."
        )
    },
    {
        "name": "Sistema de ecuaciones de Lagrange",
        "definition": (
            "Conjunto formado por las ecuaciones ∇f = λ∇g (y, si hay más restricciones, "
            "un λ por cada una) más las ecuaciones de restricción. Sus soluciones son "
            "los candidatos a extremos con restricción."
        )
    },

    # -------- INTERPRETACIÓN GEOMÉTRICA --------
    {
        "name": "Curvas de nivel",
        "definition": (
            "Conjunto de puntos (x,y) donde f(x,y) = c para una constante c. "
            "Son las 'curvas de igual valor' de la función, análogas a curvas de altura "
            "en un mapa topográfico."
        )
    },
    {
        "name": "Superficies de nivel",
        "definition": (
            "En tres variables, son los conjuntos f(x,y,z) = c. Representan capas de igual "
            "valor de la función, como superficies de igual temperatura o densidad."
        )
    },
    {
        "name": "Interpretación geométrica del método de Lagrange",
        "definition": (
            "En el punto óptimo con restricción, las curvas (o superficies) de nivel de f "
            "son tangentes a la curva (o superficie) de restricción. Eso equivale a que los "
            "gradientes ∇f y ∇g sean paralelos."
        )
    }
]

# ==================================================
# INTERFAZ: SELECTBOX TIPO DICCIONARIO
# ==================================================

nombres = [c["name"] for c in CONCEPTOS]
seleccion = st.selectbox("Selecciona un término", nombres)

concepto = next(c for c in CONCEPTOS if c["name"] == seleccion)

st.markdown("### Concepto")
st.write(concepto["definition"])
