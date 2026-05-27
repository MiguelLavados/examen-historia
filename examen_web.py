import streamlit as st
import random
from datetime import date

# Configuración de la página web optimizada para móviles y PC
st.set_page_config(page_title="COGNUSS Extenso V2", page_icon="🎓", layout="centered")

# Estilos CSS avanzados para el desvanecimiento controlado de las respuestas escritas
st.markdown("""
<style>
@keyframes blurFadeOut {
    0% { opacity: 1; filter: blur(0px); }
    75% { opacity: 1; filter: blur(0px); }
    100% { opacity: 0; filter: blur(10px); visibility: hidden; height: 0px; padding: 0px; margin: 0px; }
}
.respuesta-maestra-box {
    padding: 18px;
    background-color: #f4f9ff;
    border-left: 6px solid #1a73e8;
    border-radius: 6px;
    font-size: 14.5px;
    line-height: 1.6;
    color: #202124;
    font-weight: 500;
    animation: blurFadeOut 12s forwards;
}
</style>
""", unsafe_allow_html=True)

# Validación de fecha de caducidad obligatoria (30 de Junio de 2026)
if date.today() > date(2026, 6, 30):
    st.error("🚨 Esta aplicación ha caducado. El período de uso autorizado finalizó el 30 de Junio de 2026.")
    st.stop()

# --- MENÚ LATERAL GENERAL CON LOS CRÉDITOS SOLICITADOS ---
st.sidebar.markdown("## ⚙️ Menú Examen")

opcion_bloque = st.sidebar.selectbox(
    "Selecciona Bloque:",
    ["--- Seleccionar ---", "Bloque 5: Examen Repetición"]
)

st.sidebar.markdown("---")
st.sidebar.markdown("### 👥 Propiedad Intelectual & Créditos")
st.sidebar.info("""
* **Profesor Titular**: Dr. Oscar Enrique Dávila  
* **Recopilación (Escribana)**: Danitza Araya  
* **Desarrollador**: Miguel López Lavados  
* **Agente Colaborador IA**: IA (Tu Asistente)  
* **Motor de Conocimientos**: COGNUSS 2  

---
🔒 **Derechos Reservados © 2026**  
📅 *Fecha de Caducidad: 30 de Jun-2026*
""")

# --- INTERFAZ DINÁMICA ---
if opcion_bloque == "--- Seleccionar ---":
    st.title("🛡️ COGNUSS EXTENSO V2")
    st.subheader("Programa creado por Miguel López Lavados | Caduca: 30-Jun-2026")
    st.markdown("---")
    st.info("👈 Selecciona el Bloque 5 en el menú lateral izquierdo para cargar el examen de repetición.")

