
import streamlit as st
import random
import re

# =====================================================
# CONFIGURACIÓN
# =====================================================

st.set_page_config(
    page_title="LinguaPath | Aprende inglés",
    page_icon="🌍",
    layout="wide"
)

# =====================================================
# DISEÑO
# =====================================================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800;900&display=swap');

html, body, [class*="css"] {
    font-family: 'Nunito', sans-serif;
}

.stApp {
    background: #F5F7FC;
}

.block-container {
    max-width: 1150px;
    padding-top: 2rem;
}

.hero {
    background: linear-gradient(120deg, #172554, #354FC0, #7666E8);
    padding: 35px;
    border-radius: 22px;
    color: white;
    margin-bottom: 25px;
}

.hero h1 {
    font-size: 38px;
    font-weight: 900;
}

.hero p {
    color: #E0E7FF;
    font-size: 16px;
}

.card {
    background: white;
    padding: 23px;
    border-radius: 18px;
    border: 1px solid #E6EAF2;
    margin-bottom: 15px;
}

.word {
    font-size: 36px;
    font-weight: 900;
    color: #354FC0;
    text-align: center;
}

.translation {
    text-align: center;
    font-size: 19px;
    color: #64748B;
}

div.stButton > button {
    border-radius: 12px;
    font-weight: 700;
    min-height: 43px;
}

h1, h2, h3 {
    color: #24345D;
}
</style>
""", unsafe_allow_html=True)


# =====================================================
# NIVELES
# =====================================================

NIVELES = {
    "A1": {
        "nombre": "Principiante",
        "descripcion": "Aprende las bases del inglés.",
        "objetivo": "Presentarte, saludar y utilizar expresiones sencillas.",
        "emoji": "🟢"
    },
    "A2": {
        "nombre": "Elemental",
        "descripcion": "Construye conversaciones sencillas.",
        "objetivo": "Hablar de experiencias, rutinas y planes.",
        "emoji": "🟢"
    },
    "B1": {
        "nombre": "Intermedio",
        "descripcion": "Comunícate en situaciones cotidianas.",
        "objetivo": "Expresar opiniones y desenvolverte al viajar.",
        "emoji": "🔵"
    },
    "B2": {
        "nombre": "Intermedio alto",
        "descripcion": "Expresa ideas más complejas.",
        "objetivo": "Argumentar y mantener conversaciones fluidas.",
        "emoji": "🔵"
    },
    "C1": {
        "nombre": "Avanzado",
        "descripcion": "Domina estructuras avanzadas.",
        "objetivo": "Comunicarte en contextos académicos y profesionales.",
        "emoji": "🟣"
    },
    "C2": {
        "nombre": "Maestría",
        "descripcion": "Alcanza un dominio muy avanzado.",
        "objetivo": "Comprender matices y expresarte con precisión.",
        "emoji": "🟣"
    }
}


# =====================================================
# LECCIONES
# =====================================================

LECCIONES = {

"A1": [
    {
        "titulo": "Saludos y presentaciones",
        "tipo": "Vocabulario",
        "explicacion": """
Los saludos permiten iniciar una conversación.

Para presentarte puedes utilizar:

**My name is...** = Mi nombre es...

**I am...** = Yo soy...

**Nice to meet you** = Mucho gusto.
""",
        "ejemplos": [
            ("Hello!", "¡Hola!"),
            ("Good morning.", "Buenos días."),
            ("My name is Ana.", "Me llamo Ana."),
            ("Nice to meet you.", "Mucho gusto.")
        ]
    },
    {
        "titulo": "Verbo TO BE",
        "tipo": "Gramática",
        "explicacion": """
El verbo TO BE significa ser o estar.

Sus formas principales son:

- I am
- You are
- He / She / It is
- We / They are
""",
        "ejemplos": [
            ("I am a student.", "Soy estudiante."),
            ("She is happy.", "Ella está feliz."),
            ("They are friends.", "Ellos son amigos.")
        ]
    },
    {
        "titulo": "Números y edad",
        "tipo": "Vocabulario",
        "explicacion": """
Para expresar la edad utilizamos el verbo TO BE.

**How old are you?** = ¿Cuántos años tienes?

**I am twenty years old.** = Tengo veinte años.
""",
        "ejemplos": [
            ("One", "Uno"),
            ("Two", "Dos"),
            ("Ten", "Diez"),
            ("Twenty", "Veinte")
        ]
    },
    {
        "titulo": "Artículos A y AN",
        "tipo": "Gramática",
        "explicacion": """
Utilizamos A y AN para hablar de algo en singular.

- A: antes de un sonido consonántico.
- AN: antes de un sonido vocálico.
""",
        "ejemplos": [
            ("A book", "Un libro"),
            ("An apple", "Una manzana"),
            ("A car", "Un automóvil")
        ]
    },
    {
        "titulo": "Rutina diaria",
        "tipo": "Expresiones",
        "explicacion": """
Utilizamos el presente simple para hablar de nuestras rutinas.

Con HE, SHE e IT normalmente añadimos S al verbo.
""",
        "ejemplos": [
            ("I wake up at seven.", "Me despierto a las siete."),
            ("She studies English.", "Ella estudia inglés."),
            ("I go to university.", "Voy a la universidad.")
        ]
    }
],

"A2": [
    {
        "titulo": "Present Simple",
        "tipo": "Gramática",
        "explicacion": """
Utilizamos el presente simple para expresar hábitos y rutinas.

Ejemplo:

I study every day.

She works in a hospital.
""",
        "ejemplos": [
            ("I play football.", "Juego fútbol."),
            ("She reads books.", "Ella lee libros."),
            ("We study English.", "Estudiamos inglés.")
        ]
    },
    {
        "titulo": "Present Continuous",
        "tipo": "Gramática",
        "explicacion": """
Se utiliza para acciones que están ocurriendo ahora.

Estructura:

AM / IS / ARE + verbo terminado en ING.
""",
        "ejemplos": [
            ("I am studying.", "Estoy estudiando."),
            ("She is cooking.", "Ella está cocinando."),
            ("They are playing.", "Ellos están jugando.")
        ]
    },
    {
        "titulo": "Pasado simple",
        "tipo": "Gramática",
        "explicacion": """
El pasado simple describe acciones que terminaron.

Los verbos regulares suelen terminar en ED.
Los irregulares cambian de forma.
""",
        "ejemplos": [
            ("I watched a movie.", "Vi una película."),
            ("She went home.", "Ella fue a casa."),
            ("We visited Quito.", "Visitamos Quito.")
        ]
    },
    {
        "titulo": "Comparativos",
        "tipo": "Gramática",
        "explicacion": """
Utilizamos comparativos para comparar dos cosas.

- Taller than = Más alto que.
- More expensive than = Más caro que.
- Better than = Mejor que.
""",
        "ejemplos": [
            ("My house is bigger.", "Mi casa es más grande."),
            ("She is taller than me.", "Ella es más alta que yo."),
            ("This is better.", "Esto es mejor.")
        ]
    },
    {
        "titulo": "Planes futuros",
        "tipo": "Gramática",
        "explicacion": """
GOING TO expresa planes e intenciones.

WILL se utiliza para decisiones espontáneas y predicciones.
""",
        "ejemplos": [
            ("I am going to travel.", "Voy a viajar."),
            ("It will rain.", "Lloverá."),
            ("I will help you.", "Te ayudaré.")
        ]
    }
],

"B1": [
    {
        "titulo": "Present Perfect",
        "tipo": "Gramática",
        "explicacion": """
Se forma con HAVE / HAS + participio.

Se utiliza para hablar de experiencias y acciones relacionadas con el presente.
""",
        "ejemplos": [
            ("I have visited Peru.", "He visitado Perú."),
            ("She has finished.", "Ella ha terminado."),
            ("Have you eaten?", "¿Has comido?")
        ]
    },
    {
        "titulo": "Dar opiniones",
        "tipo": "Comunicación",
        "explicacion": """
Estas expresiones ayudan a comunicar opiniones:

- In my opinion = En mi opinión.
- I believe = Creo.
- I agree = Estoy de acuerdo.
- I disagree = No estoy de acuerdo.
""",
        "ejemplos": [
            ("I think English is important.", "Creo que el inglés es importante."),
            ("I agree with you.", "Estoy de acuerdo contigo.")
        ]
    },
    {
        "titulo": "Conectores",
        "tipo": "Escritura",
        "explicacion": """
Los conectores unen ideas y permiten escribir mejor.

- However = Sin embargo.
- Therefore = Por lo tanto.
- Although = Aunque.
- Furthermore = Además.
""",
        "ejemplos": [
            ("I was tired. However, I studied.", "Estaba cansada. Sin embargo, estudié."),
            ("It was raining. Therefore, we stayed home.", "Llovía. Por lo tanto, nos quedamos en casa.")
        ]
    },
    {
        "titulo": "First Conditional",
        "tipo": "Gramática",
        "explicacion": """
Se utiliza para situaciones futuras posibles.

Estructura:

IF + PRESENT SIMPLE + WILL + VERBO.
""",
        "ejemplos": [
            ("If it rains, I will stay home.", "Si llueve, me quedaré en casa."),
            ("If you study, you will improve.", "Si estudias, mejorarás.")
        ]
    },
    {
        "titulo": "Inglés para viajar",
        "tipo": "Vocabulario",
        "explicacion": """
Aprende expresiones útiles para viajar al extranjero.
""",
        "ejemplos": [
            ("Where is the airport?", "¿Dónde está el aeropuerto?"),
            ("I need a hotel.", "Necesito un hotel."),
            ("Could you help me?", "¿Podría ayudarme?")
        ]
    }
],

"B2": [
    {
        "titulo": "Second Conditional",
        "tipo": "Gramática",
        "explicacion": """
Se utiliza para situaciones hipotéticas.

IF + PAST SIMPLE + WOULD + VERBO.
""",
        "ejemplos": [
            ("If I had money, I would travel.", "Si tuviera dinero, viajaría."),
            ("If I were you, I would study.", "Si fuera tú, estudiaría.")
        ]
    },
    {
        "titulo": "Third Conditional",
        "tipo": "Gramática",
        "explicacion": """
Habla de situaciones imaginarias del pasado.

IF + PAST PERFECT + WOULD HAVE + PARTICIPIO.
""",
        "ejemplos": [
            ("If I had studied, I would have passed.", "Si hubiera estudiado, habría aprobado.")
        ]
    },
    {
        "titulo": "Phrasal Verbs",
        "tipo": "Vocabulario",
        "explicacion": """
Son combinaciones de verbos y partículas que tienen significados propios.
""",
        "ejemplos": [
            ("Give up", "Rendirse"),
            ("Find out", "Averiguar"),
            ("Look after", "Cuidar"),
            ("Carry on", "Continuar")
        ]
    },
    {
        "titulo": "Voz pasiva",
        "tipo": "Gramática",
        "explicacion": """
Se utiliza cuando queremos destacar la acción y no quién la realiza.

Estructura: BE + PAST PARTICIPLE.
""",
        "ejemplos": [
            ("The bridge was built in 1990.", "El puente fue construido en 1990."),
            ("English is spoken worldwide.", "El inglés se habla mundialmente.")
        ]
    },
    {
        "titulo": "Collocations",
        "tipo": "Vocabulario",
        "explicacion": """
Son combinaciones de palabras que aparecen juntas de manera natural.
""",
        "ejemplos": [
            ("Make a decision", "Tomar una decisión"),
            ("Heavy rain", "Lluvia intensa"),
            ("Strong argument", "Argumento sólido")
        ]
    }
],

"C1": [
    {
        "titulo": "Inversion",
        "tipo": "Gramática avanzada",
        "explicacion": """
En inglés formal podemos invertir el orden del sujeto y el auxiliar para dar énfasis.
""",
        "ejemplos": [
            ("Never have I seen this.", "Nunca había visto esto."),
            ("Rarely do we get this opportunity.", "Rara vez tenemos esta oportunidad.")
        ]
    },
    {
        "titulo": "Academic English",
        "tipo": "Comunicación",
        "explicacion": """
Aprende expresiones para comunicar ideas en contextos académicos.
""",
        "ejemplos": [
            ("The evidence indicates...", "La evidencia indica..."),
            ("This may suggest...", "Esto podría sugerir..."),
            ("In contrast...", "En contraste...")
        ]
    },
    {
        "titulo": "Hedging",
        "tipo": "Comunicación",
        "explicacion": """
Permite expresar afirmaciones con cautela y evitar sonar demasiado absoluto.
""",
        "ejemplos": [
            ("It appears that...", "Parece que..."),
            ("To some extent...", "Hasta cierto punto."),
            ("It may be possible...", "Puede que sea posible.")
        ]
    },
    {
        "titulo": "Idioms",
        "tipo": "Vocabulario",
        "explicacion": """
Son expresiones cuyo significado no siempre puede deducirse literalmente.
""",
        "ejemplos": [
            ("Once in a blue moon", "Muy de vez en cuando."),
            ("Break the ice", "Romper el hielo."),
            ("Get the ball rolling", "Poner algo en marcha.")
        ]
    },
    {
        "titulo": "Ensayos académicos",
        "tipo": "Escritura",
        "explicacion": """
Un ensayo académico presenta una tesis, argumentos y una conclusión.
""",
        "ejemplos": [
            ("Furthermore", "Además."),
            ("Consequently", "En consecuencia."),
            ("In conclusion", "En conclusión.")
        ]
    }
],

"C2": [
    {
        "titulo": "Ironía y significado implícito",
        "tipo": "Comprensión",
        "explicacion": """
La ironía comunica algo diferente de lo que expresan literalmente las palabras.

El contexto y el tono son fundamentales.
""",
        "ejemplos": [
            ("That's just wonderful!", "¡Qué maravilloso! (puede ser irónico).")
        ]
    },
    {
        "titulo": "Precisión léxica",
        "tipo": "Vocabulario",
        "explicacion": """
Aprende palabras avanzadas y sus diferencias de significado.
""",
        "ejemplos": [
            ("Meticulous", "Minucioso."),
            ("Reluctant", "Reacio."),
            ("Compelling", "Convincente."),
            ("Ambiguous", "Ambiguo.")
        ]
    },
    {
        "titulo": "Conectores avanzados",
        "tipo": "Escritura",
        "explicacion": """
Permiten construir argumentos sofisticados y expresar concesiones.
""",
        "ejemplos": [
            ("Admittedly", "Es cierto que."),
            ("Nevertheless", "No obstante."),
            ("Notwithstanding", "A pesar de.")
        ]
    },
    {
        "titulo": "Análisis de textos",
        "tipo": "Comprensión",
        "explicacion": """
Analiza el tono, intención y postura del autor.
""",
        "ejemplos": [
            ("The author implies...", "El autor da a entender..."),
            ("The tone is critical.", "El tono es crítico.")
        ]
    },
    {
        "titulo": "Paraphrasing",
        "tipo": "Escritura",
        "explicacion": """
Consiste en expresar una idea utilizando estructuras y palabras diferentes, sin cambiar su significado.
""",
        "ejemplos": [
            ("The results were unexpected.", "The findings differed from expectations.")
        ]
    }
]
}


# =====================================================
# PREGUNTAS DE PRÁCTICA
# =====================================================

QUIZ = {
"A1": [
    ("___ name is Laura.", ["My", "Me", "I"], 0, "My name significa mi nombre."),
    ("He ___ a teacher.", ["am", "is", "are"], 1, "Con HE utilizamos IS."),
    ("___ apple.", ["A", "An", "The"], 1, "Apple comienza con sonido vocálico."),
    ("Buenos días:", ["Good night", "Good morning", "Goodbye"], 1, "Good morning significa buenos días."),
    ("She ___ happy.", ["are", "am", "is"], 2, "Con SHE utilizamos IS.")
],
"A2": [
    ("Yesterday, I ___ a movie.", ["watch", "watched", "watching"], 1, "Yesterday indica pasado."),
    ("Look! It ___.", ["rains", "is raining", "rain"], 1, "Está ocurriendo ahora."),
    ("She is ___ than me.", ["tall", "taller", "tallest"], 1, "Utilizamos taller than."),
    ("I ___ travel tomorrow.", ["am going to", "going", "am"], 0, "Going to expresa planes."),
    ("I have ___ finished.", ["already", "never", "yet"], 0, "Already significa ya.")
],
"B1": [
    ("I have ___ to Peru.", ["go", "been", "going"], 1, "Have + participio."),
    ("If it rains, I ___ home.", ["will stay", "stayed", "would stayed"], 0, "First conditional."),
    ("___, we continued.", ["However", "Because", "Although"], 0, "However expresa contraste."),
    ("She ___ here since 2022.", ["has lived", "live", "living"], 0, "Since suele utilizar present perfect."),
    ("Which expresses an opinion?", ["In my opinion", "Last Monday", "At home"], 0, "Significa en mi opinión.")
],
"B2": [
    ("If I ___ rich, I would travel.", ["am", "were", "will be"], 1, "Second conditional."),
    ("The bridge ___ in 1990.", ["built", "was built", "building"], 1, "Voz pasiva."),
    ("Give up means:", ["Continue", "Surrender", "Discover"], 1, "Significa rendirse."),
    ("Make a ___.", ["decision", "deciding", "decide"], 0, "Make a decision."),
    ("If I had studied, I ___ passed.", ["would have", "will have", "would"], 0, "Third conditional.")
],
"C1": [
    ("___ have I seen this.", ["Never", "No", "Not"], 0, "Never introduce inversión."),
    ("This ___ suggest...", ["may", "must definitely", "always"], 0, "May expresa cautela."),
    ("Which is more formal?", ["Request", "Get", "Grab"], 0, "Request es formal."),
    ("An essay needs a clear ___.", ["thesis", "joke", "story"], 0, "La tesis presenta la idea principal."),
    ("Meticulous means:", ["Careless", "Very detailed", "Quick"], 1, "Significa minucioso.")
],
"C2": [
    ("Reluctant means:", ["Eager", "Unwilling", "Certain"], 1, "Significa reacio."),
    ("Which expresses concession?", ["Admittedly", "For example", "Therefore"], 0, "Admittedly reconoce un punto."),
    ("Compelling means:", ["Persuasive", "Unclear", "Irrelevant"], 0, "Significa convincente."),
    ("A paraphrase should:", ["Change the meaning", "Preserve the meaning", "Copy everything"], 1, "Debe mantener el significado."),
    ("Ambiguous means:", ["Clear", "Having more than one possible meaning", "Simple"], 1, "Significa ambiguo.")
]
}


# =====================================================
# VOCABULARIO
# =====================================================

VOCABULARIO = {
"A1": [
    ("Apple", "Manzana"),
    ("House", "Casa"),
    ("Water", "Agua"),
    ("Book", "Libro"),
    ("Friend", "Amigo"),
    ("School", "Escuela"),
    ("Family", "Familia"),
    ("Food", "Comida"),
    ("Happy", "Feliz"),
    ("Today", "Hoy")
],
"A2": [
    ("Usually", "Normalmente"),
    ("Sometimes", "A veces"),
    ("Healthy", "Saludable"),
    ("Expensive", "Caro"),
    ("Journey", "Viaje"),
    ("Weather", "Clima"),
    ("Borrow", "Pedir prestado"),
    ("Arrive", "Llegar"),
    ("Neighbour", "Vecino"),
    ("Improve", "Mejorar")
],
"B1": [
    ("Achievement", "Logro"),
    ("Advice", "Consejo"),
    ("Although", "Aunque"),
    ("Opportunity", "Oportunidad"),
    ("Reliable", "Confiable"),
    ("Experience", "Experiencia"),
    ("Avoid", "Evitar"),
    ("Afford", "Poder permitirse"),
    ("Environment", "Medioambiente"),
    ("Develop", "Desarrollar")
],
"B2": [
    ("Accurate", "Preciso"),
    ("Challenge", "Desafío"),
    ("Efficient", "Eficiente"),
    ("Enhance", "Mejorar"),
    ("Outcome", "Resultado"),
    ("Requirement", "Requisito"),
    ("Widespread", "Generalizado"),
    ("Despite", "A pesar de"),
    ("Considerable", "Considerable"),
    ("Furthermore", "Además")
],
"C1": [
    ("Subtle", "Sutil"),
    ("Thorough", "Exhaustivo"),
    ("Undermine", "Debilitar"),
    ("Noteworthy", "Destacable"),
    ("Plausible", "Verosímil"),
    ("Convey", "Transmitir"),
    ("Inevitable", "Inevitable"),
    ("Ambiguous", "Ambiguo"),
    ("Compelling", "Convincente"),
    ("Whereas", "Mientras que")
],
"C2": [
    ("Albeit", "Aunque"),
    ("Eloquent", "Elocuente"),
    ("Reluctant", "Reacio"),
    ("Meticulous", "Minucioso"),
    ("Pragmatic", "Pragmático"),
    ("Scrutiny", "Escrutinio"),
    ("Resilient", "Resiliente"),
    ("Nuance", "Matiz"),
    ("Counterintuitive", "Contraintuitivo"),
    ("Undoubtedly", "Indudablemente")
]
}


# =====================================================
# READING
# =====================================================

READING = {
"A1": (
    "A Day at School",
    "My name is Emma. I am a student. I wake up at seven. I have breakfast and go to school by bus. I like English because it is fun.",
    "What time does Emma wake up?",
    ["At six", "At seven", "At eight"],
    1
),
"A2": (
    "A Weekend Trip",
    "Last weekend, Daniel visited a small town with his family. They travelled by car and stayed in a hotel near the beach. They enjoyed the local food.",
    "Where did Daniel stay?",
    ["In a hotel", "At school", "At home"],
    0
),
"B1": (
    "Learning a New Skill",
    "Sofia wanted to learn how to cook. At first, she made many mistakes. However, she practised every weekend. After a few months, she became more confident.",
    "What helped Sofia improve?",
    ["Buying equipment", "Practising consistently", "Watching television"],
    1
),
"B2": (
    "Urban Transport",
    "Many cities are investing in public transport, cycling infrastructure and walkable neighbourhoods. These changes can reduce traffic and pollution, but they require long-term planning.",
    "What do these changes require?",
    ["Long-term planning", "More private cars", "Less public transport"],
    0
),
"C1": (
    "The Value of Attention",
    "Complex tasks often require uninterrupted periods of concentration. Collaboration is also valuable, but organisations should distinguish between tasks that benefit from interaction and those that require individual focus.",
    "What distinction does the author recommend?",
    ["Between tasks requiring interaction and concentration", "Between employees", "Between cities"],
    0
),
"C2": (
    "The Limits of Measurement",
    "Metrics can reveal useful patterns, but their apparent precision can encourage misplaced confidence. A number should not be treated as the complete representation of a complex situation.",
    "What is the main warning?",
    ["All measurements are useless", "Numbers explain everything", "Metrics can be misleading"],
    2
)
}


# =====================================================
# ESTADO DE LA APLICACIÓN
# =====================================================

defaults = {
    "xp": 0,
    "completadas": [],
    "nivel": "A1",
    "indice": 0,
    "aprendidas": [],
    "resultados": {}
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value


def ganar_xp(cantidad):
    st.session_state.xp += cantidad


def completar(actividad, puntos=10):
    if actividad not in st.session_state.completadas:
        st.session_state.completadas.append(actividad)
        ganar_xp(puntos)


# =====================================================
# MENÚ LATERAL
# =====================================================

with st.sidebar:

    st.markdown("# 🌍 LinguaPath")
    st.caption("Your English learning journey")

    pagina = st.radio(
        "MENÚ PRINCIPAL",
        [
            "🏠 Inicio",
            "📚 Lecciones",
            "🧠 Practicar",
            "🃏 Vocabulario",
            "📖 Reading",
            "✍️ Writing",
            "📈 Mi progreso"
        ]
    )

    st.divider()

    st.markdown("### Tu nivel")

    nivel = st.selectbox(
        "Selecciona tu nivel",
        list(NIVELES.keys()),
        index=list(NIVELES.keys()).index(st.session_state.nivel)
    )

    if nivel != st.session_state.nivel:
        st.session_state.nivel = nivel
        st.session_state.indice = 0
        st.rerun()

    st.markdown(f"**{NIVELES[nivel]['emoji']} {nivel} - {NIVELES[nivel]['nombre']}**")

    st.progress(min(st.session_state.xp % 100, 100) / 100)

    st.caption(f"⭐ {st.session_state.xp} XP acumulados")


nivel = st.session_state.nivel
datos = NIVELES[nivel]


# =====================================================
# CABECERA
# =====================================================

def cabecera(titulo, descripcion):
    st.markdown(
        f"""
        <div class="hero">
            <h1>{titulo}</h1>
            <p>{descripcion}</p>
        </div>
        """,
        unsafe_allow_html=True
    )


# =====================================================
# INICIO
# =====================================================

if pagina == "🏠 Inicio":

    cabecera(
        "¡Bienvenida a LinguaPath! 🌍",
        "Aprende inglés a tu ritmo y alcanza tus metas."
    )

    c1, c2, c3 = st.columns(3)

    c1.metric("⭐ Experiencia", st.session_state.xp)
    c2.metric("✅ Actividades", len(st.session_state.completadas))
    c3.metric("🎯 Nivel actual", nivel)

    st.write("")

    izquierda, derecha = st.columns([1.4, 1])

    with izquierda:

        st.markdown('<div class="card">', unsafe_allow_html=True)

        st.subheader(f"{datos['emoji']} {nivel} - {datos['nombre']}")

        st.write(datos["descripcion"])

        st.info("**Tu objetivo:** " + datos["objetivo"])

        st.markdown("### ¿Qué aprenderás?")

        st.write("""
        - Gramática y estructuras.
        - Vocabulario y expresiones.
        - Comprensión lectora.
        - Escritura en inglés.
        - Ejercicios y desafíos.
        """)

        st.markdown('</div>', unsafe_allow_html=True)

        if st.button("🚀 Comenzar a aprender", type="primary"):
            st.success("¡Excelente! Selecciona Lecciones en el menú lateral.")

    with derecha:

        st.markdown('<div class="card">', unsafe_allow_html=True)

        st.subheader("🗺️ Tu camino")

        for codigo, info in NIVELES.items():

            actual = " ← Nivel seleccionado" if codigo == nivel else ""

            st.markdown(
                f"**{info['emoji']} {codigo} - {info['nombre']}**{actual}"
            )

            st.caption(info["descripcion"])

        st.markdown('</div>', unsafe_allow_html=True)

    st.info("Consejo: dedica un poco de tiempo al inglés cada día.")


# =====================================================
# LECCIONES
# =====================================================

elif pagina == "📚 Lecciones":

    cabecera(
        "Tus lecciones 📚",
        f"Aprende nuevos conocimientos en el nivel {nivel}."
    )

    lecciones = LECCIONES[nivel]

    indice = st.selectbox(
        "Selecciona una lección",
        range(len(lecciones)),
        format_func=lambda i: f"{i+1}. {lecciones[i]['titulo']}"
    )

    leccion = lecciones[indice]

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.caption(leccion["tipo"].upper())

    st.title(leccion["titulo"])

    st.markdown(leccion["explicacion"])

    st.divider()

    st.subheader("Ejemplos")

    for ingles, espanol in leccion["ejemplos"]:

        a, b = st.columns(2)

        a.markdown(f"**{ingles}**")
        b.write(espanol)

    st.markdown('</div>', unsafe_allow_html=True)

    clave = f"{nivel}-leccion-{indice}"

    if clave in st.session_state.completadas:

        st.success("¡Ya completaste esta lección!")

    elif st.button("✅ Marcar como completada", type="primary"):

        completar(clave, 15)

        st.success("¡Muy bien! Has ganado 15 XP.")

        st.rerun()

    st.progress(
        (indice + 1) / len(lecciones),
        text=f"Lección {indice+1} de {len(lecciones)}"
    )


# =====================================================
# PRÁCTICA
# =====================================================

elif pagina == "🧠 Practicar":

    cabecera(
        "Zona de práctica 🧠",
        "Demuestra lo que has aprendido."
    )

    preguntas = QUIZ[nivel]

    modo = st.radio(
        "Selecciona el modo",
        ["Quiz completo", "Reto rápido"],
        horizontal=True
    )

    if modo == "Reto rápido":

        numero = st.selectbox(
            "Selecciona una pregunta",
            range(len(preguntas)),
            format_func=lambda i: f"Pregunta {i+1}"
        )

        preguntas_actuales = [preguntas[numero]]
        clave = f"{nivel}-rapido-{numero}"

    else:

        preguntas_actuales = preguntas
        clave = f"{nivel}-quiz"

    respuestas = []

    for i, pregunta in enumerate(preguntas_actuales):

        enunciado, opciones, correcta, explicacion = pregunta

        st.markdown('<div class="card">', unsafe_allow_html=True)

        st.markdown(f"### {i+1}. {enunciado}")

        respuesta = st.radio(
            "Selecciona una respuesta:",
            opciones,
            key=f"{clave}-{i}"
        )

        respuestas.append(
            (respuesta, opciones, correcta, explicacion)
        )

        st.markdown('</div>', unsafe_allow_html=True)

    if st.button("Comprobar respuestas", type="primary"):

        puntos = 0

        for respuesta, opciones, correcta, explicacion in respuestas:

            if opciones.index(respuesta) == correcta:
                puntos += 1

        st.session_state.resultados[clave] = (
            puntos,
            len(respuestas),
            [
                (opciones[correcta], explicacion)
                for respuesta, opciones, correcta, explicacion in respuestas
            ]
        )

        completar(clave, 20)

        st.rerun()

    if clave in st.session_state.resultados:

        puntos, total, explicaciones = st.session_state.resultados[clave]

        st.subheader(f"Resultado: {puntos}/{total}")

        st.progress(puntos / total)

        if puntos == total:
            st.success("¡Excelente! Todas tus respuestas son correctas.")

        elif puntos >= total / 2:
            st.info("¡Buen trabajo! Sigue practicando.")

        else:
            st.warning("Repasa las lecciones y vuelve a intentarlo.")

        st.markdown("### Respuestas correctas")

        for i, (respuesta, explicacion) in enumerate(explicaciones):

            st.write(f"**{i+1}. {respuesta}**")
            st.caption(explicacion)

        if st.button("Volver a practicar"):

            del st.session_state.resultados[clave]

            st.rerun()


# =====================================================
# VOCABULARIO
# =====================================================

elif pagina == "🃏 Vocabulario":

    cabecera(
        "Tarjetas de vocabulario 🃏",
        "Aprende nuevas palabras y memoriza sus significados."
    )

    palabras = VOCABULARIO[nivel]

    indice = st.session_state.indice % len(palabras)

    ingles, espanol = palabras[indice]

    st.caption(f"TARJETA {indice+1} DE {len(palabras)}")

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.markdown(
        f'<div class="word">{ingles}</div>',
        unsafe_allow_html=True
    )

    mostrar = st.toggle(
        "Mostrar traducción",
        key=f"traduccion-{nivel}-{indice}"
    )

    if mostrar:

        st.markdown(
            f'<div class="translation">{espanol}</div>',
            unsafe_allow_html=True
        )

    else:

        st.caption("Intenta recordar el significado antes de revelarlo.")

    st.markdown('</div>', unsafe_allow_html=True)

    a, b, c = st.columns(3)

    with a:

        if st.button("⬅ Anterior", use_container_width=True):

            st.session_state.indice = (indice - 1) % len(palabras)

            st.rerun()

    with b:

        if st.button("Repasar", use_container_width=True):

            st.session_state.indice = (indice + 1) % len(palabras)

            st.rerun()

    with c:

        if st.button("Ya la sé ✓", type="primary", use_container_width=True):

            if ingles not in st.session_state.aprendidas:

                st.session_state.aprendidas.append(ingles)

                ganar_xp(2)

            st.session_state.indice = (indice + 1) % len(palabras)

            st.rerun()

    st.write("")

    aprendidas_nivel = [
        palabra for palabra in st.session_state.aprendidas
        if palabra in [p[0] for p in palabras]
    ]

    st.metric("Palabras aprendidas", len(aprendidas_nivel))

    st.progress(len(aprendidas_nivel) / len(palabras))


# =====================================================
# READING
# =====================================================

elif pagina == "📖 Reading":

    cabecera(
        "Reading 📖",
        "Desarrolla tu comprensión lectora en inglés."
    )

    titulo, texto, pregunta, opciones, correcta = READING[nivel]

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.caption(f"LECTURA · NIVEL {nivel}")

    st.subheader(titulo)

    st.write(texto)

    st.markdown('</div>', unsafe_allow_html=True)

    respuesta = st.radio(pregunta, opciones, key=f"reading-{nivel}")

    if st.button("Comprobar comprensión", type="primary"):

        if opciones.index(respuesta) == correcta:

            st.success("¡Correcto! Has comprendido el texto.")

            completar(f"reading-{nivel}", 15)

        else:

            st.error("Respuesta incorrecta. Vuelve a leer el texto.")

            st.info(f"La respuesta correcta es: {opciones[correcta]}")


# =====================================================
# WRITING
# =====================================================

elif pagina == "✍️ Writing":

    cabecera(
        "Writing ✍️",
        "Practica tu escritura y desarrolla tu capacidad de expresión."
    )

    RETOS = {
        "A1": "Write 4 sentences introducing yourself.",
        "A2": "Write a paragraph about your daily routine.",
        "B1": "Write about a memorable trip or experience.",
        "B2": "Give your opinion about learning languages.",
        "C1": "Discuss how technology can improve education.",
        "C2": "Discuss the advantages and limitations of measuring progress."
    }

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("Tu actividad")

    st.write(RETOS[nivel])
    st.markdown("**Consejo:** utiliza conectores para organizar tus ideas.")

    st.markdown('</div>', unsafe_allow_html=True)

    texto = st.text_area(
        "Escribe tu respuesta en inglés:",
        height=220,
        placeholder="Start writing here..."
    )

    if st.button("Revisar mi escritura", type="primary"):

        if len(texto.strip().split()) < 8:

            st.warning("Escribe al menos 8 palabras.")

        else:

            palabras = re.findall(r"\b[\w'-]+\b", texto)

            oraciones = [
                s for s in re.split(r"[.!?]+", texto)
                if s.strip()
            ]

            repetidas = sorted({
                p.lower()
                for p in palabras
                if palabras.lower().count(p.lower()) > 3
                and len(p) > 3
            })

            a, b, c = st.columns(3)

            a.metric("Palabras", len(palabras))
            b.metric("Oraciones", len(oraciones))
            c.metric("Repeticiones", len(repetidas))

            st.success("¡Has completado tu actividad!")

            if repetidas:

                st.write("Palabras que puedes intentar variar:")
                st.write(", ".join(repetidas))

            st.markdown("### Autoevaluación")

            st.write("""
            - ¿Respondí al tema solicitado?
            - ¿Utilicé correctamente los tiempos verbales?
            - ¿Organicé mis ideas?
            - ¿Revisé la ortografía?
            """)

            completar(f"writing-{nivel}", 10)


# =====================================================
# PROGRESO
# =====================================================

elif pagina == "📈 Mi progreso":

    cabecera(
        "Mi progreso 📈",
        "Observa cuánto has avanzado en tu aprendizaje."
    )

    a, b, c = st.columns(3)

    a.metric("⭐ Experiencia", st.session_state.xp)

    b.metric(
        "🏆 Actividades",
        len(st.session_state.completadas)
    )

    c.metric("🎯 Nivel actual", nivel)

    st.divider()

    st.subheader("Tus niveles")

    for codigo, info in NIVELES.items():

        cantidad = sum(
            1 for actividad in st.session_state.completadas
            if actividad.startswith(codigo + "-")
        )

        st.write(f"**{info['emoji']} {codigo} - {info['nombre']}**")

        st.progress(
            min(cantidad / 8, 1.0),
            text=f"{cantidad} actividades registradas"
        )

    st.divider()

    st.subheader("🏅 Insignias")

    insignias = [
        ("🌱", "Primeros pasos", st.session_state.xp >= 10),
        ("📚", "Estudiante constante", len(st.session_state.completadas) >= 3),
        ("🧠", "Mente activa", len(st.session_state.completadas) >= 5),
        ("⭐", "100 XP", st.session_state.xp >= 100)
    ]

    columnas = st.columns(4)

    for columna, (emoji, nombre, desbloqueada) in zip(columnas, insignias):

        with columna:

            st.markdown('<div class="card">', unsafe_allow_html=True)

            st.markdown(f"## {emoji}")

            st.markdown(f"**{nombre}**")

            if desbloqueada:

                st.success("Desbloqueada")

            else:

                st.caption("Bloqueada")

            st.markdown('</div>', unsafe_allow_html=True)


# =====================================================
# PIE DE PÁGINA
# =====================================================

st.divider()

st.markdown(
    """
    <div style="text-align:center; color:#8992A7;">
        🌍 LINGUAPATH · Aprende hoy, avanza cada día.
    </div>
    """,
    unsafe_allow_html=True
)
