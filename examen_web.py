import streamlit as st
from datetime import date

st.set_page_config(page_title="COGNUSS Extenso V2", page_icon="🎓", layout="centered")

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

if date.today() > date(2026, 6, 30):
    st.error("🚨 Esta aplicación ha caducado.")
    st.stop()

st.sidebar.markdown("## ⚙️ Menú Examen")
opcion_bloque = st.sidebar.selectbox("Selecciona Bloque:", ["--- Seleccionar ---", "Bloque 5: Examen Repetición"])

st.sidebar.markdown("---")
st.sidebar.markdown("### 👥 Propiedad Intelectual & Créditos")
st.sidebar.info("* **Profesor Titular**: Dr. Oscar Enrique Dávila\n* **Recopilación**: Danitza Araya\n* **Desarrollador**: Miguel López Lavados\n* **IA**: Agente Colaborador\n\n🔒 **Derechos Reservados © 2026**")

if "tab_select" not in st.session_state:
    st.session_state.tab_select = 0

if opcion_bloque == "Bloque 5: Examen Repetición":
    st.title("⚖️ Examen de Repetición")
    st.caption("Cuestionario Maestro Integrado")
    st.markdown("---")
    
    # Manejo del estado del selector de pestañas
    nombres_tabs = ["Tema 1", "Tema 2", "Tema 3", "Tema 4", "Tema 5", "Tema 6: Baluarte Escrito"]
    
    # Renderizar pestañas controladas por sesión
    mis_tabs = st.tabs(nombres_tabs)

    with mis_tabs[0]:
        st.markdown("### 🏛️ Eje 1: Concilios de Toledo")
        st.markdown("**Enunciado:** ¿Mediante qué mecanismo legal las decisiones aprobadas unánimemente en los Concilios de Toledo se promulaban como leyes civiles del Reino Visigodo?")
        a1 = st.radio("Opciones:", ["A) La Lex in confirmatione concilii dictada por el monarca.", "B) El Tomus Regius.", "C) El Fuero de Albedrío.", "D) El canon eclesiástico."], index=None, key="op_1")
        if a1:
            if a1.startswith("A)"): st.success("✅ ¡Correcto!")
            else: st.error("❌ Incorrecto. Opción correcta: A)")
        st.info("💡 Para ir a la siguiente pregunta, haz clic en la pestaña **'Tema 2'** arriba.")

    with mis_tabs[1]:
        st.markdown("### 🏡 Eje 2: Cartas Pueblas y Fueros")
        st.markdown("**Enunciado:** ¿Qué diferencia jurídica fundamental existía en la Alta Edad Media entre las Cartas Pueblas primarias y los Fueros extensos municipales?")
        a2 = st.radio("Opciones:", ["A) Las Cartas Pueblas eran eclesiásticas.", "B) Las Cartas Pueblas regulaban solo condiciones económicas y agrarias de asentamiento; los Fueros extensos eran ordenamientos integrales.", "C) Las Cartas Pueblas eran orales.", "D) Las Cartas Pueblas regían en zona islámica."], index=None, key="op_2")
        if a2:
            if a2.startswith("B)"): st.success("✅ ¡Correcto!")
            else: st.error("❌ Incorrecto. Opción correcta: B)")
        st.info("💡 Para ir a la siguiente pregunta, haz clic en la pestaña **'Tema 3'** arriba.")

    with mis_tabs[2]:
        st.markdown("### ⚔️ Eje 3: Fuero de Albedrío y Fazañas")
        st.markdown("**Enunciado:** En Castilla, ¿qué eran las Fazañas?")
        a3 = st.radio("Opciones:", ["A) Leyes escritas del monarca.", "B) Contratos agrarios reales.", "C) Sentencias de los jueces de albedrío que se convertían en precedentes judiciales vinculantes.", "D) Ordalías de la Iglesia."], index=None, key="op_3")
        if a3:
            if a3.startswith("C)"): st.success("✅ ¡Correcto!")
            else: st.error("❌ Incorrecto. Opción correcta: C)")
        st.info("💡 Para ir a la siguiente pregunta, haz clic en la pestaña **'Tema 4'** arriba.")

    with mis_tabs[3]:
        st.markdown("### 🎓 Eje 4: Formación del Derecho Común")
        st.markdown("**Enunciado:** ¿Objetivo central de los Comentaristas?")
        a4 = st.radio("Opciones:", ["A) Aplicar y adaptar de forma práctica el derecho romano a las realidades y litigios reales.", "B) Estudiar exégesis germánica.", "C) Fijar el significado literal original.", "D) Redactar el Credo Niceno."], index=None, key="op_4")
        if a4:
            if a4.startswith("A)"): st.success("✅ ¡Correcto!")
            else: st.error("❌ Incorrecto. Opción correcta: A)")
        st.info("💡 Para ir a la siguiente pregunta, haz clic en la pestaña **'Tema 5'** arriba.")

    with mis_tabs[4]:
        st.markdown("### 👑 Eje 5: Tradición de Asturias-León")
        st.markdown("**Enunciado:** ¿Característica de Asturias-León frente a Castilla?")
        a5 = st.radio("Opciones:", ["A) El predominio del derecho consuetudinario.", "B) Un sistema marcadamente legalista basado en la vigencia y aplicación formal de las leyes del Liber Iudiciorum.", "C) La adopción del derecho de las taifas.", "D) El rechazo absoluto de las leyes escritas."], index=None, key="op_5")
        if a5:
            if a5.startswith("B)"): st.success("✅ ¡Correcto!")
            else: st.error("❌ Incorrecto. Opción correcta: B)")
        st.info("💡 Para ir a las respuestas de desarrollo, haz clic en la pestaña **'Tema 6: Baluarte Escrito'** arriba.")

    with mis_tabs[5]:
        st.markdown("### 📝 Baluarte Escrito: Respuestas Oficiales de la Cátedra")
        st.info("⏱️ **Memorización Gradual**: Presiona el botón del tema que deseas repasar. La respuesta oficial aparecerá por **25 segundos** antes de difuminarse.")
        st.markdown("---")
        
        st.markdown("#### Tópico 1: Importancia de los Concilios en la España Visigoda")
        if st.button("👁️ Mostrar Respuesta Maestra - Tema 1", key="btn_esc_1"):
            st.markdown('<div class="respuesta-maestra-box"><b>Respuesta Oficial:</b> Los Concilios de Toledo se consolidaron como asambleas político-religiosas y órganos colegisladores fundamentales tras la conversión al catolicismo en el 589 d.C. El monarca junto al Aula Real fijaba la agenda con el Tomus Regius, transformando los acuerdos en cánones convalidados mediante la Lex in confirmatione concilii. El III Concilio decretó la conversión de Recaredo, unificando el territorio. El IV Concilio, presidido por San Isidoro, institucionalizó la monarquía electiva (canon 75) contra el morbo gótico. El VIII Concilio redactó la primera edición del Liber Iudiciorum bajo Recesvinto. El XII Concilio validó a Ervigio y endureció las leyes antisemitas. El XIII Concilio otorgó el Habeas Corpus Visigodo, protegiendo a los nobles de arrestos reales arbitrarios.</div>', unsafe_allow_html=True)
        st.text_area("✍️ Practica tu redacción (Tema 1):", key="txt_esc_1", height=100)
        st.markdown("<br><hr>", unsafe_allow_html=True)

        st.markdown("#### Tópico 2: El Derecho Local en la Alta Edad Media")
        if st.button("👁️ Mostrar Respuesta Maestra - Tema 2", key="btn_esc_2"):
            st.markdown('<div class="respuesta-maestra-box"><b>Respuesta Oficial:</b> El derecho local altomedieval surgió por la fragmentación política tras la invasión del 711 d.C. y la urgencia de repoblar las fronteras cristianas. Las Cartas Pueblas constituyeron el tipo documental más primario, regulando solo condiciones económicas y agrarias para los colonos. Los Fueros evolucionaron otorgando estatutos jurídicos privilegiados, exención fiscal y autonomía organizativa municipal. Los fueros breves fijaban exenciones básicas para la supervivencia fronteriza. Los fueros extensos (siglos XII-XIII, como el de Cuenca) estructuraron ordenamientos íntegros penales, civiles y procesales. Este particularismo creó un mosaico normativo autónomo que debilitó el poder central real.</div>', unsafe_allow_html=True)
        st.text_area("✍️ Practica tu redacción (Tema 2):", key="txt_esc_2", height=100)
        st.markdown("<br><hr>", unsafe_allow_html=True)

        st.markdown("#### Tópico 3: Características del Derecho Territorial en Castilla")
        if st.button("👁️ Mostrar Respuesta Maestra - Tema 3", key="btn_esc_3"):
            st.markdown('<div class="respuesta-maestra-box"><b>Respuesta Oficial:</b> El derecho castellano altomedieval fue consuetudinario, popular, no escrito e independiente del Liber. En el 843 d.C., Castilla rechazó formalmente las leyes visigodas de León quemando los textos. Adoptó el Fuero de Albedrío, un sistema donde jueces de la comunidad resolvían litigios según equidad y costumbres. Las Fazañas eran estas sentencias judiciales que operaban de inmediato como precedentes vinculantes. Ante una situación nueva fronteriza, el fallo del juez se convertía en la regla jurídica obligatoria para casos futuros, creando un orden dinámico y flexible.</div>', unsafe_allow_html=True)
        st.text_area("✍️ Practica tu redacción (Tema 3):", key="txt_esc_3", height=100)
        st.markdown("<br><hr>", unsafe_allow_html=True)

        st.markdown("#### Tópico 4: Formación del Derecho Común")
        if st.button("👁️ Mostrar Respuesta Maestra - Tema 4", key="btn_esc_4"):
            st.markdown('<div class="respuesta-maestra-box"><b>Respuesta Oficial:</b> El Ius Commune integró el derecho romano justinianeo, el canónico y el feudal en la Baja Edad Media. Inició en el siglo XI al redescubrirse el Digesto y fundarse la Escuela de Bolonia (1088 d.C.) por Irnerio. Los Glosadores (siglos XI-XIII) hicieron un análisis teórico y exegético literal fijando el sentido mediante glosas interlineales. Los Comentaristas (siglos XIII-XV), liderados por Bartolo de Sassoferrato, adaptaron el derecho romano a la práctica de los tribunales. Se complementó con el Decreto de Graciano (1140 d.C.), que armonizó cánones de la Iglesia, sirviendo a los monarcas para centralizar el poder.</div>', unsafe_allow_html=True)