# --- SECCIÓN MAESTRA: BLOQUE 5 EXAMEN REPETICIÓN ---
elif opcion_bloque == "Bloque 5: Examen Repetición":
    st.title("⚖️ Examen de Repetición")
    st.subheader("Cuestionario Maestro Integrado - Temas 1, 5, 10, 13 y 18")
    st.markdown("---")
    
    modo = st.radio(
        "👉 **Selecciona la modalidad de evaluación para este bloque:**",
        ["Cuestionario Escrito (Memorización Gradual)", "Test de Selección Múltiple (Alternativas Cortas)"],
        index=0
    )
    st.markdown("---")
    
    # Formato de lista lineal seguro, sin estructuras de llaves que se puedan romper
    banco_repeticion = [
        [
            1, 
            "1. Importancia de los Concilios en la España Visigoda (Toledo 3, 4, 8, 12 y 13)",
            "¿Mediante qué mecanismo legal las decisiones aprobadas unánimemente en los Concilios de Toledo se promulaban como leyes civiles del Reino?",
            ["La Lex in confirmatione concilii dictada por el monarca.", "El Tomus Regius entregado unilateralmente por el Oficio Palatino.", "El Fuero de Albedrío decretado de forma oral por el Senatus.", "El canon conciliar de valor exclusivamente eclesiástico."],
            "La Lex in confirmatione concilii dictada por el monarca.",
            "Los Concilios de Toledo se consolidaron como asambleas político-religiosas y órganos colegisladores fundamentales tras la conversión del reino visigodo al catolicismo en el año 589 d.C. Bajo esta dinámica, el monarca junto al Aula Real fijaba la agenda temática inaugurando las sesiones y entregando el Tomus Regius, que contenía los proyectos de ley que los obispos debían estudiar, debatir y corregir de manera unánime. Los acuerdos resultantes se transformaban en cánones conciliares y se promulgaban formalmente como leyes civiles del reino mediante la Lex in confirmatione concilii dictada por el monarca. El III Concilio (589 d.C.) decretó la conversión del rey Recaredo, unificando religiosamente el territorio. El IV Concilio (633 d.C.), presidido por San Isidoro, institucionalizó la monarquía electiva mediante el canon 75 para regular la sucesión real y combatir el 'morbo gótico'. El VIII Concilio (653 d.C.) legitimó el acceso al trono de Recesvinto y redactó la histórica primera edición del Liber Iudiciorum. El XII Concilio (680 d.C.) validó la polémica sucesión de Ervigio frente a Wamba y endureció drásticamente la legislación antisemita. Finalmente, el XIII Concilio (683 d.C.) limitó el absolutismo monárquico al otorgar el 'Habeas Corpus Visigodo', brindando sólidas garantías judiciales a los nobles frente a arrestos arbitrarios de la corona."
        ],
        [
            5, 
            "5. El Derecho Local en la Alta Edad Media: Cartas Pueblas y Fueros",
            "¿Qué diferencia jurídica fundamental existía en la Alta Edad Media entre las Cartas Pueblas y los Fueros extensos?",
            ["Las Cartas Pueblas regulaban solo condiciones económicas y agrarias de asentamiento; los Fueros extensos eran ordenamientos jurídicos municipales integrales.", "Las Cartas Pueblas eran códigos eclesiásticos y los Fueros extensos regulaban la guerra civil.", "Las Cartas Pueblas eran de origen romano-germánico escrito y los Fueros extensos eran costumbres orales.", "Las Cartas Pueblas regían en la España islámica y los Fueros extensos en la zona atlántica."],
            "Las Cartas Pueblas regulaban solo condiciones económicas y agrarias de asentamiento; los Fueros extensos eran ordenamientos jurídicos municipales integrales.",
            "El derecho local altomedieval eclosionó con fuerza debido a la profunda fragmentación política de la península y a la imperiosa necesidad de los reyes cristianos de repoblar las tierras ganadas a los musulmanes tras la invasión del 711 d.C. En este escenario de frontera, las Cartas Pueblas constituyeron el tipo documental más rudimentario y primario, limitándose a regular exclusivamente las condiciones agrarias y económicas mínimas para el asentamiento de los colonos. Los Fueros (tanto breves como extensos) evolucionaron a partir de estas cartas, otorgando a los municipios un estatuto jurídico particular, privilegios de exención fiscal y una marcada autonomía organizativa. Los fueros breves fijaban las libertades básicas indispensables para atraer habitantes a las zonas de peligro militar fronterizo. Posteriormente, los fueros extensos de los siglos XII y XIII (como el célebre modelo de Cuenca-Teruel) desarrollaron ordenamientos jurídicos íntegros y complejos que abarcaban derecho civil, penal, procesal y organizativo municipal. Este marcado particularismo jurídico generó un mosaico de derechos locales autónomos que debilitó temporalmente la potestad legislativa centralizada de la corona, moldeando el autogobierno comunal."
        ],
        [
            10, 
            "10. Características del Derecho Territorial en el Reino de Castilla: Fuero de Albedrío y Fazañas",
            "En el derecho territorial castellano de la Alta Edad Media, ¿qué eran técnicamente las denominadas Fazañas?",
            ["Sentencias de los jueces de albedrío que se convertían en precedentes judiciales vinculantes.", "Leyes escritas dictadas por el monarca para unificar los reinos cristianos de la península.", "Contratos agrarios bilaterales celebrados de forma solemne ante los funcionarios del Aula Real.", "Ordalías o juicios de Dios regulados estrictamente por las costumbres del derecho romano vulgar."],
            "Sentencias de los jueces de albedrío que se convertían en precedentes judiciales vinculantes.",
            "El derecho castellano altomedieval se caracterizó por su profundo particularismo regional, su carácter puramente consuetudinario y no escrito, su origen eminentemente popular y su total independencia de la tradición romana del Liber. Al carecer de un código legal escrito y uniforme, el derecho se construyó sobre las costumbres locales arraigadas en la comunidad. De acuerdo a la tradición histórica, en el año 843 d.C. los castellanos rechazaron formalmente el Liber Iudiciorum usado en León, llegando a quemar los textos legales por considerarlos ajenos a su realidad. En su lugar, instituyeron el 'Fuero de Albedrío', un sistema judicial flexible donde los jueces locales de la comunidad resolvían los pleitos basándose en su propio sentido de la justicia y criterio de equidad. Por su parte, las 'Fazañas' eran las sentencias o juicios de albedrío dictados por estos magistrados populares que se convertían de inmediato en precedentes judiciales vinculantes y obligatorios para futuros casos de la misma región. Este sistema judicial configuró un ordenamiento dinámico, casuístico y alejado de la tradición romanista escrito y del monarquismo legislativo, adaptándose con rapidez a los peligros cambiantes de la frontera."
        ],
        [
            13, 
            "13. Formación del Derecho Común Romano Canónico",
            "¿Cuál era el original objetivo central de la Escuela de los Comentaristas o Postglosadores en comparación con los Glosadores?",
            ["Aplicar y adaptar de forma práctica el derecho romano a las realidades y litigios reales de los tribunales.", "Estudiar exclusivamente las costumbres consuetudinarias no escritas de la frontera germánica.", "Limitarse a fijar el significado literal y original de las leyes de Justiniano mediante el uso de glosas.", "Redactar la profesión oficial de fe cristiana del Credo Niceno durante la celebración de concilios ecuménicos."],
            "Aplicar y adaptar de forma práctica el derecho romano a las realidades y litigios reales de los tribunales.",
