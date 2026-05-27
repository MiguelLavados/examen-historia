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
    
    if modo == "Cuestionario Escrito (Memorización Gradual)":
        st.info("⏱️ **Método Gradual Activo**: Al presionar el botón de un tema, la respuesta oficial de la cátedra aparecerá por exactamente **12 segundos** y luego se difuminará por completo.")
        
        # Tema 1
        st.markdown("#### Tópico N.º 1: 1. Importancia de los Concilios en la España Visigoda (Toledo 3, 4, 8, 12 y 13)")
        if st.button("👁️ Mostrar Respuesta Maestra - Tema 1", key="btn_esc_1"):
            st.markdown('<div class="respuesta-maestra-box"><b>Respuesta de la Cátedra (10-15 Líneas):</b><br>Los Concilios de Toledo se consolidaron como asambleas político-religiosas y órganos colegisladores fundamentales tras la conversión del reino visigodo al catolicismo en el año 589 d.C. Bajo esta dinámica, el monarca junto al Aula Real fijaba la agenda temática inaugurando las sesiones y entregando el Tomus Regius, que contenía los proyectos de ley que los obispos debían estudiar, debatir y corregir de manera unánime. Los acuerdos resultantes se transformaban en cánones conciliares y se promulgaban formalmente como leyes civiles del reino mediante la Lex in confirmatione concilii dictada por el monarca. El III Concilio (589 d.C.) decretó la conversión del rey Recaredo, unificando religiosamente el territorio. El IV Concilio (633 d.C.), presidido por San Isidoro, institucionalizó la monarquía electiva mediante el canon 75 para regular la sucesión real y combatir el "morbo gótico". El VIII Concilio (653 d.C.) legitimó el acceso al trono de Recesvinto y redactó la histórica primera edición del Liber Iudiciorum. El XII Concilio (680 d.C.) validó la polémica sucesión de Ervigio frente a Wamba y endureció drásticamente la legislación antisemita. Finalmente, el XIII Concilio (683 d.C.) limitó el absolutismo monárquico al otorgar el "Habeas Corpus Visigodo", brindando sólidas garantías judiciales a los nobles frente a arrestos arbitrarios de la corona.</div>', unsafe_allow_html=True)
        st.text_area("✍️ Redacta tu desarrollo en base a lo memorizado:", key="in_esc_1", height=110)
        st.markdown("<br>", unsafe_allow_html=True)

        # Tema 5
        st.markdown("#### Tópico N.º 5: 5. El Derecho Local en la Alta Edad Media: Cartas Pueblas y Fueros")
        if st.button("👁️ Mostrar Respuesta Maestra - Tema 5", key="btn_esc_5"):
            st.markdown('<div class="respuesta-maestra-box"><b>Respuesta de la Cátedra (10-15 Líneas):</b><br>El derecho local altomedieval eclosionó con fuerza debido a la profunda fragmentación política de la península y a la imperiosa necesidad de los reyes cristianos de repoblar las tierras ganadas a los musulmanes tras la invasión del 711 d.C. En este escenario de frontera, las Cartas Pueblas constituyeron el tipo documental más rudimentario y primario, limitándose a regular exclusivamente las condiciones agrarias y económicas mínimas para el asentamiento de los colonos. Los Fueros (tanto breves como extensos) evolucionaron a partir de estas cartas, otorgando a los municipios un estatuto jurídico particular, privilegios de exención fiscal y una marcada autonomía organizativa. Los fueros breves fijaban las libertades básicas indispensables para atraer habitantes a las zonas de peligro militar fronterizo. Posteriormente, los fueros extensos de los siglos XII y XIII (como el célebre modelo de Cuenca-Teruel) desarrollaron ordenamientos jurídicos íntegros y complejos que abarcaban derecho civil, penal, procesal y organizativo municipal. Este marcado particularismo jurídico generó un mosaico de derechos locales autónomos que debilitó temporalmente la potestad legislativa centralizada de la corona, moldeando el autogobierno comunal.</div>', unsafe_allow_html=True)
        st.text_area("✍️ Redacta tu desarrollo en base a lo memorizado:", key="in_esc_5", height=110)
        st.markdown("<br>", unsafe_allow_html=True)

        # Tema 10
        st.markdown("#### Tópico N.º 10: 10. Características del Derecho Territorial en el Reino de Castilla: Fuero de Albedrío y Fazañas")
        if st.button("👁️ Mostrar Respuesta Maestra - Tema 10", key="btn_esc_10"):
            st.markdown('<div class="respuesta-maestra-box"><b>Respuesta de la Cátedra (10-15 Líneas):</b><br>El derecho castellano altomedieval se caracterizó por su profundo particularismo regional, su carácter puramente consuetudinario y no escrito, su origen Rooms popular y su total independencia de la tradición romana del Liber. Al carecer de un código legal escrito y uniforme, el derecho se construyó sobre las costumbres locales arraigadas en la comunidad. De acuerdo a la tradición histórica, en el año 843 d.C. los castellanos rechazaron formalmente el Liber Iudiciorum usado en León, llegando a quemar los textos legales por considerarlos ajenos a su realidad. En su lugar, instituyeron el "Fuero de Albedrío", un sistema judicial flexible donde los jueces locales de la comunidad resolvían los pleitos basándose en su propio sentido de la justicia y criterio de equidad. Por su parte, las "Fazañas" eran las sentencias o juicios de albedrío dictados por estos magistrados populares que se convertían de inmediato en precedentes judiciales vinculantes y obligatorios para futuros casos de la misma región. Este sistema judicial configuró un ordenamiento dinámico, casuístico y alejado de la tradición romanista escrito y del monarquismo legislativo, adaptándose con rapidez a los peligros cambiantes de la frontera.</div>', unsafe_allow_html=True)
        st.text_area("✍️ Redacta tu desarrollo en base a lo memorizado:", key="in_esc_10", height=110)
        st.markdown("<br>", unsafe_allow_html=True)

        # Tema 13
        st.markdown("#### Tópico N.º 13: 13. Formación del Derecho Común Romano Canónico")
        if st.button("👁️ Mostrar Respuesta Maestra - Tema 13", key="btn_esc_13"):
            st.markdown('<div class="respuesta-maestra-box"><b>Respuesta de la Cátedra (10-15 Líneas):</b><br>El Derecho Común (Ius Commune) se articuló durante la Baja Edad Media europea como un sistema normativo supranacional, técnico y unificado mediante la integración del derecho romano, el canónico y el derecho feudal. Su origen se sitúa en el siglo XI tras el redescubrimiento en Italia del manuscrito clásico del Digesto de Justiniano y el nacimiento de la célebre Escuela de Bolonia en 1088 d.C. bajo la enseñanza de Irnerio. Los juristas de este período se dividieron en dos escuelas fundamentales: los Glosadores y los Comentaristas. Los Glosadores (siglos XI al XIII) analizaron los textos justinianeos de forma estrictamente teórica y exegética, aclarando el significado literal del texto a través de breves anotaciones marginales o interlineales llamadas glosas. Por el contrario, los Comentaristas o Postglosadores (siglos XIII al XV), como Bartolo de Sassoferrato, adoptaron un enfoque pragmático y utilitario, elaborando ensayos jurídicos profundos encaminados a adaptar el derecho romano teórico a las necesidades prácticas y comerciales de los tribunales medievales. Este sistema se complementó en el ámbito eclesiástico con el Decreto de Graciano (1140 d.C.), que concordó y armonizó los cánones eclesiásticos discordantes de la Iglesia, alzándose como el modelo de recepción jurídica indispensable para los monarcas que buscaban centralizar su poder legislativo.</div>', unsafe_allow_html=True)
