import streamlit as st
import random
from datetime import date

# Configuración de la página web optimizada para móviles y PC
st.set_page_config(page_title="COGNUSS Extenso V2", page_icon="🎓", layout="centered")

# Estilos CSS con temporizador de 25 segundos fijos aislados
st.markdown("""
<style>
@keyframes blurFadeOut {
    0% { opacity: 1; filter: blur(0px); }
    85% { opacity: 1; filter: blur(0px); }
    100% { opacity: 0; filter: blur(10px); visibility: hidden; }
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
    margin-bottom: 25px;
    margin-top: 10px;
    display: block;
    animation: blurFadeOut 25s forwards;
}
</style>
""", unsafe_allow_html=True)

# Validación de fecha de caducidad obligatoria (30 de Junio de 2026)
if date.today() > date(2026, 6, 30):
    st.error("🚨 Esta aplicación ha caducado. El período de uso autorizado finalizó el 30 de Junio de 2026.")
    st.stop()

# --- MENÚ LATERAL GENERAL CON LOS CRÉDITOS SOLICITADOS ---
st.sidebar.markdown("## ⚙️ Menú Examen")
opcion_bloque = st.sidebar.selectbox("Selecciona Bloque:", ["--- Seleccionar ---", "Bloque 5: Examen Repetición"])

st.sidebar.markdown("---")
st.sidebar.markdown("### 👥 Propiedad Intelectual & Créditos")
st.sidebar.info("* **Profesor Titular**: Dr. Oscar Enrique Dávila\n* **Recopilación (Escribana)**: Danitza Araya\n* **Desarrollador**: Miguel López Lavados\n* **Agente Colaborador IA**: IA\n* **Motor de Conocimientos**: COGNUSS 2\n\n--- \n🔒 **Derechos Reservados © 2026**\n📅 *Fecha de Caducidad: 30 de Jun-2026*")

if opcion_bloque == "--- Seleccionar ---":
    st.title("🛡️ COGNUSS EXTENSO V2")
    st.subheader("Programa creado por Miguel López Lavados | Caduca: 30-Jun-2026")
    st.markdown("---")
    st.info("👈 Selecciona el Bloque 5 en el menú lateral izquierdo para cargar el examen de repetición.")

