import streamlit as st

st.set_page_config(page_title="Diccionario Cálculo 3 Completo", layout="wide")

st.title("📘 Diccionario Completo de Cálculo Multivariable")
st.write("Selecciona un término para ver su concepto.")

# ==================================================
# DICCIONARIO GLOBAL 
# ==================================================

CONCEPTOS = [

    # ==================================================
    # 1. LÍMITES, CONTINUIDAD, DOMINIOS Y TOPOLOGÍA
    # ==================================================

    {
        "name": "Límite de una función de varias variables",
        "definition": (
            "El límite lim_{(x,y)→(a,b)} f(x,y) existe si el valor de la función se aproxima "
            "al mismo número L al acercarse a (a,b) por cualquier trayectoria del dominio."
        )
    },
    {
        "name": "Límite por trayectorias",
        "definition": (
            "Método para estudiar un límite evaluando f(x,y) cuando (x,y) se acerca al punto "
            "siguiendo distintas curvas o caminos. Si dos trayectorias dan valores distintos, "
            "el límite NO existe."
        )
    },
    {
        "name": "Límite por coordenadas polares",
        "definition": (
            "Técnica para analizar límites en ℝ² sustituyendo x=r cosθ, y=r sinθ. "
            "Si al tomar r→0 el resultado depende de θ, el límite no existe."
        )
    },
    {
        "name": "Continuidad en funciones de varias variables",
        "definition": (
            "Una función es continua en (a,b) si el límite de f(x,y) al acercarse a (a,b) "
            "es igual al valor f(a,b). Se requiere que el límite exista y coincida."
        )
    },
    {
        "name": "Discontinuidad removible",
        "definition": (
            "Ocurre cuando el límite existe pero f no está definida o está mal definida en el punto. "
            "Puede corregirse redefiniendo la función."
        )
    },
    {
        "name": "Discontinuidad esencial (no removible)",
        "definition": (
            "Ocurre cuando el límite no existe o las trayectorias llevan a valores distintos. "
            "No puede resolverse con una simple redefinición."
        )
    },
    {
        "name": "Dominio de una función de varias variables",
        "definition": (
            "El conjunto de puntos donde la función está bien definida. Puede requerir restricciones "
            "por raíces pares, logaritmos, denominadores o condiciones geométricas."
        )
    },
    {
        "name": "Rango de una función de varias variables",
        "definition": (
            "Conjunto de valores posibles que puede tomar f(x,y). En algunos problemas se estudia "
            "la imagen de curvas o superficies completas."
        )
    },
    {
        "name": "Vecindad de un punto",
        "definition": (
            "Un conjunto que contiene un punto (a,b) y todos los puntos situados a una distancia "
            "menor que un radio dado. Representa un entorno local alrededor del punto."
        )
    },
    {
        "name": "Disco abierto en ℝ²",
        "definition": (
            "Conjunto de puntos dentro de un círculo sin incluir la frontera: "
            "D_r(a,b) = {(x,y): sqrt((x-a)^2+(y-b)^2) < r}."
        )
    },
    {
        "name": "Disco cerrado en ℝ²",
        "definition": (
            "Conjunto formado por los puntos dentro del disco y también los puntos de la circunferencia: "
            "D̄_r(a,b) = {(x,y): sqrt((x-a)^2+(y-b)^2) ≤ r}."
        )
    },
    {
        "name": "Conjunto abierto",
        "definition": (
            "Un conjunto es abierto si todo punto contiene una vecindad completamente incluida "
            "en el conjunto. No contiene puntos de frontera."
        )
    },
    {
        "name": "Conjunto cerrado",
        "definition": (
            "Un conjunto que contiene todos sus puntos frontera, o equivalente: su complemento es abierto. "
            "También puede definirse como aquel que contiene todos sus puntos límite."
        )
    },
    {
        "name": "Frontera de un conjunto",
        "definition": (
            "Conjunto de puntos donde cualquier vecindad intersecta tanto el conjunto como su complemento. "
            "Es el 'borde' del conjunto."
        )
    },
    {
        "name": "Interior de un conjunto",
        "definition": (
            "Todos los puntos del conjunto que tienen una vecindad completamente contenida en él. "
            "Representa la parte estrictamente dentro del conjunto."
        )
    },
    {
        "name": "Clausura de un conjunto",
        "definition": (
            "Un conjunto más todos sus puntos límite. Equivale a la unión del conjunto con su frontera."
        )
    },
    {
        "name": "Conjunto acotado",
        "definition": (
            "Un conjunto es acotado si puede encerrarse dentro de una esfera o disco de radio finito. "
            "No se extiende indefinidamente."
        )
    },
    {
        "name": "Conjunto compacto",
        "definition": (
            "En ℝ² un conjunto es compacto si es cerrado y acotado. Este tipo de conjuntos garantizan "
            "propiedades importantes como la existencia de máximos y mínimos globales."
        )
    },
    {
        "name": "Conjunto conexo",
        "definition": (
            "Un conjunto es conexo si no puede dividirse en dos regiones separadas. "
            "Intuitivamente, todo punto está 'conectado' por un camino dentro del conjunto."
        )
    },
    {
        "name": "Región",
        "definition": (
            "Conjunto abierto, conexo y no vacío. Es el tipo de dominio que aparece con frecuencia "
            "en problemas de Cálculo Multivariable."
        )
    },
    {
        "name": "Región simple",
        "definition": (
            "Región que puede describirse mediante desigualdades simples (tipo x entre a y b, "
            "y entre funciones en x). Son ideales para integrales dobles."
        )
    },
    {
        "name": "Región tipo I",
        "definition": (
            "Región donde y está descrita entre dos funciones de x: "
            "D = {(x,y): a ≤ x ≤ b, g1(x) ≤ y ≤ g2(x)}."
        )
    },
    {
        "name": "Región tipo II",
        "definition": (
            "Región donde x está entre dos funciones de y: "
            "D = {(x,y): c ≤ y ≤ d, h1(y) ≤ x ≤ h2(y)}."
        )
    },
    {
        "name": "Conjuntos de nivel",
        "definition": (
            "Para una función f(x,y), el conjunto de nivel f(x,y)=c es la curva donde la función "
            "toma el valor constante c."
        )
    },
    {
        "name": "Superficies de nivel",
        "definition": (
            "En ℝ³, el conjunto de nivel f(x,y,z)=c es una superficie donde todos los puntos cumplen "
            "el mismo valor de la función."
        )
    },
    {
        "name": "Función acotada",
        "definition": (
            "Una función es acotada si existe una constante M tal que |f(x,y)| ≤ M para todos los "
            "puntos del dominio."
        )
    },
    {
        "name": "Función no acotada",
        "definition": (
            "Una función que puede hacerse arbitrariamente grande o pequeña (positiva o negativa) "
            "en alguna región del dominio."
        )
    },
    {
        "name": "Conjunto de puntos límite",
        "definition": (
            "Puntos donde cualquier vecindad contiene puntos del conjunto y puntos que no son del conjunto. "
            "Se relaciona con la clausura."
        )
    },
    {
        "name": "Conjunto denso",
        "definition": (
            "Un conjunto A es denso en otro B si cada punto de B puede aproximarse tanto como se quiera "
            "con puntos de A."
        )
    },
    {
        "name": "Conjunto discreto",
        "definition": (
            "Conjunto cuyos puntos están separados entre sí: cada punto tiene una vecindad que "
            "no contiene otros puntos del conjunto."
        )
    },
    {
        "name": "Vecindad punctuada",
        "definition": (
            "Una vecindad que excluye el punto central (a,b). Se usa en límites para evitar evaluar "
            "f(a,b) directamente."
        )
    },
    {
        "name": "Convergencia de sucesiones en ℝ²",
        "definition": (
            "Una sucesión (x_n, y_n) converge a (a,b) si x_n→a y y_n→b. Esto permite definir límites "
            "de funciones mediante criterios de sucesiones."
        )
    },
    {
        "name": "Criterio de sucesiones para límites",
        "definition": (
            "Un límite lim f(x,y) = L existe si y solo si para toda sucesión (x_n,y_n) que converge "
            "a (a,b), los valores f(x_n,y_n) convergen a L."
        )
    },
    {
        "name": "Conjunto cerrado bajo límite",
        "definition": (
            "Un conjunto es cerrado si contiene el límite de toda sucesión convergente de elementos del conjunto."
        )
    }


    # ==================================================
    # 2. DERIVADAS PARCIALES Y JACOBIANAS
    # ==================================================

    {
        "name": "Derivada parcial",
        "definition": (
            "La derivada parcial de f respecto a x (f_x) mide la tasa de cambio de f cuando "
            "solo x varía y el resto de variables permanecen constantes."
        )
    },
    {
        "name": "Derivadas parciales de primer orden",
        "definition": (
            "Son las derivadas f_x, f_y, f_z, etc. Se obtienen derivando f una sola vez con respecto "
            "a cada variable independiente."
        )
    },
    {
        "name": "Derivadas parciales de segundo orden",
        "definition": (
            "Se obtienen derivando nuevamente las parciales de primer orden. Incluyen f_xx, f_yy, "
            "las mixtas f_xy y f_yx."
        )
    },
    {
        "name": "Derivada parcial mixta",
        "definition": (
            "Derivada de segundo orden donde se derivan respecto a dos variables diferentes, por ejemplo f_xy."
        )
    },
    {
        "name": "Simetría de derivadas mixtas",
        "definition": (
            "Si las segundas derivadas parciales son continuas, entonces f_xy = f_yx. Este resultado "
            "es el Teorema de Clairaut o de Schwarz."
        )
    },
    {
        "name": "Derivadas parciales iteradas",
        "definition": (
            "Derivadas obtenidas aplicando varias veces operadores de derivación parcial, como f_xxy o f_yyx."
        )
    },
    {
        "name": "Gradiente de una función",
        "definition": (
            "Vector formado por las derivadas parciales: ∇f = (f_x, f_y, f_z). Indica dirección y magnitud "
            "de mayor crecimiento de f."
        )
    },
    {
        "name": "Matriz Jacobiana",
        "definition": (
            "Matriz que contiene todas las derivadas parciales de una transformación vectorial F(x,y). "
            "Es clave para cambios de variables y análisis de funciones vectoriales."
        )
    },
    {
        "name": "Determinante Jacobiano",
        "definition": (
            "El determinante de la matriz Jacobiana. Mide el factor de escala del cambio de variables. "
            "Es esencial en integrales múltiples."
        )
    },
    {
        "name": "Jacobiano positivo",
        "definition": (
            "Cuando el determinante del Jacobiano es > 0 indica que la transformación conserva orientación."
        )
    },
    {
        "name": "Jacobiano negativo",
        "definition": (
            "Si el determinante es < 0 la transformación invierte orientación."
        )
    },
    {
        "name": "Punto crítico de un mapeo",
        "definition": (
            "Punto donde el Jacobiano se anula o pierde rango. Suele indicar singularidades o "
            "problemas de inversión."
        )
    },
    {
        "name": "Regla de la cadena para funciones escalares",
        "definition": (
            "Si z = f(x,y) y x = x(t), y = y(t), entonces dz/dt = f_x dx/dt + f_y dy/dt."
        )
    },
    {
        "name": "Regla de la cadena para funciones compuestas",
        "definition": (
            "Generaliza la regla de la cadena: si F = f(g(x,y), h(x,y)), entonces ∇F se obtiene "
            "multiplicando las Jacobianas correspondientes."
        )
    },
    {
        "name": "Derivada total",
        "definition": (
            "Expresa el cambio total de f cuando todas sus variables dependen de otra variable t: "
            "df/dt = f_x dx/dt + f_y dy/dt + f_z dz/dt."
        )
    },
    {
        "name": "Plano tangente mediante derivadas parciales",
        "definition": (
            "Para z=f(x,y), el plano tangente en (a,b) se obtiene usando f_x(a,b) y f_y(a,b)."
        )
    },
    {
        "name": "Dirección de máximo crecimiento",
        "definition": (
            "Dirección dada por el gradiente ∇f. La magnitud del crecimiento es |∇f|."
        )
    },
    {
        "name": "Derivada direccional",
        "definition": (
            "La tasa de cambio de f en una dirección dada u. Se calcula como D_u f = ∇f · u."
        )
    },
    {
        "name": "Superficie diferenciable",
        "definition": (
            "Una superficie z=f(x,y) es diferenciable si su aproximación lineal existe y su error tiende "
            "a cero más rápido que la distancia al punto."
        )
    },
    {
        "name": "Jacobiano de una transformación",
        "definition": (
            "El Jacobiano representa el factor de escala que transforma áreas o volúmenes bajo cambios "
            "de coordenadas."
        )
    },
    {
        "name": "Transformación invertible",
        "definition": (
            "Una transformación F(x,y) es invertible localmente si su Jacobiano es distinto de cero en el punto."
        )
    },
    {
        "name": "Regla de la cadena en notación matricial",
        "definition": (
            "Si F depende de G y G depende de x, entonces J_F = J_f ∘ J_g. Se multiplican Jacobianas "
            "como matrices."
        )
    },
    {
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
        "name": "Diferenciabilidad",
        "definition": (
            "Una función es diferenciable en un punto si puede aproximarse linealmente mediante su "
            "gradiente, y el error tiende más rápido a 0 que la distancia al punto."
        )
    },
    {
        "name": "Aproximación lineal",
        "definition": (
            "Aproximación de f(x,y) por su plano tangente: f(x,y) ≈ f(a,b) + f_x(a,b)(x−a) + f_y(a,b)(y−b)."
        )
    },
    {
        "name": "Error de aproximación lineal",
        "definition": (
            "Diferencia entre la función y su aproximación lineal. Para diferenciabilidad, debe "
            "disminuir más rápido que la distancia a (a,b)."
        )
    },
    {
        "name": "Plano tangente",
        "definition": (
            "Plano que mejor aproxima la superficie en un punto. Se construye con f_x y f_y."
        )
    },
    {
        "name": "Mapa diferencial",
        "definition": (
            "La aplicación lineal que mejor aproxima la función en un punto. Es la generalización "
            "del plano tangente."
        )
    },
    {
        "name": "Linealización",
        "definition": (
            "Sinónimo de aproximación lineal, usando la derivada total o el gradiente."
        )
    },
    {
        "name": "Regla de la cadena (versión general)",
        "definition": (
            "Si y=g(u,v) y u=u(x,y), v=v(x,y), entonces las derivadas se calculan mediante la "
            "multiplicación de las Jacobianas correspondientes."
        )
    },
    {
        "name": "Jacobiano de una función compuesta",
        "definition": (
            "Es el producto de las Jacobianas individuales: J(f∘g)=J(f)J(g)."
        )
    },
    {
        "name": "Función diferenciable pero con parciales discontinuas",
        "definition": (
            "Existen funciones diferenciables cuyas derivadas parciales no son continuas. "
            "La diferenciabilidad es una condición más fuerte."
        )
    },
    {
        "name": "Diferenciabilidad fuerte",
        "definition": (
            "Supone continuidad de todas las derivadas parciales. Garantiza mejor suavidad "
            "y propiedades teóricas."
        )
    },
    {
        "name": "Condición suficiente de diferenciabilidad",
        "definition": (
            "Si todas las derivadas parciales de primer orden son continuas, entonces la función "
            "es diferenciable."
        )
    },
    {
        "name": "Diferencial total",
        "definition": (
            "Generalización del diferencial de Cálculo 1: df = f_x dx + f_y dy + f_z dz."
        )
    },
    {
        "name": "Interpretación geométrica de la diferenciabilidad",
        "definition": (
            "La función se comporta localmente como un plano (en ℝ³) o una recta (en ℝ²)."
        )
    }

    # ==================================================
    # 4. GRADIENTE, DERIVADAS DIRECCIONALES, PLANO TANGENTE
    # ==================================================

    {
        "name": "Gradiente de una función",
        "definition": (
            "El gradiente ∇f es el vector formado por las derivadas parciales de f. "
            "Indica la dirección de máximo crecimiento de la función."
        )
    },
    {
        "name": "Magnitud del gradiente",
        "definition": (
            "La norma |∇f| mide la pendiente máxima de la función en un punto."
        )
    },
    {
        "name": "Interpretación geométrica del gradiente",
        "definition": (
            "El gradiente es perpendicular (normal) a las curvas o superficies de nivel. "
            "Apunta hacia donde f aumenta más rápidamente."
        )
    },
    {
        "name": "Derivada direccional",
        "definition": (
            "La tasa de cambio de f en la dirección de un vector unitario u. "
            "Se calcula como D_u f = ∇f · u."
        )
    },
    {
        "name": "Derivada direccional máxima",
        "definition": (
            "La derivada direccional es máxima cuando la dirección u coincide con el gradiente."
        )
    },
    {
        "name": "Dirección de aumento más rápido",
        "definition": (
            "La dirección del gradiente ∇f, donde la función crece a la tasa máxima."
        )
    },
    {
        "name": "Plano tangente a una superficie",
        "definition": (
            "Para z=f(x,y), el plano tangente en (a,b) se obtiene mediante: "
            "z = f(a,b) + f_x(a,b)(x−a) + f_y(a,b)(y−b)."
        )
    },
    {
        "name": "Plano normal a una superficie",
        "definition": (
            "El plano cuya normal es el gradiente ∇f(a,b). Representa la orientación perpendicular "
            "al plano tangente."
        )
    },
    {
        "name": "Recta normal",
        "definition": (
            "Línea que pasa por el punto y tiene como dirección el gradiente ∇f."
        )
    },
    {
        "name": "Curvas de nivel",
        "definition": (
            "Curvas donde f(x,y)=c. El gradiente es perpendicular en cada punto."
        )
    },
    {
        "name": "Superficies de nivel",
        "definition": (
            "Superficies en ℝ³ donde f(x,y,z)=c. El gradiente es normal a ellas."
        )
    },
    {
        "name": "Relación entre gradiente y derivada direccional",
        "definition": (
            "La derivada direccional D_u f es el producto punto ∇f·u. "
            "Esto muestra que ∇f contiene toda la información direccional."
        )
    },
    {
        "name": "Curvatura de una curva de nivel",
        "definition": (
            "La curvatura indica cómo cambia la dirección del gradiente a lo largo de la curva."
        )
    },

    # ==================================================
    # 5. HESSIANA, SEGUNDA DERIVADA Y CLASIFICACIÓN DE PUNTOS
    # ==================================================

    {
        "name": "Matriz Hessiana",
        "definition": (
            "Matriz cuadrada formada por las segundas derivadas de f. "
            "Para dos variables: Hf = [[f_xx, f_xy], [f_yx, f_yy]]."
        )
    },
    {
        "name": "Simetría de la Hessiana",
        "definition": (
            "Si las segundas derivadas parciales son continuas, entonces f_xy = f_yx "
            "y la Hessiana es simétrica."
        )
    },
    {
        "name": "Forma cuadrática asociada a la Hessiana",
        "definition": (
            "Expresión Q(h,k) = [h k] Hf [h k]^T que permite clasificar el tipo de punto crítico."
        )
    },
    {
        "name": "Determinante de la Hessiana",
        "definition": (
            "D = f_xx f_yy − (f_xy)^2. Sirve para clasificar puntos críticos mediante la segunda derivada."
        )
    },
    {
        "name": "Criterio de la segunda derivada",
        "definition": (
            "Si D>0 y f_xx>0: mínimo local; "
            "si D>0 y f_xx<0: máximo local; "
            "si D<0: punto de silla; "
            "si D=0: prueba inconclusa."
        )
    },
    {
        "name": "Punto crítico",
        "definition": (
            "Punto donde el gradiente se anula (∇f=0) o no existe. "
            "Es un candidato a extremo o punto de silla."
        )
    },
    {
        "name": "Punto de silla",
        "definition": (
            "Punto crítico donde la función aumenta en unas direcciones y disminuye en otras, "
            "como f(x,y)=x^2−y^2."
        )
    },
    {
        "name": "Máximo local",
        "definition": (
            "Punto donde f(x0,y0) es mayor que los valores en puntos cercanos. "
            "Requiere ∇f=0 y Hessiana negativa definida."
        )
    },
    {
        "name": "Mínimo local",
        "definition": (
            "Punto donde f(x0,y0) es menor que los valores de f en puntos cercanos. "
            "Requiere Hessiana positiva definida."
        )
    },
    {
        "name": "Hessiana positiva definida",
        "definition": (
            "Una matriz Hessiana H es positiva definida si h^T H h > 0 para todo vector no nulo h. "
            "Implica un mínimo local."
        )
    },
    {
        "name": "Hessiana negativa definida",
        "definition": (
            "H es negativa definida si h^T H h < 0 para todo vector no nulo h. "
            "Indica un máximo local."
        )
    },
    {
        "name": "Hessiana indefinida",
        "definition": (
            "Si la forma cuadrática toma valores positivos y negativos, indica un punto de silla."
        )
    },
    {
        "name": "Autovalores de la Hessiana",
        "definition": (
            "Los autovalores determinan la curvatura en distintas direcciones. "
            "Todos positivos ⇒ mínimo; todos negativos ⇒ máximo; mezcla ⇒ silla."
        )
    },
    {
        "name": "Direcciones principales de curvatura",
        "definition": (
            "Direcciones asociadas a los autovectores de la Hessiana. "
            "Cada una describe la curvatura extrema de la superficie."
        )
    },
    {
        "name": "Concavidad y convexidad",
        "definition": (
            "La convexidad se relaciona con Hessiana positiva semidefinida. "
            "La concavidad con Hessiana negativa semidefinida."
        )
    },
    {
        "name": "Punto singular",
        "definition": (
            "Punto donde la Hessiana pierde rango o las derivadas no existen. "
            "Requiere un análisis especial."
        )
    },
    {
        "name": "Clasificación de puntos críticos",
        "definition": (
            "Procedimiento que, usando la Hessiana, determina si un punto crítico es máximo, mínimo "
            "o silla."
        )
    },
    {
        "name": "Extremos globales",
        "definition": (
            "Máximos o mínimos sobre todo el dominio. En conjuntos compactos siempre existen."
        )
    },
    {
        "name": "Extremos en frontera",
        "definition": (
            "Para dominios con borde, los máximos/mínimos también pueden aparecer en la frontera. "
            "Debe verificarse con métodos especiales."
        )
    }

    # ==================================================
    # 6. CAMPOS VECTORIALES, DIVERGENCIA, ROTACIONAL
    # ==================================================

    {
        "name": "Campo vectorial en ℝ²",
        "definition": (
            "Es una función F(x,y) que asigna a cada punto un vector. "
            "Se representa como F(x,y) = (P(x,y), Q(x,y))."
        )
    },
    {
        "name": "Campo vectorial en ℝ³",
        "definition": (
            "Es una función F(x,y,z) = (P, Q, R) que asigna un vector tridimensional a cada punto."
        )
    },
    {
        "name": "Campo conservativo",
        "definition": (
            "Un campo F es conservativo si existe una función potencial φ tal que "
            "F = ∇φ. La circulación alrededor de cualquier curva cerrada es cero."
        )
    },
    {
        "name": "Función potencial",
        "definition": (
            "Función escalar φ tal que su gradiente ∇φ es igual al campo vectorial. "
            "Permite calcular integrales de línea fácilmente."
        )
    },
    {
        "name": "Condición de conservatividad en ℝ²",
        "definition": (
            "Si F=(P,Q) y las derivadas son continuas, entonces F es conservativo si P_y = Q_x."
        )
    },
    {
        "name": "Campo irrotacional",
        "definition": (
            "Un campo cuyo rotacional es cero. En regiones simplemente conexas, ser irrotacional "
            "equivale a ser conservativo."
        )
    },
    {
        "name": "Campo solenoidal",
        "definition": (
            "Un campo con divergencia cero: div(F)=0. Se relaciona con flujos incompresibles."
        )
    },
    {
        "name": "Divergencia de un campo",
        "definition": (
            "div(F) = ∂P/∂x + ∂Q/∂y + ∂R/∂z. Mide la tasa neta de flujo que 'sale' de un punto."
        )
    },
    {
        "name": "Rotacional de un campo",
        "definition": (
            "curl(F) = ∇ × F mide la tendencia del campo a generar rotación o vorticidad."
        )
    },
    {
        "name": "Rotacional en ℝ³",
        "definition": (
            "curl(F) = (R_y − Q_z, P_z − R_x, Q_x − P_y). "
            "Indica cuánto gira el campo alrededor de un punto."
        )
    },
    {
        "name": "Rotacional en ℝ²",
        "definition": (
            "En 2D se considera curl(F) = Q_x − P_y (es un escalar)."
        )
    },
    {
        "name": "Región simplemente conexa",
        "definition": (
            "Región sin 'agujeros'. En estas regiones, cualquier campo irrotacional es conservativo."
        )
    },
    {
        "name": "Región no simplemente conexa",
        "definition": (
            "Región con agujeros. En estas regiones puede haber campos irrotacionales que no sean conservativos."
        )
    },
    {
        "name": "Flujo de un campo vectorial",
        "definition": (
            "El flujo mide cuánto del campo atraviesa una curva o superficie."
        )
    },
    {
        "name": "Líneas de corriente",
        "definition": (
            "Curvas cuyas tangentes coinciden con el campo vectorial. "
            "Se interpretan como trayectorias de partículas en un flujo."
        )
    },
    {
        "name": "Curvas parametrizadas en ℝ²",
        "definition": (
            "Una curva se expresa como r(t)=(x(t),y(t)), a ≤ t ≤ b. "
            "Permite describir trayectorias o bordes de regiones."
        )
    },
    {
        "name": "Curvas parametrizadas en ℝ³",
        "definition": (
            "Curva definida como r(t)=(x(t),y(t),z(t)). Ideal para analizar movimiento en el espacio."
        )
    },
    {
        "name": "Vector tangente a una curva",
        "definition": (
            "El vector r'(t) indica la dirección de la curva en el punto r(t)."
        )
    },
    {
        "name": "Campo gradiente",
        "definition": (
            "Campo de la forma F = ∇f. Todo campo conservativo tiene esta forma."
        )
    },
    {
        "name": "Circulación de un campo",
        "definition": (
            "La integral de línea de F a lo largo de una curva. Mide el trabajo realizado por el campo."
        )
    },
    {
        "name": "Circulación alrededor de una curva cerrada",
        "definition": (
            "Si F es conservativo, esta circulación es cero para cualquier curva cerrada."
        )
    },
    {
        "name": "Teorema del campo gradiente",
        "definition": (
            "La integral de F=∇φ entre dos puntos depende solo del valor de φ en los extremos."
        )
    },
    {
        "name": "Campo estacionario",
        "definition": (
            "Un campo que no depende del tiempo. Se usa en modelos de flujo permanente."
        )
    },
    {
        "name": "Magnitud de un campo vectorial",
        "definition": (
            "En ℝ³, la magnitud es |F|=√(P²+Q²+R²). Indica fuerza o intensidad del campo."
        )
    },
    {
        "name": "Campo radial",
        "definition": (
            "Campo de la forma F(x,y,z)=k·(x,y,z). Apunta hacia afuera o hacia el origen."
        )
    },
    {
        "name": "Campo central",
        "definition": (
            "Campo que depende solo de la distancia al origen: F = f(r) * (x,y,z)/r."
        )
    },
    {
        "name": "Campo de rotación pura",
        "definition": (
            "Campo con divergencia cero pero rotacional no nulo, como (-y,x) en ℝ²."
        )
    },
    {
        "name": "Curva cerrada",
        "definition": (
            "Curva donde r(a)=r(b). Se usa en teoremas de circulación como el de Green."
        )
    }

    # ==================================================
    # 7. INTEGRALES DOBLES Y TRIPLES
    # ==================================================

    {
        "name": "Integral doble",
        "definition": (
            "La integral ∬_D f(x,y) dA calcula el volumen bajo la superficie z=f(x,y) "
            "sobre una región D del plano."
        )
    },
    {
        "name": "Interpretación geométrica de la integral doble",
        "definition": (
            "Representa la suma acumulada de infinitos rectángulos de área diferencial dA "
            "multiplicados por la altura f(x,y)."
        )
    },
    {
        "name": "Región de integración tipo I",
        "definition": (
            "Región descrita por a ≤ x ≤ b, g1(x) ≤ y ≤ g2(x). "
            "Se usa para integrar respecto a y y luego x."
        )
    },
    {
        "name": "Región de integración tipo II",
        "definition": (
            "Región descrita por c ≤ y ≤ d, h1(y) ≤ x ≤ h2(y). "
            "Se integra primero sobre x y luego sobre y."
        )
    },
    {
        "name": "Integral iterada",
        "definition": (
            "Expresión donde se integra primero respecto a una variable y luego respecto a otra. "
            "Equivale a una integral doble en regiones rectangulares o simples."
        )
    },
    {
        "name": "Área diferencial dA",
        "definition": (
            "Elemento infinitesimal de área en el plano. En coordenadas rectangulares dA = dx dy."
        )
    },
    {
        "name": "Región acotada",
        "definition": (
            "Una región es acotada si cabe dentro de un disco de radio finito."
        )
    },
    {
        "name": "Integral triple",
        "definition": (
            "La integral ∭_E f(x,y,z) dV representa el volumen o la masa dentro de una región sólida E."
        )
    },
    {
        "name": "Interpretación geométrica de la integral triple",
        "definition": (
            "Suma de infinitos prismas de volumen dV multiplicados por la densidad f(x,y,z)."
        )
    },
    {
        "name": "Elemento de volumen dV",
        "definition": (
            "En coordenadas rectangulares dV = dx dy dz."
        )
    },
    {
        "name": "Densidad variable",
        "definition": (
            "Función ρ(x,y,z) que permite calcular masas mediante integrales dobles o triples."
        )
    },
    {
        "name": "Centroide (centro de masa)",
        "definition": (
            "El punto 'promedio' de una región con densidad uniforme o variable. "
            "Se calcula usando integrales para los momentos."
        )
    },
    {
        "name": "Momento respecto a un eje",
        "definition": (
            "Representa la tendencia de una masa a rotar respecto a un eje. Se calcula integrando "
            "la distancia al eje multiplicada por la densidad."
        )
    },
    {
        "name": "Momento de inercia",
        "definition": (
            "Magnitud física que mide la resistencia de un cuerpo a cambios en su rotación. "
            "En Cálculo se obtiene mediante integrales: I = ∬ r² ρ dA."
        )
    },
    {
        "name": "Región sólida tipo caja",
        "definition": (
            "Región donde cada una de las tres variables está acotada por constantes."
        )
    },
    {
        "name": "Región sólida general",
        "definition": (
            "Región descrita por funciones para los límites de x, y y z."
        )
    },

    # ==================================================
    # 8. CAMBIO DE VARIABLES EN INTEGRALES
    # ==================================================

    {
        "name": "Cambio de variable en integrales dobles",
        "definition": (
            "Técnica para transformar una región difícil en otra más simple mediante una "
            "transformación (u,v) con un Jacobiano J."
        )
    },
    {
        "name": "Factor de escala del Jacobiano",
        "definition": (
            "En un cambio de variable dA = |J| du dv, donde |J| es el valor absoluto del determinante "
            "del Jacobiano de la transformación."
        )
    },
    {
        "name": "Cambio a coordenadas polares",
        "definition": (
            "Transformación x = r cosθ, y = r sinθ. El Jacobiano es r, de modo que dA = r dr dθ."
        )
    },
    {
        "name": "Coordenada radial r",
        "definition": (
            "Distancia del punto al origen: r = √(x² + y²)."
        )
    },
    {
        "name": "Coordenada angular θ",
        "definition": (
            "Ángulo respecto al eje positivo x. Describe dirección del punto."
        )
    },
    {
        "name": "Región circular en polares",
        "definition": (
            "Región descrita por 0 ≤ r ≤ R y θ entre dos ángulos α y β."
        )
    },
    {
        "name": "Cambio a coordenadas cilíndricas",
        "definition": (
            "Usado para integrales triples: x = r cosθ, y = r sinθ, z = z. "
            "El Jacobiano es r, así que dV = r dr dθ dz."
        )
    },
    {
        "name": "Coordenadas cilíndricas",
        "definition": (
            "Sistema definido por (r, θ, z). Útil para sólidos de revolución o regiones circulares."
        )
    },
    {
        "name": "Cambio a coordenadas esféricas",
        "definition": (
            "Transformación x = ρ sinφ cosθ, y = ρ sinφ sinθ, z = ρ cosφ. "
            "El Jacobiano es ρ² sinφ, de modo que dV = ρ² sinφ dρ dφ dθ."
        )
    },
    {
        "name": "Coordenada radial ρ",
        "definition": (
            "Distancia del punto al origen en tres dimensiones."
        )
    },
    {
        "name": "Coordenada polar φ",
        "definition": (
            "Ángulo medido desde el eje z hacia abajo."
        )
    },
    {
        "name": "Coordenada azimutal θ",
        "definition": (
            "Ángulo alrededor del eje z, igual al de coordenadas cilíndricas."
        )
    },
    {
        "name": "Región esférica",
        "definition": (
            "Región descrita mediante 0 ≤ ρ ≤ R y rangos para φ y θ."
        )
    },
    {
        "name": "Región en forma de cono",
        "definition": (
            "Región descrita típicamente con φ constante en coordenadas esféricas."
        )
    },
    {
        "name": "Uso del Jacobiano en integrales triples",
        "definition": (
            "En cambios de coordenadas en 3D, el Jacobiano determina cómo se transforma el volumen: "
            "dV = |J| du dv dw."
        )
    },
    {
        "name": "Región simple para cambio de variables",
        "definition": (
            "Región donde los límites en las nuevas variables son constantes o funciones simples."
        )
    },
    {
        "name": "Integral de masa mediante cambio de variables",
        "definition": (
            "Si la densidad se expresa mejor en otro sistema de coordenadas, se usa el Jacobiano "
            "para transformar la integral."
        )
    },
    {
        "name": "Aplicación física del cambio de coordenadas",
        "definition": (
            "Facilita cálculos en problemas radiales, cilíndricos o esféricos, como cargas eléctricas "
            "o distribuciones de masa."
        )
    }

    # ==================================================
    # 9. TEOREMAS VECTORIALES: GREEN, STOKES, GAUSS (DIVERGENCIA)
    # ==================================================

    {
        "name": "Teorema de Green",
        "definition": (
            "Relaciona la circulación de un campo vectorial F=(P,Q) alrededor de una curva cerrada C "
            "con la integral doble del rotacional sobre la región D encerrada por C:\n"
            "∮_C P dx + Q dy = ∬_D (Q_x − P_y) dA."
        )
    },
    {
        "name": "Interpretación del teorema de Green",
        "definition": (
            "Indica que la circulación alrededor de un borde es igual a la suma de la rotación interior "
            "del campo en toda la región."
        )
    },
    {
        "name": "Orientación positiva de una curva cerrada",
        "definition": (
            "Una curva cerrada tiene orientación positiva si se recorre en sentido contrario a las manecillas "
            "del reloj, dejando la región encerrada a la izquierda."
        )
    },
    {
        "name": "Orientación negativa de una curva cerrada",
        "definition": (
            "Cuando la curva se recorre en sentido horario, la orientación es negativa."
        )
    },
    {
        "name": "Curva simple cerrada",
        "definition": (
            "Curva que no se cruza consigo misma y cuya parametrización cumple r(a)=r(b)."
        )
    },
    {
        "name": "Región simplemente conexa",
        "definition": (
            "Región sin agujeros. Green se aplica directamente en este tipo de regiones."
        )
    },
    {
        "name": "Región con agujeros (no simplemente conexa)",
        "definition": (
            "Región donde Green puede aplicarse si se ajusta la orientación de cada borde interior."
        )
    },
    {
        "name": "Teorema de Stokes",
        "definition": (
            "Generaliza el teorema de Green a superficies en ℝ³:\n"
            "∮_C F·dr = ∬_S (curl F)·n dS."
        )
    },
    {
        "name": "Interpretación del teorema de Stokes",
        "definition": (
            "La circulación de F alrededor del borde C es igual al flujo del rotacional del campo "
            "a través de la superficie S."
        )
    },
    {
        "name": "Superficie orientable",
        "definition": (
            "Superficie en la que es posible elegir de manera consistente una dirección normal. "
            "Ejemplo: una esfera. Una banda de Möbius NO es orientable."
        )
    },
    {
        "name": "Normal unitaria",
        "definition": (
            "Vector unitario perpendicular a la superficie. Su orientación determina el signo del flujo."
        )
    },
    {
        "name": "Flujo de un campo vectorial a través de una superficie",
        "definition": (
            "Se calcula mediante ∬_S F·n dS. Mide cuánto del campo atraviesa la superficie."
        )
    },
    {
        "name": "Superficie con borde",
        "definition": (
            "Superficie cuya frontera es la curva C, utilizada en el teorema de Stokes."
        )
    },
    {
        "name": "Orientación compatible",
        "definition": (
            "La orientación del borde C debe ser coherente con la normal de la superficie "
            "según la regla de la mano derecha."
        )
    },
    {
        "name": "Teorema de Gauss o Divergencia",
        "definition": (
            "El flujo de un campo vectorial a través de la superficie cerrada S es igual a la integral "
            "triple de la divergencia del campo sobre la región E encerrada por S:\n"
            "∯_S F·n dS = ∭_E div(F) dV."
        )
    },
    {
        "name": "Interpretación del teorema de Gauss",
        "definition": (
            "Mide la cantidad neta de campo que 'sale' del volumen. Se interpreta como una ley de conservación."
        )
    },
    {
        "name": "Superficie cerrada",
        "definition": (
            "Superficie que encierra completamente un volumen, como una esfera o un cubo."
        )
    },
    {
        "name": "Divergencia positiva",
        "definition": (
            "Indica que el campo se comporta como una fuente: más campo sale del que entra."
        )
    },
    {
        "name": "Divergencia negativa",
        "definition": (
            "Indica que el campo se comporta como un sumidero: entra más campo del que sale."
        )
    },
    {
        "name": "Circulación",
        "definition": (
            "La integral de línea de un campo alrededor de una curva cerrada. "
            "Aparece en Green y Stokes."
        )
    },
    {
        "name": "Flujo",
        "definition": (
            "La cantidad total del campo que atraviesa una superficie. Fundamental en Gauss y Stokes."
        )
    },
    {
        "name": "Regla de la mano derecha (orientación en Stokes)",
        "definition": (
            "Determina la orientación correcta del borde: si los dedos siguen la dirección del borde, "
            "el pulgar apunta en la dirección de la normal positiva."
        )
    },
    {
        "name": "Bordes interiores en el teorema de Green",
        "definition": (
            "Si la región tiene agujeros, cada borde interior debe recorrerse en sentido horario "
            "para mantener la orientación positiva global."
        )
    },
    {
        "name": "Integración sobre superficies parametrizadas",
        "definition": (
            "Una superficie S parametrizada por r(u,v) tiene elemento de área dS = |r_u × r_v| du dv."
        )
    }

    # ==================================================
    # 10. OPTIMIZACIÓN SIN RESTRICCIONES
    # ==================================================

    {
        "name": "Optimización sin restricciones",
        "definition": (
            "Busca máximos o mínimos de f(x,y,...) sin condiciones adicionales. "
            "Se utilizan puntos críticos donde ∇f = 0."
        )
    },
    {
        "name": "Punto crítico",
        "definition": (
            "Punto donde el gradiente se anula (∇f = 0) o no existe. "
            "Son candidatos para extremos locales."
        )
    },
    {
        "name": "Clasificación de puntos críticos",
        "definition": (
            "Se determina usando la Hessiana: mínimo si H positiva definida, máximo si H negativa definida, "
            "silla si indefinida."
        )
    },
    {
        "name": "Máximo local",
        "definition": (
            "Punto donde f tiene un valor mayor que en puntos cercanos. H es negativa definida."
        )
    },
    {
        "name": "Mínimo local",
        "definition": (
            "Punto donde f tiene un valor menor que en puntos cercanos. H es positiva definida."
        )
    },
    {
        "name": "Máximo global",
        "definition": (
            "Punto donde f alcanza su mayor valor en todo el dominio."
        )
    },
    {
        "name": "Mínimo global",
        "definition": (
            "Punto donde f alcanza su menor valor en todo el dominio."
        )
    },
    {
        "name": "Extremos globales en conjuntos compactos",
        "definition": (
            "Si el dominio es compacto (cerrado y acotado), f siempre tiene máximo y mínimo globales."
        )
    },
    {
        "name": "Extremos en la frontera",
        "definition": (
            "Los valores máximos o mínimos pueden ocurrir en la frontera del dominio. "
            "Debe analizarse junto a los puntos críticos del interior."
        )
    },
    {
        "name": "Punto de silla",
        "definition": (
            "Punto crítico donde f crece en algunas direcciones y decrece en otras."
        )
    },
    {
        "name": "Curvatura de f en un punto crítico",
        "definition": (
            "La curvatura en las distintas direcciones está determinada por los autovalores de la Hessiana."
        )
    },
    {
        "name": "Direcciones principales",
        "definition": (
            "Direcciones asociadas a autovectores de la Hessiana, donde la función tiene mayor o menor curvatura."
        )
    },

    # ==================================================
    # 11. OPTIMIZACIÓN CON RESTRICCIONES (LAGRANGE)
    # ==================================================

    {
        "name": "Optimización con restricciones",
        "definition": (
            "Busca extremos de f(x,y,...) sujetos a que g(x,y,...) = c. "
            "La solución debe satisfacer tanto f como la restricción."
        )
    },
    {
        "name": "Restricción explícita",
        "definition": (
            "Una restricción donde es posible despejar una variable en función de las otras, "
            "reduciendo la dimensión del problema."
        )
    },
    {
        "name": "Restricción implícita",
        "definition": (
            "Restricción dada por g(x,y)=c donde no es fácil despejar. "
            "Se usa el método de Lagrange."
        )
    },
    {
        "name": "Método de los multiplicadores de Lagrange",
        "definition": (
            "Consiste en resolver ∇f = λ∇g junto con la ecuación de restricción g(x,y)=c. "
            "Los puntos solucionan el sistema de Lagrange."
        )
    },
    {
        "name": "Sistema de Lagrange",
        "definition": (
            "Conjunto de ecuaciones formado por ∇f(x,y)=λ∇g(x,y) y g(x,y)=c."
        )
    },
    {
        "name": "Condición geométrica de Lagrange",
        "definition": (
            "En el punto óptimo, las curvas o superficies de nivel de f y de g son tangentes. "
            "Equivale a que ∇f y ∇g sean paralelos."
        )
    },
    {
        "name": "Interpretación geométrica del multiplicador λ",
        "definition": (
            "λ mide el cambio en el valor óptimo de f respecto a pequeñas variaciones en la restricción g=c."
        )
    },
    {
        "name": "Superficie de restricción",
        "definition": (
            "Conjunto de puntos que satisfacen la condición g(x,y)=c. La búsqueda del extremo se "
            "limita a esta superficie."
        )
    },
    {
        "name": "Curva de restricción",
        "definition": (
            "En ℝ², la restricción g(x,y)=c forma una curva sobre la cual debe encontrarse el extremo."
        )
    },
    {
        "name": "Función objetivo",
        "definition": (
            "La función f que se desea maximizar o minimizar."
        )
    },
    {
        "name": "Multiplicador de Lagrange",
        "definition": (
            "Parámetro λ que aparece en el sistema de Lagrange. Representa la tasa de cambio del valor óptimo "
            "respecto a la restricción."
        )
    },
    {
        "name": "Lagrangiano",
        "definition": (
            "Función auxiliar definida como L(x,y,λ)=f(x,y)+λ(g(x,y)−c). "
            "Sus derivadas parciales generan el sistema de Lagrange."
        )
    },
    {
        "name": "Puntos candidatos a extremos con restricción",
        "definition": (
            "Soluciones del sistema de Lagrange que satisfacen la restricción g=c."
        )
    },
    {
        "name": "Extremos bajo restricciones múltiples",
        "definition": (
            "Si existen varias restricciones g1, g2, ... se introduce un multiplicador λ para cada una."
        )
    },
    {
        "name": "Optimización sobre curvas cerradas",
        "definition": (
            "Para curvas cerradas o compactas, la existencia de extremos está garantizada."
        )
    },
    {
        "name": "Optimización sobre superficies",
        "definition": (
            "Para f(x,y,z) sujeta a g(x,y,z)=c, la superficie de restricción es "
            "bidimensional y debe recorrerse localmente."
        )
    },
    {
        "name": "Extremos condicionados",
        "definition": (
            "Valores máximos o mínimos de f sobre la región definida por la restricción."
        )
    },
    {
        "name": "Método mixto: interior + frontera",
        "definition": (
            "La solución global puede estar en un punto crítico del interior o en la frontera. "
            "Deben analizarse ambos."
        )
    },
    {
        "name": "Regiones factibles",
        "definition": (
            "Conjunto de puntos que satisfacen la restricción. La optimización se limita a esta zona."
        )
    },
    {
        "name": "Interpretación geométrica de ∇f = λ∇g",
        "definition": (
            "Representa paralelismo entre gradientes; las curvas de nivel se tocan sin cruzarse."
        )
    },
    {
        "name": "Restricción activa",
        "definition": (
            "Restricción que se cumple con igualdad en el punto óptimo."
        )
    },
    {
        "name": "Restricción inactiva",
        "definition": (
            "Restricción que no afecta el punto óptimo porque no se cumple con igualdad."
        )
    }

    # ==================================================
    # 10. OPTIMIZACIÓN SIN RESTRICCIONES
    # ==================================================

    {
        "name": "Optimización sin restricciones",
        "definition": (
            "Busca máximos o mínimos de f(x,y,...) sin condiciones adicionales. "
            "Se utilizan puntos críticos donde ∇f = 0."
        )
    },
    {
        "name": "Punto crítico",
        "definition": (
            "Punto donde el gradiente se anula (∇f = 0) o no existe. "
            "Son candidatos para extremos locales."
        )
    },
    {
        "name": "Clasificación de puntos críticos",
        "definition": (
            "Se determina usando la Hessiana: mínimo si H positiva definida, máximo si H negativa definida, "
            "silla si indefinida."
        )
    },
    {
        "name": "Máximo local",
        "definition": (
            "Punto donde f tiene un valor mayor que en puntos cercanos. H es negativa definida."
        )
    },
    {
        "name": "Mínimo local",
        "definition": (
            "Punto donde f tiene un valor menor que en puntos cercanos. H es positiva definida."
        )
    },
    {
        "name": "Máximo global",
        "definition": (
            "Punto donde f alcanza su mayor valor en todo el dominio."
        )
    },
    {
        "name": "Mínimo global",
        "definition": (
            "Punto donde f alcanza su menor valor en todo el dominio."
        )
    },
    {
        "name": "Extremos globales en conjuntos compactos",
        "definition": (
            "Si el dominio es compacto (cerrado y acotado), f siempre tiene máximo y mínimo globales."
        )
    },
    {
        "name": "Extremos en la frontera",
        "definition": (
            "Los valores máximos o mínimos pueden ocurrir en la frontera del dominio. "
            "Debe analizarse junto a los puntos críticos del interior."
        )
    },
    {
        "name": "Punto de silla",
        "definition": (
            "Punto crítico donde f crece en algunas direcciones y decrece en otras."
        )
    },
    {
        "name": "Curvatura de f en un punto crítico",
        "definition": (
            "La curvatura en las distintas direcciones está determinada por los autovalores de la Hessiana."
        )
    },
    {
        "name": "Direcciones principales",
        "definition": (
            "Direcciones asociadas a autovectores de la Hessiana, donde la función tiene mayor o menor curvatura."
        )
    },

    # ==================================================
    # 11. OPTIMIZACIÓN CON RESTRICCIONES (LAGRANGE)
    # ==================================================

    {
        "name": "Optimización con restricciones",
        "definition": (
            "Busca extremos de f(x,y,...) sujetos a que g(x,y,...) = c. "
            "La solución debe satisfacer tanto f como la restricción."
        )
    },
    {
        "name": "Restricción explícita",
        "definition": (
            "Una restricción donde es posible despejar una variable en función de las otras, "
            "reduciendo la dimensión del problema."
        )
    },
    {
        "name": "Restricción implícita",
        "definition": (
            "Restricción dada por g(x,y)=c donde no es fácil despejar. "
            "Se usa el método de Lagrange."
        )
    },
    {
        "name": "Método de los multiplicadores de Lagrange",
        "definition": (
            "Consiste en resolver ∇f = λ∇g junto con la ecuación de restricción g(x,y)=c. "
            "Los puntos solucionan el sistema de Lagrange."
        )
    },
    {
        "name": "Sistema de Lagrange",
        "definition": (
            "Conjunto de ecuaciones formado por ∇f(x,y)=λ∇g(x,y) y g(x,y)=c."
        )
    },
    {
        "name": "Condición geométrica de Lagrange",
        "definition": (
            "En el punto óptimo, las curvas o superficies de nivel de f y de g son tangentes. "
            "Equivale a que ∇f y ∇g sean paralelos."
        )
    },
    {
        "name": "Interpretación geométrica del multiplicador λ",
        "definition": (
            "λ mide el cambio en el valor óptimo de f respecto a pequeñas variaciones en la restricción g=c."
        )
    },
    {
        "name": "Superficie de restricción",
        "definition": (
            "Conjunto de puntos que satisfacen la condición g(x,y)=c. La búsqueda del extremo se "
            "limita a esta superficie."
        )
    },
    {
        "name": "Curva de restricción",
        "definition": (
            "En ℝ², la restricción g(x,y)=c forma una curva sobre la cual debe encontrarse el extremo."
        )
    },
    {
        "name": "Función objetivo",
        "definition": (
            "La función f que se desea maximizar o minimizar."
        )
    },
    {
        "name": "Multiplicador de Lagrange",
        "definition": (
            "Parámetro λ que aparece en el sistema de Lagrange. Representa la tasa de cambio del valor óptimo "
            "respecto a la restricción."
        )
    },
    {
        "name": "Lagrangiano",
        "definition": (
            "Función auxiliar definida como L(x,y,λ)=f(x,y)+λ(g(x,y)−c). "
            "Sus derivadas parciales generan el sistema de Lagrange."
        )
    },
    {
        "name": "Puntos candidatos a extremos con restricción",
        "definition": (
            "Soluciones del sistema de Lagrange que satisfacen la restricción g=c."
        )
    },
    {
        "name": "Extremos bajo restricciones múltiples",
        "definition": (
            "Si existen varias restricciones g1, g2, ... se introduce un multiplicador λ para cada una."
        )
    },
    {
        "name": "Optimización sobre curvas cerradas",
        "definition": (
            "Para curvas cerradas o compactas, la existencia de extremos está garantizada."
        )
    },
    {
        "name": "Optimización sobre superficies",
        "definition": (
            "Para f(x,y,z) sujeta a g(x,y,z)=c, la superficie de restricción es "
            "bidimensional y debe recorrerse localmente."
        )
    },
    {
        "name": "Extremos condicionados",
        "definition": (
            "Valores máximos o mínimos de f sobre la región definida por la restricción."
        )
    },
    {
        "name": "Método mixto: interior + frontera",
        "definition": (
            "La solución global puede estar en un punto crítico del interior o en la frontera. "
            "Deben analizarse ambos."
        )
    },
    {
        "name": "Regiones factibles",
        "definition": (
            "Conjunto de puntos que satisfacen la restricción. La optimización se limita a esta zona."
        )
    },
    {
        "name": "Interpretación geométrica de ∇f = λ∇g",
        "definition": (
            "Representa paralelismo entre gradientes; las curvas de nivel se tocan sin cruzarse."
        )
    },
    {
        "name": "Restricción activa",
        "definition": (
            "Restricción que se cumple con igualdad en el punto óptimo."
        )
    },
    {
        "name": "Restricción inactiva",
        "definition": (
            "Restricción que no afecta el punto óptimo porque no se cumple con igualdad."
        )
    }

    # ==================================================
    # 12. CURVAS EN EL ESPACIO Y FUNCIONES VECTORIALES
    # ==================================================

    {
        "name": "Función vectorial",
        "definition": (
            "Una función r(t) que asigna a cada valor t un vector en ℝ³. "
            "Describe movimientos, trayectorias o curvas en el espacio."
        )
    },
    {
        "name": "Curva en el espacio",
        "definition": (
            "Conjunto de puntos descritos por r(t) = (x(t), y(t), z(t)) para t en un intervalo."
        )
    },
    {
        "name": "Vector tangente",
        "definition": (
            "El vector r'(t), que indica dirección y velocidad instantánea de la curva en t."
        )
    },
    {
        "name": "Velocidad",
        "definition": (
            "La derivada r'(t). Su magnitud |r'(t)| es la rapidez."
        )
    },
    {
        "name": "Rapidez",
        "definition": (
            "|r'(t)|, la magnitud de la velocidad. Es la rapidez con la que se recorre la curva."
        )
    },
    {
        "name": "Aceleración",
        "definition": (
            "La derivada r''(t). Describe cómo cambia la velocidad con el tiempo."
        )
    },
    {
        "name": "Longitud de arco",
        "definition": (
            "La distancia recorrida a lo largo de una curva: L = ∫ |r'(t)| dt."
        )
    },
    {
        "name": "Parametrización por longitud de arco",
        "definition": (
            "Parámetro s que mide la distancia a lo largo de la curva. Satisface |dr/ds| = 1."
        )
    },
    {
        "name": "Curva regular",
        "definition": (
            "Curva donde r'(t) ≠ 0 para todos los puntos. Garantiza una dirección tangente definida."
        )
    },
    {
        "name": "Curva suave",
        "definition": (
            "Curva cuya derivada r'(t) es continua."
        )
    },
    {
        "name": "Plano osculador",
        "definition": (
            "Plano determinado por los vectores tangente y normal principal. "
            "Es el plano que mejor se ajusta a la curva en un punto."
        )
    },
    {
        "name": "Plano normal",
        "definition": (
            "Plano determinado por los vectores normal principal y binormal. "
            "Es perpendicular al plano osculador."
        )
    },
    {
        "name": "Plano rectificante",
        "definition": (
            "Plano generado por los vectores tangente y binormal. "
            "Describe rotación de la curva alrededor del punto."
        )
    },

    # ==================================================
    # 13. MARCO TNB, CURVATURA Y TORSIÓN
    # ==================================================

    {
        "name": "Marco TNB",
        "definition": (
            "Conjunto de vectores ortogonales {T, N, B} asociados a una curva: "
            "T es el tangente, N el normal principal, B el binormal."
        )
    },
    {
        "name": "Vector tangente unitario T",
        "definition": (
            "T = r'(t) / |r'(t)|. Indica la dirección de la curva."
        )
    },
    {
        "name": "Vector normal principal N",
        "definition": (
            "Normalizado de T'(t). Apunta hacia el centro de curvatura."
        )
    },
    {
        "name": "Vector binormal B",
        "definition": (
            "Producto cruz T × N. Completa el marco ortogonal de la curva."
        )
    },
    {
        "name": "Curvatura κ",
        "definition": (
            "Mide cuánto se curva una curva en un punto. Se define como κ = |dT/ds|."
        )
    },
    {
        "name": "Curvatura en términos de t",
        "definition": (
            "κ = |T'(t)| / |r'(t)|. Útil cuando la curva está parametrizada por t."
        )
    },
    {
        "name": "Centro de curvatura",
        "definition": (
            "Punto del cual la curva se aproxima a un círculo osculador."
        )
    },
    {
        "name": "Radio de curvatura",
        "definition": (
            "R = 1/κ. Indica el radio del círculo que mejor se ajusta a la curva."
        )
    },
    {
        "name": "Círculo osculador",
        "definition": (
            "Círculo con radio 1/κ que mejor aproxima localmente la curva."
        )
    },
    {
        "name": "Torsión τ",
        "definition": (
            "Mide cuánto la curva se desvía del plano osculador. τ = −dB/ds · N."
        )
    },
    {
        "name": "Interpretación geométrica de la torsión",
        "definition": (
            "Describe la 'torsión' o giro tridimensional de la curva fuera del plano osculador."
        )
    },
    {
        "name": "Fórmulas de Frenet–Serret",
        "definition": (
            "Relaciones entre T, N, B, la curvatura κ y la torsión τ:\n"
            "T' = κN,\nN' = −κT + τB,\nB' = −τN."
        )
    },
    {
        "name": "Movimiento en el espacio",
        "definition": (
            "El análisis del movimiento se describe con posición r(t), velocidad r'(t), "
            "y aceleración r''(t)."
        )
    },
    {
        "name": "Aceleración tangencial",
        "definition": (
            "Componente de la aceleración en dirección del vector tangente: a_T = d|v|/dt."
        )
    },
    {
        "name": "Aceleración normal",
        "definition": (
            "Componente de la aceleración perpendicular al movimiento: a_N = κ|v|²."
        )
    },
    {
        "name": "Descomposición de la aceleración",
        "definition": (
            "La aceleración puede expresarse como: a = a_T T + a_N N."
        )
    },
    {
        "name": "Curvatura de una curva plana",
        "definition": (
            "Si la curva está en el plano, se puede calcular mediante κ = |x'y'' − y'x''| / (x'² + y'²)^{3/2}."
        )
    },
    {
        "name": "Curvatura de curvas espaciales",
        "definition": (
            "Para curvas en ℝ³, se calcula usando κ = |r' × r''| / |r'|³."
        )
    },
    {
        "name": "Torsión de una curva espacial",
        "definition": (
            "Se expresa como τ = det(r', r'', r''') / |r' × r''|²."
        )
    },
    {
        "name": "Aplicación física del marco TNB",
        "definition": (
            "Permite describir fuerzas centrípetas, trayectorias de partículas y movimientos curvos."
        )
    },
    {
        "name": "Geometría intrínseca de curvas",
        "definition": (
            "Describe cómo se curva y tuerce la curva independientemente de su parametrización."
        )
    }

    # ==================================================
    # 14. SERIES DE TAYLOR MULTIVARIABLE
    # ==================================================

    {
        "name": "Series de Taylor multivariable",
        "definition": (
            "Extensión de la serie de Taylor a funciones de varias variables. "
            "Permite aproximar f(x,y,...) cerca de un punto usando derivadas parciales."
        )
    },
    {
        "name": "Aproximación de primer orden (lineal)",
        "definition": (
            "f(x,y) ≈ f(a,b) + f_x(a,b)(x−a) + f_y(a,b)(y−b). "
            "Es la versión multivariable de la recta tangente."
        )
    },
    {
        "name": "Aproximación de segundo orden (cuadrática)",
        "definition": (
            "Incluye términos de segundo grado: "
            "½[f_xx h² + 2 f_xy h k + f_yy k²], donde h=x−a y k=y−b."
        )
    },
    {
        "name": "Hessiana en la expansión de Taylor",
        "definition": (
            "La parte cuadrática usa la matriz Hessiana Hf(a,b) para construir la forma cuadrática."
        )
    },
    {
        "name": "Resto de Taylor",
        "definition": (
            "Término que mide el error entre la función exacta y la aproximación polinómica."
        )
    },
    {
        "name": "Expansión alrededor de un punto",
        "definition": (
            "Serie escrita en términos de h=x−a, k=y−b. Permite expresar la función localmente."
        )
    },
    {
        "name": "Interpretación geométrica del segundo orden",
        "definition": (
            "Indica cómo la superficie se curva cerca del punto. "
            "Se relaciona con clasificación de extremos usando la Hessiana."
        )
    },
    {
        "name": "Series de Taylor para f(x,y,z)",
        "definition": (
            "La expansión incluye términos lineales, cuadráticos y cúbicos, construidos a partir "
            "de derivadas parciales de orden superior."
        )
    },
    {
        "name": "Polinomio de Taylor",
        "definition": (
            "El polinomio que aproxima a la función. Depende del orden deseado (1, 2, 3,...)."
        )
    },
    {
        "name": "Uso de Taylor en optimización",
        "definition": (
            "La expansión de segundo orden describe la curvatura local, útil para clasificar puntos críticos."
        )
    },

    # ==================================================
    # 15. DIFERENCIALES TOTALES Y APROXIMACIONES
    # ==================================================

    {
        "name": "Diferencial total",
        "definition": (
            "df = f_x dx + f_y dy. Describe cómo cambia f debido a pequeños cambios en x e y."
        )
    },
    {
        "name": "Interpretación geométrica del diferencial",
        "definition": (
            "df evalúa la pendiente del plano tangente como aproximación de los cambios en la función."
        )
    },
    {
        "name": "Error de aproximación lineal",
        "definition": (
            "Error = f(x,y) − [f(a,b) + f_x(a,b)h + f_y(a,b)k]. "
            "Mide qué tan precisa es la aproximación lineal."
        )
    },
    {
        "name": "Aproximación lineal",
        "definition": (
            "L(x,y) = f(a,b) + f_x(a,b)(x−a) + f_y(a,b)(y−b). "
            "Se usa para aproximar valores cercanos al punto base."
        )
    },
    {
        "name": "Cambio relativo",
        "definition": (
            "dr = df / f(a,b). Representa el error proporcional al valor inicial."
        )
    },
    {
        "name": "Cambio absoluto",
        "definition": (
            "df, que mide el cambio total en la función debido a variaciones pequeñas."
        )
    },
    {
        "name": "Linealización",
        "definition": (
            "Proceso de reemplazar una función complicada por su plano tangente para simplificar cálculos."
        )
    },
    {
        "name": "Mejor aproximación cuadrática",
        "definition": (
            "El polinomio de Taylor de segundo orden da una aproximación mejor que la lineal, "
            "especialmente si la superficie tiene curvatura significativa."
        )
    },
    {
        "name": "Aplicaciones del diferencial total",
        "definition": (
            "Útil en propagación de errores, estimaciones y análisis de sensibilidad."
        )
    },
    {
        "name": "Propagación de errores",
        "definition": (
            "Usa diferenciales para estimar la incertidumbre en una función que depende de variables medidas "
            "con error."
        )
    },
    {
        "name": "Sensibilidad de una función",
        "definition": (
            "El tamaño de df indica qué tan sensible es f ante pequeños cambios en sus entradas."
        )
    }


# ==================================================
# INTERFAZ: SELECTBOX TIPO DICCIONARIO
# ==================================================

nombres = [c["name"] for c in CONCEPTOS]
seleccion = st.selectbox("Selecciona un término", nombres)

concepto = next(c for c in CONCEPTOS if c["name"] == seleccion)

st.markdown("### Concepto")
st.write(concepto["definition"])
