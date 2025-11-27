import streamlit as st

# ==================================================
# CONFIGURACIÓN DE LA PÁGINA
# ==================================================

st.set_page_config(page_title="Diccionario Cálculo 3 Completo", layout="wide")

st.title("📘 Diccionario Completo de Cálculo Multivariable")
st.write("Selecciona un término en la barra lateral (sidebar) para ver su concepto.")

# ==================================================
# DICCIONARIO GLOBAL (Incluyendo tus datos y los añadidos)
# ==================================================

CONCEPTOS = [

    # ==================================================
    # 1. LÍMITES, CONTINUIDAD, DOMINIOS Y TOPOLOGÍA
    # ==================================================

    {
        "category": "1. Límites, Topología y Continuidad",
        "name": "Límite de una función de varias variables",
        "definition": (
            "El límite $\lim_{(x,y)→(a,b)} f(x,y)$ existe si el valor de la función se aproxima "
            "al mismo número $L$ al acercarse a $(a,b)$ por cualquier trayectoria del dominio."
        )
    },
    {
        "category": "1. Límites, Topología y Continuidad",
        "name": "Límite por trayectorias",
        "definition": (
            "Método para estudiar un límite evaluando $f(x,y)$ cuando $(x,y)$ se acerca al punto "
            "siguiendo distintas curvas o caminos. Si dos trayectorias dan valores distintos, "
            "el límite **NO** existe."
        )
    },
    {
        "category": "1. Límites, Topología y Continuidad",
        "name": "Límite por coordenadas polares",
        "definition": (
            "Técnica para analizar límites en $\mathbb{R}^2$ sustituyendo $x=r \cos\theta$, $y=r \sin\theta$. "
            "Si al tomar $r\\to 0$ el resultado depende de $\theta$, el límite no existe."
        )
    },
    {
        "category": "1. Límites, Topología y Continuidad",
        "name": "Continuidad en funciones de varias variables",
        "definition": (
            "Una función es continua en $(a,b)$ si el límite de $f(x,y)$ al acercarse a $(a,b)$ "
            "es igual al valor $f(a,b)$. Se requiere que el límite exista y coincida."
        )
    },
    {
        "category": "1. Límites, Topología y Continuidad",
        "name": "Discontinuidad removible",
        "definition": (
            "Ocurre cuando el límite existe pero $f$ no está definida o está mal definida en el punto. "
            "Puede corregirse redefiniendo la función."
        )
    },
    {
        "category": "1. Límites, Topología y Continuidad",
        "name": "Discontinuidad esencial (no removible)",
        "definition": (
            "Ocurre cuando el límite no existe o las trayectorias llevan a valores distintos. "
            "No puede resolverse con una simple redefinición."
        )
    },
    {
        "category": "1. Límites, Topología y Continuidad",
        "name": "Dominio de una función de varias variables",
        "definition": (
            "El conjunto de puntos donde la función está bien definida. Puede requerir restricciones "
            "por raíces pares, logaritmos, denominadores o condiciones geométricas."
        )
    },
    {
        "category": "1. Límites, Topología y Continuidad",
        "name": "Rango de una función de varias variables",
        "definition": (
            "Conjunto de valores posibles que puede tomar $f(x,y)$. En algunos problemas se estudia "
            "la imagen de curvas o superficies completas."
        )
    },
    {
        "category": "1. Límites, Topología y Continuidad",
        "name": "Vecindad de un punto",
        "definition": (
            "Un conjunto que contiene un punto $(a,b)$ y todos los puntos situados a una distancia "
            "menor que un radio dado. Representa un entorno local alrededor del punto."
        )
    },
    {
        "category": "1. Límites, Topología y Continuidad",
        "name": "Disco abierto en $\mathbb{R}^2$",
        "definition": (
            "Conjunto de puntos dentro de un círculo sin incluir la frontera: "
            "$D_r(a,b) = \{(x,y): \sqrt{(x-a)^2+(y-b)^2} < r\}$."
        )
    },
    {
        "category": "1. Límites, Topología y Continuidad",
        "name": "Disco cerrado en $\mathbb{R}^2$",
        "definition": (
            "Conjunto formado por los puntos dentro del disco y también los puntos de la circunferencia: "
            "$\overline{D}_r(a,b) = \{(x,y): \sqrt{(x-a)^2+(y-b)^2} \leq r\}$."
        )
    },
    {
        "category": "1. Límites, Topología y Continuidad",
        "name": "Conjunto abierto",
        "definition": (
            "Un conjunto es abierto si todo punto contiene una vecindad completamente incluida "
            "en el conjunto. No contiene puntos de frontera."
        )
    },
    {
        "category": "1. Límites, Topología y Continuidad",
        "name": "Conjunto cerrado",
        "definition": (
            "Un conjunto que contiene todos sus puntos frontera, o equivalente: su complemento es abierto. "
            "También puede definirse como aquel que contiene todos sus puntos límite."
        )
    },
    {
        "category": "1. Límites, Topología y Continuidad",
        "name": "Frontera de un conjunto",
        "definition": (
            "Conjunto de puntos donde cualquier vecindad intersecta tanto el conjunto como su complemento. "
            "Es el 'borde' del conjunto."
        )
    },
    {
        "category": "1. Límites, Topología y Continuidad",
        "name": "Interior de un conjunto",
        "definition": (
            "Todos los puntos del conjunto que tienen una vecindad completamente contenida en él. "
            "Representa la parte estrictamente dentro del conjunto."
        )
    },
    {
        "category": "1. Límites, Topología y Continuidad",
        "name": "Clausura de un conjunto",
        "definition": (
            "Un conjunto más todos sus puntos límite. Equivale a la unión del conjunto con su frontera."
        )
    },
    {
        "category": "1. Límites, Topología y Continuidad",
        "name": "Conjunto acotado",
        "definition": (
            "Un conjunto es acotado si puede encerrarse dentro de una esfera o disco de radio finito. "
            "No se extiende indefinidamente."
        )
    },
    {
        "category": "1. Límites, Topología y Continuidad",
        "name": "Conjunto compacto",
        "definition": (
            "En $\mathbb{R}^2$ un conjunto es compacto si es cerrado y acotado. Este tipo de conjuntos garantizan "
            "propiedades importantes como la existencia de máximos y mínimos globales."
        )
    },
    {
        "category": "1. Límites, Topología y Continuidad",
        "name": "Conjunto conexo",
        "definition": (
            "Un conjunto es conexo si no puede dividirse en dos regiones separadas. "
            "Intuitivamente, todo punto está 'conectado' por un camino dentro del conjunto."
        )
    },
    {
        "category": "1. Límites, Topología y Continuidad",
        "name": "Región",
        "definition": (
            "Conjunto abierto, conexo y no vacío. Es el tipo de dominio que aparece con frecuencia "
            "en problemas de Cálculo Multivariable."
        )
    },
    {
        "category": "1. Límites, Topología y Continuidad",
        "name": "Región simple",
        "definition": (
            "Región que puede describirse mediante desigualdades simples (tipo $x$ entre $a$ y $b$, "
            "$y$ entre funciones en $x$). Son ideales para integrales dobles."
        )
    },
    {
        "category": "1. Límites, Topología y Continuidad",
        "name": "Región tipo I",
        "definition": (
            "Región donde $y$ está descrita entre dos funciones de $x$: "
            "$D = \{(x,y): a \leq x \leq b, g_1(x) \leq y \leq g_2(x)\}$."
        )
    },
    {
        "category": "1. Límites, Topología y Continuidad",
        "name": "Región tipo II",
        "definition": (
            "Región donde $x$ está entre dos funciones de $y$: "
            "$D = \{(x,y): c \leq y \leq d, h_1(y) \leq x \leq h_2(y)\}$."
        )
    },
    {
        "category": "1. Límites, Topología y Continuidad",
        "name": "Conjuntos de nivel",
        "definition": (
            "Para una función $f(x,y)$, el conjunto de nivel $f(x,y)=c$ es la curva donde la función "
            "toma el valor constante $c$."
        )
    },
    {
        "category": "1. Límites, Topología y Continuidad",
        "name": "Superficies de nivel",
        "definition": (
            "En $\mathbb{R}^3$, el conjunto de nivel $f(x,y,z)=c$ es una superficie donde todos los puntos cumplen "
            "el mismo valor de la función."
        )
    },
    {
        "category": "1. Límites, Topología y Continuidad",
        "name": "Función acotada",
        "definition": (
            "Una función es acotada si existe una constante $M$ tal que $|f(x,y)| \leq M$ para todos los "
            "puntos del dominio."
        )
    },
    {
        "category": "1. Límites, Topología y Continuidad",
        "name": "Función no acotada",
        "definition": (
            "Una función que puede hacerse arbitrariamente grande o pequeña (positiva o negativa) "
            "en alguna región del dominio."
        )
    },
    {
        "category": "1. Límites, Topología y Continuidad",
        "name": "Conjunto de puntos límite",
        "definition": (
            "Puntos donde cualquier vecindad contiene puntos del conjunto y puntos que no son del conjunto. "
            "Se relaciona con la clausura."
        )
    },
    {
        "category": "1. Límites, Topología y Continuidad",
        "name": "Conjunto denso",
        "definition": (
            "Un conjunto $A$ es denso en otro $B$ si cada punto de $B$ puede aproximarse tanto como se quiera "
            "con puntos de $A$."
        )
    },
    {
        "category": "1. Límites, Topología y Continuidad",
        "name": "Conjunto discreto",
        "definition": (
            "Conjunto cuyos puntos están separados entre sí: cada punto tiene una vecindad que "
            "no contiene otros puntos del conjunto."
        )
    },
    {
        "category": "1. Límites, Topología y Continuidad",
        "name": "Vecindad punctuada",
        "definition": (
            "Una vecindad que excluye el punto central $(a,b)$. Se usa en límites para evitar evaluar "
            "$f(a,b)$ directamente."
        )
    },
    {
        "category": "1. Límites, Topología y Continuidad",
        "name": "Convergencia de sucesiones en $\mathbb{R}^2$",
        "definition": (
            "Una sucesión $(x_n, y_n)$ converge a $(a,b)$ si $x_n \to a$ y $y_n \to b$. Esto permite definir límites "
            "de funciones mediante criterios de sucesiones."
        )
    },
    {
        "category": "1. Límites, Topología y Continuidad",
        "name": "Criterio de sucesiones para límites",
        "definition": (
            "Un límite $\lim f(x,y) = L$ existe si y solo si para toda sucesión $(x_n,y_n)$ que converge "
            "a $(a,b)$, los valores $f(x_n,y_n)$ convergen a $L$."
        )
    },
    {
        "category": "1. Límites, Topología y Continuidad",
        "name": "Conjunto cerrado bajo límite",
        "definition": (
            "Un conjunto es cerrado si contiene el límite de toda sucesión convergente de elementos del conjunto."
        )
    },


    # ==================================================
    # 2. DERIVADAS PARCIALES Y JACOBIANAS
    # ==================================================

    {
        "category": "2. Derivadas Parciales y Regla de la Cadena",
        "name": "Derivada parcial",
        "definition": (
            "La derivada parcial de $f$ respecto a $x$ ($f_x$) mide la tasa de cambio de $f$ cuando "
            "solo $x$ varía y el resto de variables permanecen constantes."
        )
    },
    {
        "category": "2. Derivadas Parciales y Regla de la Cadena",
        "name": "Derivadas parciales de primer orden",
        "definition": (
            "Son las derivadas $f_x, f_y, f_z$, etc. Se obtienen derivando $f$ una sola vez con respecto "
            "a cada variable independiente."
        )
    },
    {
        "category": "2. Derivadas Parciales y Regla de la Cadena",
        "name": "Derivadas parciales de segundo orden",
        "definition": (
            "Se obtienen derivando nuevamente las parciales de primer orden. Incluyen $f_{xx}, f_{yy}$, "
            "las mixtas $f_{xy}$ y $f_{yx}$."
        )
    },
    {
        "category": "2. Derivadas Parciales y Regla de la Cadena",
        "name": "Derivada parcial mixta",
        "definition": (
            "Derivada de segundo orden donde se derivan respecto a dos variables diferentes, por ejemplo $f_{xy}$."
        )
    },
    {
        "category": "2. Derivadas Parciales y Regla de la Cadena",
        "name": "Simetría de derivadas mixtas",
        "definition": (
            "Si las segundas derivadas parciales son continuas, entonces $f_{xy} = f_{yx}$. Este resultado "
            "es el **Teorema de Clairaut o de Schwarz**."
        )
    },
    {
        "category": "2. Derivadas Parciales y Regla de la Cadena",
        "name": "Derivadas parciales iteradas",
        "definition": (
            "Derivadas obtenidas aplicando varias veces operadores de derivación parcial, como $f_{xxy}$ o $f_{yyx}$."
        )
    },
    {
        "category": "2. Derivadas Parciales y Regla de la Cadena",
        "name": "Gradiente de una función",
        "definition": (
            "Vector formado por las derivadas parciales: $\nabla f = (f_x, f_y, f_z)$. Indica dirección y magnitud "
            "de mayor crecimiento de $f$."
        )
    },
    {
        "category": "2. Derivadas Parciales y Regla de la Cadena",
        "name": "Matriz Jacobiana",
        "definition": (
            "Matriz que contiene todas las derivadas parciales de una transformación vectorial $F(x,y)$. "
            "Es clave para cambios de variables y análisis de funciones vectoriales."
        )
    },
    {
        "category": "2. Derivadas Parciales y Regla de la Cadena",
        "name": "Determinante Jacobiano",
        "definition": (
            "El determinante de la matriz Jacobiana. Mide el factor de escala del cambio de variables. "
            "Es esencial en integrales múltiples."
        )
    },
    {
        "category": "2. Derivadas Parciales y Regla de la Cadena",
        "name": "Jacobiano positivo",
        "definition": (
            "Cuando el determinante del Jacobiano es $> 0$ indica que la transformación conserva orientación."
        )
    },
    {
        "category": "2. Derivadas Parciales y Regla de la Cadena",
        "name": "Jacobiano negativo",
        "definition": (
            "Si el determinante es $< 0$ la transformación invierte orientación."
        )
    },
    {
        "category": "2. Derivadas Parciales y Regla de la Cadena",
        "name": "Punto crítico de un mapeo",
        "definition": (
            "Punto donde el Jacobiano se anula o pierde rango. Suele indicar singularidades o "
            "problemas de inversión."
        )
    },
    {
        "category": "2. Derivadas Parciales y Regla de la Cadena",
        "name": "Regla de la cadena para funciones escalares",
        "definition": (
            "Si $z = f(x,y)$ y $x = x(t), y = y(t)$, entonces $dz/dt = f_x dx/dt + f_y dy/dt$."
        )
    },
    {
        "category": "2. Derivadas Parciales y Regla de la Cadena",
        "name": "Regla de la cadena para funciones compuestas",
        "definition": (
            "Generaliza la regla de la cadena: si $F = f(g(x,y), h(x,y))$, entonces $\nabla F$ se obtiene "
            "multiplicando las Jacobianas correspondientes."
        )
    },
    {
        "category": "2. Derivadas Parciales y Regla de la Cadena",
        "name": "Derivada total",
        "definition": (
            "Expresa el cambio total de $f$ cuando todas sus variables dependen de otra variable $t$: "
            "$df/dt = f_x dx/dt + f_y dy/dt + f_z dz/dt$."
        )
    },
    {
        "category": "2. Derivadas Parciales y Regla de la Cadena",
        "name": "Plano tangente mediante derivadas parciales",
        "definition": (
            "Para $z=f(x,y)$, el plano tangente en $(a,b)$ se obtiene usando $f_x(a,b)$ y $f_y(a,b)$."
        )
    },
    {
        "category": "2. Derivadas Parciales y Regla de la Cadena",
        "name": "Dirección de máximo crecimiento",
        "definition": (
            "Dirección dada por el gradiente $\nabla f$. La magnitud del crecimiento es $|\nabla f|$."
        )
    },
    {
        "category": "2. Derivadas Parciales y Regla de la Cadena",
        "name": "Derivada direccional",
        "definition": (
            "La tasa de cambio de $f$ en una dirección dada $\mathbf{u}$. Se calcula como $D_{\mathbf{u}} f = \nabla f \cdot \mathbf{u}$."
        )
    },
    {
        "category": "2. Derivadas Parciales y Regla de la Cadena",
        "name": "Superficie diferenciable",
        "definition": (
            "Una superficie $z=f(x,y)$ es diferenciable si su aproximación lineal existe y su error tiende "
            "a cero más rápido que la distancia al punto."
        )
    },
    {
        "category": "2. Derivadas Parciales y Regla de la Cadena",
        "name": "Jacobiano de una transformación",
        "definition": (
            "El Jacobiano representa el factor de escala que transforma áreas o volúmenes bajo cambios "
            "de coordenadas."
        )
    },
    {
        "category": "2. Derivadas Parciales y Regla de la Cadena",
        "name": "Transformación invertible",
        "definition": (
            "Una transformación $F(x,y)$ es invertible localmente si su Jacobiano es distinto de cero en el punto."
        )
    },
    {
        "category": "2. Derivadas Parciales y Regla de la Cadena",
        "name": "Regla de la cadena en notación matricial",
        "definition": (
            "Si $F$ depende de $G$ y $G$ depende de $x$, entonces $J_F = J_f \circ J_g$. Se multiplican Jacobianas "
            "como matrices."
        )
    },
    {
        "category": "2. Derivadas Parciales y Regla de la Cadena",
        "name": "Regla de la cadena para campos vectoriales",
        "definition": (
            "Generalización de la regla de la cadena donde aparecen Jacobianas de funciones vectoriales "
            "componiéndose entre sí."
        )
    },

    # ==================================================
    # 3. DIFERENCIABILIDAD, APROXIMACIÓN LINEAL, REGLA DE LA CADENA
    # ==================================================

    {
        "category": "3. Diferenciabilidad y Aproximación",
        "name": "Diferenciabilidad",
        "definition": (
            "Una función es diferenciable en un punto si puede aproximarse linealmente mediante su "
            "gradiente, y el error tiende más rápido a 0 que la distancia al punto."
        )
    },
    {
        "category": "3. Diferenciabilidad y Aproximación",
        "name": "Aproximación lineal",
        "definition": (
            "Aproximación de $f(x,y)$ por su plano tangente: $f(x,y) \approx f(a,b) + f_x(a,b)(x−a) + f_y(a,b)(y−b)$."
        )
    },
    {
        "category": "3. Diferenciabilidad y Aproximación",
        "name": "Error de aproximación lineal",
        "definition": (
            "Diferencia entre la función y su aproximación lineal. Para diferenciabilidad, debe "
            "disminuir más rápido que la distancia a $(a,b)$."
        )
    },
    {
        "category": "3. Diferenciabilidad y Aproximación",
        "name": "Plano tangente",
        "definition": (
            "Plano que mejor aproxima la superficie en un punto. Se construye con $f_x$ y $f_y$."
        )
    },
    {
        "category": "3. Diferenciabilidad y Aproximación",
        "name": "Mapa diferencial",
        "definition": (
            "La aplicación lineal que mejor aproxima la función en un punto. Es la generalización "
            "del plano tangente."
        )
    },
    {
        "category": "3. Diferenciabilidad y Aproximación",
        "name": "Linealización",
        "definition": (
            "Sinónimo de aproximación lineal, usando la derivada total o el gradiente."
        )
    },
    {
        "category": "3. Diferenciabilidad y Aproximación",
        "name": "Regla de la cadena (versión general)",
        "definition": (
            "Si $y=g(u,v)$ y $u=u(x,y)$, $v=v(x,y)$, entonces las derivadas se calculan mediante la "
            "multiplicación de las Jacobianas correspondientes."
        )
    },
    {
        "category": "3. Diferenciabilidad y Aproximación",
        "name": "Jacobiano de una función compuesta",
        "definition": (
            "Es el producto de las Jacobianas individuales: $J(f \circ g)=J(f)J(g)$."
        )
    },
    {
        "category": "3. Diferenciabilidad y Aproximación",
        "name": "Función diferenciable pero con parciales discontinuas",
        "definition": (
            "Existen funciones diferenciables cuyas derivadas parciales no son continuas. "
            "La diferenciabilidad es una condición más fuerte."
        )
    },
    {
        "category": "3. Diferenciabilidad y Aproximación",
        "name": "Diferenciabilidad fuerte",
        "definition": (
            "Supone continuidad de todas las derivadas parciales. Garantiza mejor suavidad "
            "y propiedades teóricas."
        )
    },
    {
        "category": "3. Diferenciabilidad y Aproximación",
        "name": "Condición suficiente de diferenciabilidad",
        "definition": (
            "Si todas las derivadas parciales de primer orden son continuas, entonces la función "
            "es diferenciable."
        )
    },
    {
        "category": "3. Diferenciabilidad y Aproximación",
        "name": "Diferencial total",
        "definition": (
            "Generalización del diferencial de Cálculo 1: $df = f_x dx + f_y dy + f_z dz$."
        )
    },
    {
        "category": "3. Diferenciabilidad y Aproximación",
        "name": "Interpretación geométrica de la diferenciabilidad",
        "definition": (
            "La función se comporta localmente como un plano (en $\mathbb{R}^3$) o una recta (en $\mathbb{R}^2$)."
        )
    },

    {
    "category": "3. Diferenciabilidad y Aproximación",
    "name": "Curva de nivel",
    "definition": (
        "Conjunto de puntos (x, y) donde una función f(x, y) toma un valor constante, "
        "es decir, f(x, y) = c. Es la representación en el plano de la altura constante "
        "de una superficie z = f(x, y)."
    )
},
{
    "category": "3. Diferenciabilidad y Aproximación",
    "name": "Mapa de contornos",
    "definition": (
        "Dibujo formado por muchas curvas de nivel que representan los valores de la "
        "función en diferentes alturas. Si las curvas están juntas, la función cambia "
        "rápido; si están separadas, cambia lento."
    )
},
{
    "category": "3. Diferenciabilidad y Aproximación",
    "name": "Superficie z = f(x,y)",
    "definition": (
        "Representación tridimensional de una función de dos variables. Cada punto (x, y) "
        "tiene una altura z. Las curvas de nivel son cortes horizontales de la superficie."
    )
},
{
    "category": "3. Diferenciabilidad y Aproximación",
    "name": "Intersección superficie–plano",
    "definition": (
        "El corte de la superficie z = f(x, y) con un plano horizontal z = k produce "
        "una curva de nivel. Geométricamente equivale a 'rebanar' la superficie."
    )
},
{
    "category": "3. Diferenciabilidad y Aproximación",
    "name": "Curvas de nivel cerradas",
    "definition": (
        "Curvas de nivel que forman un lazo completo alrededor de un punto. Indican zonas "
        "de máximo, mínimo o elevaciones tipo montaña o valle."
    )
},
{
    "category": "3. Diferenciabilidad y Aproximación",
    "name": "Curvas de nivel abiertas",
    "definition": (
        "Curvas que no se cierran y se extienden indefinidamente en el plano. "
        "Ocurren en funciones como planos inclinados."
    )
},
{
    "category": "3. Diferenciabilidad y Aproximación",
    "name": "Separación entre curvas de nivel",
    "definition": (
        "Indica cómo cambia la función: si están juntas, el cambio es rápido (alta pendiente). "
        "Si están separadas, la variación es lenta."
    )
},
{
    "category": "3. Diferenciabilidad y Aproximación",
    "name": "Curva de nivel vertical",
    "definition": (
        "Curva de nivel que se orienta casi verticalmente en el plano. Sugiere que la función "
        "varía más con el eje y que con el eje x."
    )
},


    # ==================================================
    # 4. GRADIENTE, DERIVADAS DIRECCIONALES, PLANO TANGENTE
    # ==================================================

    {
        "category": "4. Gradiente y Derivada Direccional",
        "name": "Gradiente de una función",
        "definition": (
            "El gradiente $\nabla f$ es el vector formado por las derivadas parciales de $f$. "
            "Indica la dirección de máximo crecimiento de la función."
        )
    },
    {
        "category": "4. Gradiente y Derivada Direccional",
        "name": "Magnitud del gradiente",
        "definition": (
            "La norma $|\nabla f|$ mide la pendiente máxima de la función en un punto."
        )
    },
    {
        "category": "4. Gradiente y Derivada Direccional",
        "name": "Interpretación geométrica del gradiente",
        "definition": (
            "El gradiente es perpendicular (normal) a las curvas o superficies de nivel. "
            "Apunta hacia donde $f$ aumenta más rápidamente."
        )
    },
    {
        "category": "4. Gradiente y Derivada Direccional",
        "name": "Derivada direccional",
        "definition": (
            "La tasa de cambio de $f$ en la dirección de un vector unitario $\mathbf{u}$. "
            "Se calcula como $D_{\mathbf{u}} f = \nabla f \cdot \mathbf{u}$."
        )
    },
    {
        "category": "4. Gradiente y Derivada Direccional",
        "name": "Derivada direccional máxima",
        "definition": (
            "La derivada direccional es máxima cuando la dirección $\mathbf{u}$ coincide con el gradiente."
        )
    },
    {
        "category": "4. Gradiente y Derivada Direccional",
        "name": "Dirección de aumento más rápido",
        "definition": (
            "La dirección del gradiente $\nabla f$, donde la función crece a la tasa máxima."
        )
    },
    {
        "category": "4. Gradiente y Derivada Direccional",
        "name": "Plano tangente a una superficie",
        "definition": (
            "Para $z=f(x,y)$, el plano tangente en $(a,b)$ se obtiene mediante: "
            "$z = f(a,b) + f_x(a,b)(x−a) + f_y(a,b)(y−b)$."
        )
    },
    {
        "category": "4. Gradiente y Derivada Direccional",
        "name": "Plano normal a una superficie",
        "definition": (
            "El plano cuya normal es el gradiente $\nabla f(a,b)$. Representa la orientación perpendicular "
            "al plano tangente."
        )
    },
    {
        "category": "4. Gradiente y Derivada Direccional",
        "name": "Recta normal",
        "definition": (
            "Línea que pasa por el punto y tiene como dirección el gradiente $\nabla f$."
        )
    },
    {
        "category": "4. Gradiente y Derivada Direccional",
        "name": "Curvas de nivel",
        "definition": (
            "Curvas donde $f(x,y)=c$. El gradiente es perpendicular en cada punto."
        )
    },
    {
        "category": "4. Gradiente y Derivada Direccional",
        "name": "Superficies de nivel",
        "definition": (
            "Superficies en $\mathbb{R}^3$ donde $f(x,y,z)=c$. El gradiente es normal a ellas."
        )
    },
    {
        "category": "4. Gradiente y Derivada Direccional",
        "name": "Relación entre gradiente y derivada direccional",
        "definition": (
            "La derivada direccional $D_{\mathbf{u}} f$ es el producto punto $\nabla f \cdot \mathbf{u}$. "
            "Esto muestra que $\nabla f$ contiene toda la información direccional."
        )
    },
    {
        "category": "4. Gradiente y Derivada Direccional",
        "name": "Curvatura de una curva de nivel",
        "definition": (
            "La curvatura indica cómo cambia la dirección del gradiente a lo largo de la curva."
        )
    },

    # ==================================================
    # 5. HESSIANA, SEGUNDA DERIVADA Y CLASIFICACIÓN DE PUNTOS
    # ==================================================

    {
        "category": "5. Extremos y Hessiana",
        "name": "Matriz Hessiana",
        "definition": (
            "Matriz cuadrada formada por las segundas derivadas de $f$. "
            "Para dos variables: $$H_f = \begin{bmatrix} f_{xx} & f_{xy} \\ f_{yx} & f_{yy} \end{bmatrix}$$"
        )
    },
    {
        "category": "5. Extremos y Hessiana",
        "name": "Simetría de la Hessiana",
        "definition": (
            "Si las segundas derivadas parciales son continuas, entonces $f_{xy} = f_{yx} $ "
            "y la Hessiana es simétrica."
        )
    },
    {
        "category": "5. Extremos y Hessiana",
        "name": "Forma cuadrática asociada a la Hessiana",
        "definition": (
            "Expresión $Q(h,k) = [h\ k] H_f [h\ k]^T$ que permite clasificar el tipo de punto crítico."
        )
    },
    {
        "category": "5. Extremos y Hessiana",
        "name": "Determinante de la Hessiana",
        "definition": (
            "$\text{D} = f_{xx} f_{yy} − (f_{xy})^2$. Sirve para clasificar puntos críticos mediante la segunda derivada."
        )
    },
    {
        "category": "5. Extremos y Hessiana",
        "name": "Criterio de la segunda derivada",
        "definition": (
            "Si $\text{D}>0$ y $f_{xx}>0$: **mínimo local**; "
            "si $\text{D}>0$ y $f_{xx}<0$: **máximo local**; "
            "si $\text{D}<0$: **punto de silla**; "
            "si $\text{D}=0$: prueba inconclusa."
        )
    },
    {
        "category": "5. Extremos y Hessiana",
        "name": "Punto crítico",
        "definition": (
            "Punto donde el gradiente se anula ($\nabla f=\mathbf{0}$) o no existe. "
            "Es un candidato a extremo o punto de silla."
        )
    },
    {
        "category": "5. Extremos y Hessiana",
        "name": "Punto de silla",
        "definition": (
            "Punto crítico donde la función aumenta en unas direcciones y disminuye en otras, "
            "como $f(x,y)=x^2−y^2$."
        )
    },
    {
        "category": "5. Extremos y Hessiana",
        "name": "Máximo local",
        "definition": (
            "Punto donde $f(x_0,y_0)$ es mayor que los valores en puntos cercanos. "
            "Requiere $\nabla f=\mathbf{0}$ y Hessiana negativa definida."
        )
    },
    {
        "category": "5. Extremos y Hessiana",
        "name": "Mínimo local",
        "definition": (
            "Punto donde $f(x_0,y_0)$ es menor que los valores de $f$ en puntos cercanos. "
            "Requiere Hessiana positiva definida."
        )
    },
    {
        "category": "5. Extremos y Hessiana",
        "name": "Hessiana positiva definida",
        "definition": (
            "Una matriz Hessiana $H$ es positiva definida si $\mathbf{h}^T H \mathbf{h} > 0$ para todo vector no nulo $\mathbf{h}$. "
            "Implica un **mínimo local**."
        )
    },
    {
        "category": "5. Extremos y Hessiana",
        "name": "Hessiana negativa definida",
        "definition": (
            "$H$ es negativa definida si $\mathbf{h}^T H \mathbf{h} < 0$ para todo vector no nulo $\mathbf{h}$. "
            "Indica un **máximo local**."
        )
    },
    {
        "category": "5. Extremos y Hessiana",
        "name": "Hessiana indefinida",
        "definition": (
            "Si la forma cuadrática toma valores positivos y negativos, indica un **punto de silla**."
        )
    },
    {
        "category": "5. Extremos y Hessiana",
        "name": "Autovalores de la Hessiana",
        "definition": (
            "Los autovalores determinan la curvatura en distintas direcciones. "
            "Todos positivos $\Rightarrow$ mínimo; todos negativos $\Rightarrow$ máximo; mezcla $\Rightarrow$ silla."
        )
    },
    {
        "category": "5. Extremos y Hessiana",
        "name": "Direcciones principales de curvatura",
        "definition": (
            "Direcciones asociadas a los autovectores de la Hessiana. "
            "Cada una describe la curvatura extrema de la superficie."
        )
    },
    {
        "category": "5. Extremos y Hessiana",
        "name": "Concavidad y convexidad",
        "definition": (
            "La convexidad se relaciona con Hessiana positiva semidefinida. "
            "La concavidad con Hessiana negativa semidefinida."
        )
    },
    {
        "category": "5. Extremos y Hessiana",
        "name": "Punto singular",
        "definition": (
            "Punto donde la Hessiana pierde rango o las derivadas no existen. "
            "Requiere un análisis especial."
        )
    },
    {
        "category": "5. Extremos y Hessiana",
        "name": "Clasificación de puntos críticos",
        "definition": (
            "Procedimiento que, usando la Hessiana, determina si un punto crítico es máximo, mínimo "
            "o silla."
        )
    },
    {
        "category": "5. Extremos y Hessiana",
        "name": "Extremos globales",
        "definition": (
            "Máximos o mínimos sobre todo el dominio. En conjuntos compactos siempre existen."
        )
    },
    {
        "category": "5. Extremos y Hessiana",
        "name": "Extremos en frontera",
        "definition": (
            "Para dominios con borde, los máximos/mínimos también pueden aparecer en la frontera. "
            "Debe verificarse con métodos especiales."
        )
    },

    # ==================================================
    # 6. CAMPOS VECTORIALES, DIVERGENCIA, ROTACIONAL
    # ==================================================

    {
        "category": "6. Campos Vectoriales y Operadores",
        "name": "Campo vectorial en $\mathbb{R}^2$",
        "definition": (
            "Es una función $\mathbf{F}(x,y)$ que asigna a cada punto un vector. "
            "Se representa como $\mathbf{F}(x,y) = (P(x,y), Q(x,y))$."
        )
    },
    {
        "category": "6. Campos Vectoriales y Operadores",
        "name": "Campo vectorial en $\mathbb{R}^3$",
        "definition": (
            "Es una función $\mathbf{F}(x,y,z) = (P, Q, R)$ que asigna un vector tridimensional a cada punto."
        )
    },
    {
        "category": "6. Campos Vectoriales y Operadores",
        "name": "Campo conservativo",
        "definition": (
            "Un campo $\mathbf{F}$ es conservativo si existe una función potencial $\phi$ tal que "
            "$\mathbf{F} = \nabla\phi$. La circulación alrededor de cualquier curva cerrada es cero."
        )
    },
    {
        "category": "6. Campos Vectoriales y Operadores",
        "name": "Función potencial",
        "definition": (
            "Función escalar $\phi$ tal que su gradiente $\nabla\phi$ es igual al campo vectorial. "
            "Permite calcular integrales de línea fácilmente."
        )
    },
    {
        "category": "6. Campos Vectoriales y Operadores",
        "name": "Condición de conservatividad en $\mathbb{R}^2$",
        "definition": (
            "Si $\mathbf{F}=(P,Q)$ y las derivadas son continuas, entonces $\mathbf{F}$ es conservativo si $\partial P/\partial y = \partial Q/\partial x$."
        )
    },
    {
        "category": "6. Campos Vectoriales y Operadores",
        "name": "Campo irrotacional",
        "definition": (
            "Un campo cuyo rotacional es cero ($\operatorname{curl}(\mathbf{F}) = \mathbf{0}$). En regiones simplemente conexas, ser irrotacional "
            "equivale a ser conservativo."
        )
    },
    {
        "category": "6. Campos Vectoriales y Operadores",
        "name": "Campo solenoidal",
        "definition": (
            "Un campo con divergencia cero: $\operatorname{div}(\mathbf{F})=0$. Se relaciona con flujos incompresibles."
        )
    },
    {
        "category": "6. Campos Vectoriales y Operadores",
        "name": "Divergencia de un campo",
        "definition": (
            "$$\operatorname{div}(\mathbf{F}) = \frac{\partial P}{\partial x} + \frac{\partial Q}{\partial y} + \frac{\partial R}{\partial z}$$ Mide la tasa neta de flujo que 'sale' de un punto."
        )
    },
    {
        "category": "6. Campos Vectoriales y Operadores",
        "name": "Rotacional de un campo",
        "definition": (
            "$\operatorname{curl}(\mathbf{F}) = \nabla \times \mathbf{F}$ mide la tendencia del campo a generar rotación o vorticidad."
        )
    },
    {
        "category": "6. Campos Vectoriales y Operadores",
        "name": "Rotacional en $\mathbb{R}^3$",
        "definition": (
            "$$\operatorname{curl}(\mathbf{F}) = \left(\frac{\partial R}{\partial y} - \frac{\partial Q}{\partial z}, \frac{\partial P}{\partial z} - \frac{\partial R}{\partial x}, \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}\right)$$ Indica cuánto gira el campo alrededor de un punto."
        )
    },
    {
        "category": "6. Campos Vectoriales y Operadores",
        "name": "Rotacional en $\mathbb{R}^2$",
        "definition": (
            "En 2D se considera $\operatorname{curl}(\mathbf{F}) = \partial Q/\partial x − \partial P/\partial y$ (es un escalar)."
        )
    },
    {
        "category": "6. Campos Vectoriales y Operadores",
        "name": "Región simplemente conexa",
        "definition": (
            "Región sin 'agujeros'. En estas regiones, cualquier campo irrotacional es conservativo."
        )
    },
    {
        "category": "6. Campos Vectoriales y Operadores",
        "name": "Región no simplemente conexa",
        "definition": (
            "Región con agujeros. En estas regiones puede haber campos irrotacionales que no sean conservativos."
        )
    },
    {
        "category": "6. Campos Vectoriales y Operadores",
        "name": "Flujo de un campo vectorial",
        "definition": (
            "El flujo mide cuánto del campo atraviesa una curva o superficie."
        )
    },
    {
        "category": "6. Campos Vectoriales y Operadores",
        "name": "Líneas de corriente",
        "definition": (
            "Curvas cuyas tangentes coinciden con el campo vectorial. "
            "Se interpretan como trayectorias de partículas en un flujo."
        )
    },
    {
        "category": "6. Campos Vectoriales y Operadores",
        "name": "Curvas parametrizadas en $\mathbb{R}^2$",
        "definition": (
            "Una curva se expresa como $\mathbf{r}(t)=(x(t),y(t))$, $a \leq t \leq b$. "
            "Permite describir trayectorias o bordes de regiones."
        )
    },
    {
        "category": "6. Campos Vectoriales y Operadores",
        "name": "Curvas parametrizadas en $\mathbb{R}^3$",
        "definition": (
            "Curva definida como $\mathbf{r}(t)=(x(t),y(t),z(t))$. Ideal para analizar movimiento en el espacio."
        )
    },
    {
        "category": "6. Campos Vectoriales y Operadores",
        "name": "Vector tangente a una curva",
        "definition": (
            "El vector $\mathbf{r}'(t)$ indica la dirección de la curva en el punto $\mathbf{r}(t)$."
        )
    },
    {
        "category": "6. Campos Vectoriales y Operadores",
        "name": "Campo gradiente",
        "definition": (
            "Campo de la forma $\mathbf{F} = \nabla f$. Todo campo conservativo tiene esta forma."
        )
    },
    {
        "category": "6. Campos Vectoriales y Operadores",
        "name": "Circulación de un campo",
        "definition": (
            "La integral de línea de $\mathbf{F}$ a lo largo de una curva. Mide el trabajo realizado por el campo."
        )
    },
    {
        "category": "6. Campos Vectoriales y Operadores",
        "name": "Circulación alrededor de una curva cerrada",
        "definition": (
            "Si $\mathbf{F}$ es conservativo, esta circulación es cero para cualquier curva cerrada."
        )
    },
    {
        "category": "6. Campos Vectoriales y Operadores",
        "name": "Teorema del campo gradiente",
        "definition": (
            "La integral de $\mathbf{F}=\nabla\phi$ entre dos puntos depende solo del valor de $\phi$ en los extremos."
        )
    },
    {
        "category": "6. Campos Vectoriales y Operadores",
        "name": "Campo estacionario",
        "definition": (
            "Un campo que no depende del tiempo. Se usa en modelos de flujo permanente."
        )
    },
    {
        "category": "6. Campos Vectoriales y Operadores",
        "name": "Magnitud de un campo vectorial",
        "definition": (
            "En $\mathbb{R}^3$, la magnitud es $|\mathbf{F}|=\sqrt{P^2+Q^2+R^2}$. Indica fuerza o intensidad del campo."
        )
    },
    {
        "category": "6. Campos Vectoriales y Operadores",
        "name": "Campo radial",
        "definition": (
            "Campo de la forma $\mathbf{F}(x,y,z)=k \cdot (x,y,z)$. Apunta hacia afuera o hacia el origen."
        )
    },
    {
        "category": "6. Campos Vectoriales y Operadores",
        "name": "Campo central",
        "definition": (
            "Campo que depende solo de la distancia al origen: $\mathbf{F} = f(r) \cdot (x,y,z)/r$."
        )
    },
    {
        "category": "6. Campos Vectoriales y Operadores",
        "name": "Campo de rotación pura",
        "definition": (
            "Campo con divergencia cero pero rotacional no nulo, como $(-y,x)$ en $\mathbb{R}^2$."
        )
    },
    {
        "category": "6. Campos Vectoriales y Operadores",
        "name": "Curva cerrada",
        "definition": (
            "Curva donde $\mathbf{r}(a)=\mathbf{r}(b)$. Se usa en teoremas de circulación como el de Green."
        )
    },

    # ==================================================
    # 7. INTEGRALES DOBLES Y TRIPLES
    # ==================================================

    {
        "category": "7. Integrales Múltiples",
        "name": "Integral doble",
        "definition": (
            "La integral $\iint_D f(x,y) dA$ calcula el volumen bajo la superficie $z=f(x,y)$ "
            "sobre una región $D$ del plano."
        )
    },
    {
        "category": "7. Integrales Múltiples",
        "name": "Interpretación geométrica de la integral doble",
        "definition": (
            "Representa la suma acumulada de infinitos rectángulos de área diferencial $dA$ "
            "multiplicados por la altura $f(x,y)$."
        )
    },
    {
        "category": "7. Integrales Múltiples",
        "name": "Región de integración tipo I",
        "definition": (
            "Región descrita por $a \leq x \leq b, g_1(x) \leq y \leq g_2(x)$. "
            "Se usa para integrar respecto a $y$ y luego $x$."
        )
    },
    {
        "category": "7. Integrales Múltiples",
        "name": "Región de integración tipo II",
        "definition": (
            "Región descrita por $c \leq y \leq d, h_1(y) \leq x \leq h_2(y)$. "
            "Se integra primero sobre $x$ y luego sobre $y$."
        )
    },
    {
        "category": "7. Integrales Múltiples",
        "name": "Integral iterada",
        "definition": (
            "Expresión donde se integra primero respecto a una variable y luego respecto a otra. "
            "Equivale a una integral doble en regiones rectangulares o simples."
        )
    },
    {
        "category": "7. Integrales Múltiples",
        "name": "Área diferencial $dA$",
        "definition": (
            "Elemento infinitesimal de área en el plano. En coordenadas rectangulares $dA = dx dy$."
        )
    },
    {
        "category": "7. Integrales Múltiples",
        "name": "Región acotada",
        "definition": (
            "Una región es acotada si cabe dentro de un disco de radio finito."
        )
    },
    {
        "category": "7. Integrales Múltiples",
        "name": "Integral triple",
        "definition": (
            "La integral $\iiint_E f(x,y,z) dV$ representa el volumen o la masa dentro de una región sólida $E$."
        )
    },
    {
        "category": "7. Integrales Múltiples",
        "name": "Volumen diferencial $dV$",
        "definition": (
            "Elemento infinitesimal de volumen en el espacio. En coordenadas rectangulares $dV = dx dy dz$."
        )
    },
    {
        "category": "7. Integrales Múltiples",
        "name": "Coordenadas polares",
        "definition": (
            "Sistema de coordenadas en $\mathbb{R}^2$ donde $(x,y)$ se sustituye por $(r, \theta)$, con $x = r \cos \theta$, $y = r \sin \theta$. Son útiles para regiones circulares."
        )
    },
    {
        "category": "7. Integrales Múltiples",
        "name": "Jacobiano de coordenadas polares",
        "definition": (
            "El factor de escala que transforma el área: $dA = r dr d\theta$. Este factor $r$ es crucial en las integrales dobles polares."
        )
    },
    {
        "category": "7. Integrales Múltiples",
        "name": "Coordenadas cilíndricas",
        "definition": (
            "Sistema de coordenadas en $\mathbb{R}^3$ que combina polares en el plano $xy$ con la coordenada $z$: $(r, \theta, z)$. Se utiliza para sólidos cilíndricos o cónicos."
        )
    },
    {
        "category": "7. Integrales Múltiples",
        "name": "Jacobiano de coordenadas cilíndricas",
        "definition": (
            "El factor de escala para el volumen: $dV = r dz dr d\theta$. Se aplica en integrales triples con simetría de rotación."
        )
    },
    {
        "category": "7. Integrales Múltiples",
        "name": "Coordenadas esféricas",
        "definition": (
            "Sistema de coordenadas en $\mathbb{R}^3$ definido por la distancia al origen $\rho$, el ángulo polar $\theta$ y el ángulo zenital $\phi$. Se usa para sólidos esféricos."
        )
    },
    {
        "category": "7. Integrales Múltiples",
        "name": "Jacobiano de coordenadas esféricas",
        "definition": (
            "El factor de escala para el volumen: $dV = \rho^2 \sin \phi d\rho d\phi d\theta$. Es clave en integrales triples para regiones esféricas."
        )
    },
    {
        "category": "7. Integrales Múltiples",
        "name": "Cambio de orden de integración",
        "definition": (
            "Reescribir una integral iterada (tipo $\int_a^b \int_{g_1(x)}^{g_2(x)} f(x,y) dy dx$) en el orden opuesto (tipo $dx dy$). Requiere redefinir los límites de la región de integración."
        )
    },
    {
        "category": "7. Integrales Múltiples",
        "name": "Integral doble como área",
        "definition": (
            "Si la función a integrar es $f(x,y) = 1$, la integral doble $\iint_D 1 dA$ calcula el área de la región $D$."
        )
    },
    {
        "category": "7. Integrales Múltiples",
        "name": "Integral triple como volumen",
        "definition": (
            "Si la función a integrar es $f(x,y,z) = 1$, la integral triple $\iiint_E 1 dV$ calcula el volumen del sólido $E$."
        )
    },
    {
        "category": "7. Integrales Múltiples",
        "name": "Aplicaciones de la integral doble/triple",
        "definition": (
            "Cálculo de masa, centro de masa, momentos de inercia y valor promedio de una función sobre una región."
        )
    },

    # ==================================================
    # 8. INTEGRALES DE LÍNEA Y SUPERFICIE (Añadidos)
    # ==================================================
    {
        "category": "8. Integrales de Línea y Superficie",
        "name": "Integral de línea de un campo escalar",
        "definition": (
            "Integral de una función $f(x,y,z)$ a lo largo de una curva $C$. Se usa para calcular la masa de un alambre con densidad variable."
        )
    },
    {
        "category": "8. Integrales de Línea y Superficie",
        "name": "Integral de línea de un campo vectorial (Trabajo)",
        "definition": (
            "Integral $\int_C \mathbf{F} \cdot d\mathbf{r}$. Mide el **trabajo** realizado por la fuerza $\mathbf{F}$ sobre una partícula que se mueve a lo largo de la curva $C$."
        )
    },
    {
        "category": "8. Integrales de Línea y Superficie",
        "name": "Longitud de arco diferencial $ds$",
        "definition": (
            "Elemento de longitud infinitesimal a lo largo de la curva. $ds = |\mathbf{r}'(t)| dt$. Se usa en la integral de línea de campos escalares."
        )
    },
    {
        "category": "8. Integrales de Línea y Superficie",
        "name": "Orientación de una curva",
        "definition": (
            "La dirección en la que se recorre una curva. Una curva cerrada se considera con orientación **positiva** si se recorre en sentido antihorario (contrario a las agujas del reloj)."
        )
    },
    {
        "category": "8. Integrales de Línea y Superficie",
        "name": "Superficie parametrizada",
        "definition": (
            "Una superficie $\mathbf{r}(u,v) = (x(u,v), y(u,v), z(u,v))$ definida por dos parámetros $u$ y $v$. Ejemplos: esfera, cilindro, plano."
        )
    },
    {
        "category": "8. Integrales de Línea y Superficie",
        "name": "Vector normal a la superficie",
        "definition": (
            "Vector $\mathbf{N} = \mathbf{r}_u \times \mathbf{r}_v$ que es perpendicular al plano tangente en un punto. Su magnitud $|\mathbf{N}|$ es el factor de área de superficie."
        )
    },
    {
        "category": "8. Integrales de Línea y Superficie",
        "name": "Área de superficie diferencial $dS$",
        "definition": (
            "Elemento infinitesimal de área de una superficie parametrizada: $dS = |\mathbf{r}_u \times \mathbf{r}_v| du dv$."
        )
    },
    {
        "category": "8. Integrales de Línea y Superficie",
        "name": "Integral de superficie de un campo escalar",
        "definition": (
            "Integral $\iint_S f(x,y,z) dS$. Se utiliza para calcular la masa de una lámina superficial con densidad $f(x,y,z)$."
        )
    },
    {
        "category": "8. Integrales de Línea y Superficie",
        "name": "Integral de superficie (Flujo)",
        "definition": (
            "Integral $\iint_S \mathbf{F} \cdot d\mathbf{S} = \iint_S \mathbf{F} \cdot \mathbf{N} dS$. Mide el flujo neto de un campo vectorial $\mathbf{F}$ a través de una superficie orientada $S$."
        )
    },
    {
        "category": "8. Integrales de Línea y Superficie",
        "name": "Orientación de una superficie",
        "definition": (
            "Se define por la dirección del vector normal $\mathbf{N}$. Una superficie cerrada tiene orientación **positiva** si la normal apunta hacia afuera."
        )
    },
    
    # ==================================================
    # 9. TEOREMAS FUNDAMENTALES DEL CÁLCULO VECTORIAL (Añadidos)
    # ==================================================
    {
        "category": "9. Teoremas Vectoriales",
        "name": "Teorema de Green",
        "definition": (
            "Relaciona una integral de línea a lo largo de una curva cerrada $C$ en $\mathbb{R}^2$ con una integral doble sobre la región $D$ encerrada por $C$. $$\oint_C (P dx + Q dy) = \iint_D \left(\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}\right) dA$$"
        )
    },
    {
        "category": "9. Teoremas Vectoriales",
        "name": "Teorema de Stokes",
        "definition": (
            "Relaciona la integral de línea de $\mathbf{F}$ a lo largo de una curva cerrada $C$ con la integral de superficie del rotacional sobre $S$. $$\oint_C \mathbf{F} \cdot d\mathbf{r} = \iint_S \operatorname{curl}(\mathbf{F}) \cdot d\mathbf{S}$$"
        )
    },
    {
        "category": "9. Teoremas Vectoriales",
        "name": "Teorema de la Divergencia (Gauss)",
        "definition": (
            "Relaciona el flujo ($\iint_S$) a través de una superficie cerrada $S$ con la integral triple de la divergencia sobre el volumen $E$ encerrado por $S$. $$\iint_S \mathbf{F} \cdot d\mathbf{S} = \iiint_E \operatorname{div}(\mathbf{F}) dV$$"
        )
    },
    {
        "category": "9. Teoremas Vectoriales",
        "name": "Teorema Fundamental para Integrales de Línea",
        "definition": (
            "Si $\mathbf{F} = \nabla \phi$ (campo conservativo), la integral de $\mathbf{F}$ entre dos puntos $\mathbf{r}(a)$ y $\mathbf{r}(b)$ es independiente de la trayectoria: $\int_C \mathbf{F} \cdot d\mathbf{r} = \phi(\mathbf{r}(b)) - \phi(\mathbf{r}(a))$."
        )
    },
    {
        "category": "9. Teoremas Vectoriales",
        "name": "Operador Laplaciano",
        "definition": (
            "Operador $\nabla^2 f = \operatorname{div}(\nabla f)$. Mide la diferencia de $f$ con el valor promedio en su vecindad. En $\mathbb{R}^3$: $$\nabla^2 f = \frac{\partial^2 f}{\partial x^2} + \frac{\partial^2 f}{\partial y^2} + \frac{\partial^2 f}{\partial z^2}$$"
        )
    },
    {
        "category": "9. Teoremas Vectoriales",
        "name": "Campo armónico",
        "definition": (
            "Una función escalar $f$ tal que satisface la Ecuación de Laplace: $\nabla^2 f = 0$."
        )
    },
    {
        "category": "9. Teoremas Vectoriales",
        "name": "Flujo neto (Salida)",
        "definition": (
            "El valor de la integral de superficie (flujo) de un campo vectorial a través de una superficie cerrada. Un valor positivo indica una fuente de campo (salida) en el volumen."
        )
    },
]