elif opcion_bloque == "Bloque 5: Examen Repetición":
    st.title("⚖️ Examen de Repetición")
    st.subheader("Cuestionario Maestro Integrado - Control de Avance Secuencial")
    st.markdown("---")
    
    modo = st.radio("👉 **Selecciona la modalidad de evaluación:**", ["Cuestionario Escrito (Memorización Gradual)", "Test de Selección Múltiple (Avance Secuencial de Preguntas)"], index=0)
    st.markdown("---")
    
    # Inicializar variables de sesión para el avance lineal continuo
    if "pregunta_actual" not in st.session_state:
        st.session_state.pregunta_actual = 1
    if "ans_1" not in st.session_state: st.session_state.ans_1 = None
    if "ans_2" not in st.session_state: st.session_state.ans_2 = None
    if "ans_3" not in st.session_state: st.session_state.ans_3 = None
    if "ans_4" not in st.session_state: st.session_state.ans_4 = None
    if "ans_5" not in st.session_state: st.session_state.ans_5 = None
    if "ans_6" not in st.session_state: st.session_state.ans_6 = None

    # --- MODALIDAD 1: CUESTIONARIO ESCRITO ---
    if modo == "Cuestionario Escrito (Memorización Gradual)":
        st.info("⏱️ **Método Gradual Activo**: Avanza pregunta por pregunta utilizando los botones inferiores. Al presionar el botón central, la respuesta oficial de la cátedra aparecerá por exactamente **25 segundos** antes de difuminarse.")
        
        if st.session_state.pregunta_actual == 1:
            st.markdown("#### Tópico N.º 1: 1. Importancia de los Concilios en la España Visigoda (Toledo 3, 4, 8, 12 y 13)")
            if st.button("👁️ Mostrar Respuesta Maestra - Tema 1", key="btn_esc_1"):
                st.markdown('<div class="respuesta-maestra-box"><b>Respuesta Oficial:</b> Los Concilios de Toledo se consolidaron como asambleas político-religiosas y órganos colegisladores fundamentales tras la conversión al catolicismo en el 589 d.C. El monarca junto al Aula Real fijaba la agenda con el Tomus Regius, transformando los acuerdos en cánones convalidados mediante la Lex in confirmatione concilii. El III Concilio decretó la conversión de Recaredo, unificando el territorio. El IV Concilio, presidido por San Isidoro, institucionalizó la monarquía electiva (canon 75) contra el morbo gótico. El VIII Concilio redactá la primera edición del Liber Iudiciorum bajo Recesvinto. El XII Concilio validó a Ervigio y endureció las leyes antisemitas. El XIII Concilio otorgó el Habeas Corpus Visigodo, protegiendo a los nobles de arrestos reales arbitrarios.</div>', unsafe_allow_html=True)
            st.text_area("✍️ Redacta tu desarrollo en base a lo memorizado:", key="in_esc_1", height=120)

        elif st.session_state.pregunta_actual == 2:
            st.markdown("#### Tópico N.º 2: 5. El Derecho Local en la Alta Edad Media: Cartas Pueblas y Fueros")
            if st.button("👁️ Mostrar Respuesta Maestra - Tema 5", key="btn_esc_5"):
                st.markdown('<div class="respuesta-maestra-box"><b>Respuesta Oficial:</b> El derecho local altomedieval surgió por la fragmentación política tras la invasión del 711 d.C. y la urgencia de repoblar las fronteras cristianas. Las Cartas Pueblas constituyeron el tipo documental más primario, regulando solo condiciones económicas y agrarias para los colonos. Los Fueros evolucionaron otorgando estatutos jurídicos privilegiados, exención fiscal y autonomía organizativa municipal. Los fueros breves fijaban exenciones básicas para la supervivencia fronteriza. Los fueros extensos (siglos XII-XIII, como el de Cuenca) estructuraron ordenamientos íntegros penales, civiles y procesales. Este particularismo creó un mosaico normativo autónomo que debilitó el poder central real.</div>', unsafe_allow_html=True)
            st.text_area("✍️ Redacta tu desarrollo en base a lo memorizado:", key="in_esc_5", height=120)

        elif st.session_state.pregunta_actual == 3:
            st.markdown("#### Tópico N.º 3: 10. Características del Derecho Territorial en Castilla: Fuero de Albedrío y Fazañas")
            if st.button("👁️ Mostrar Respuesta Maestra - Tema 10", key="btn_esc_10"):
                st.markdown('<div class="respuesta-maestra-box"><b>Respuesta Oficial:</b> El derecho castellano altomedieval fue consuetudinario, popular, no escrito e independiente del Liber. En el 843 d.C., Castilla rechazó formalmente las leyes visigodas de León quemando los textos. Adoptó el Fuero de Albedrío, un sistema donde jueces de la comunidad resolvían litigios según equidad y costumbres. Las Fazañas eran estas sentencias judiciales que operaban de inmediato como precedentes vinculantes. Ante una situación nueva fronteriza, el fallo del juez se convertía en la regla jurídica obligatoria para casos futuros, creando un orden dinámico y flexible.</div>', unsafe_allow_html=True)
            st.text_area("✍️ Redacta tu desarrollo en base a lo memorizado:", key="in_esc_10", height=120)

        elif st.session_state.pregunta_actual == 4:
            st.markdown("#### Tópico N.º 4: 13. Formación del Derecho Común Romano Canónico: Glosadores y Comentaristas")
            if st.button("👁️ Mostrar Respuesta Maestra - Tema 13", key="btn_esc_13"):
                st.markdown('<div class="respuesta-maestra-box"><b>Respuesta Oficial:</b> El Ius Commune integró el derecho romano justinianeo, el canónico y el feudal en la Baja Edad Media. Inició en el siglo XI al redescubrirse el Digesto y fundarse la Escuela de Bolonia (1088 d.C.) por Irnerio. Los Glosadores (siglos XI-XIII) hicieron un análisis teórico y exegético literal fijando el sentido mediante glosas interlineales. Los Comentaristas (siglos XIII-XV), liderados por Bartolo de Sassoferrato, adaptaron el derecho romano a la práctica de los tribunales. Se complementó con el Decreto de Graciano (1140 d.C.), que armonizó cánones de la Iglesia, sirviendo a los monarcas para centralizar el poder.</div>', unsafe_allow_html=True)
            st.text_area("✍️ Redacta tu desarrollo en base a lo memorizado:", key="in_esc_13", height=120)

        elif st.session_state.pregunta_actual == 5:
            st.markdown("#### Tópico N.º 5: 18. El Derecho Territorial en el Reino de Asturias-León")
            if st.button("👁️ Mostrar Respuesta Maestra - Tema 18", key="btn_esc_18"):
                st.markdown('<div class="respuesta-maestra-box"><b>Respuesta Oficial:</b> Asturias-León defendió la continuidad legalista escrita del reino visigodo mediante el neogoticismo, oponiéndose al albedrío castellano. Aplicó rigurosamente el Liber Iudiciorum en el tribunal regio (Palatium). La territorialización se consolidó en el 1017 d.C. con las leyes territoriales de Alfonso V en las Cortes de León. En 1241 d.C., Fernando III ordenó su traducción oficial al romance bajo el nombre de Fuero Juzgo. Este texto unificado rigió las ciudades reconquistadas y se proyectó a América, aplicándose formalmente en tribunales chilenos hasta el siglo XIX ante la falta de un Código Penal patrio.</div>', unsafe_allow_html=True)
            st.text_area("✍️ Redacta tu desarrollo en base a lo memorizado:", key="in_esc_18", height=120)

        elif st.session_state.pregunta_actual == 6:
            st.markdown("#### Tópico N.º 6: Proyección Histórica: Vigencia del Fuero Juzgo en Chile")
            if st.button("👁️ Mostrar Respuesta Maestra - Tema 6", key="btn_esc_6"):