# ==================================================
# LÓGICA DE LA APLICACIÓN STREAMLIT
# ==================================================

# 1. Crear una lista de nombres de conceptos para el selector
concept_names = [c["name"] for c in CONCEPTOS]

# 2. Organizar conceptos por categoría en el sidebar
categories = sorted(list(set(c["category"] for c in CONCEPTOS)))

# 3. Mostrar el selector en el sidebar y permitir la navegación por categorías
with st.sidebar:
    st.header("🔍 Selecciona una Sección")
    selected_category = st.radio("Secciones", categories)
    
    # Filtrar conceptos basados en la categoría seleccionada
    filtered_concepts = [c for c in CONCEPTOS if c["category"] == selected_category]
    filtered_names = [c["name"] for c in filtered_concepts]

    st.subheader("Términos")
    
    # Selector de términos
    selected_name = st.selectbox(
        label="Término de Cálculo",
        options=filtered_names,
        index=0 if filtered_names else None,
        key="concept_selector"
    )

# 4. Mostrar el concepto principal
if selected_name:
    # Buscar el objeto de concepto completo
    selected_concept = next(c for c in CONCEPTOS if c["name"] == selected_name)
    
    st.subheader(f"✨ {selected_concept['name']}")
    
    # Usamos st.markdown para renderizar LaTeX
    st.markdown(selected_concept["definition"])
else:
    st.info("Utiliza el menú de la izquierda para explorar los términos.")
