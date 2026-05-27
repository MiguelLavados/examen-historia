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
    st.error("🚨 Esta aplicación ha caducado. El período de uso autorizado finalizó el 30 de Junio de 2026.")
    st.stop()

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
    st.caption("Cuestionario Maestro Integrado")
    st.markdown("---")
    
    modo = st.radio("👉 **Selecciona la modalidad de evaluación:**", ["Cuestionario Escrito (Memorización Gradual)", "Test de Selección Múltiple (Selector por Pestañas)"], index=1)
    st.markdown("---")
    
    # Crear las 6 pestañas interactivas independientes arriba en la pantalla
    t1, t2, t3, t4, t5, t6 = st.tabs(["Tema 1", "Tema 2", "Tema 3", "Tema 4", "Tema 5", "Tema 6"])

    # --- TEMA 1 ---
    with t1:
        st.markdown("### 🏛️ Eje 1: Concilios de Toledo")
        if modo == "Cuestionario Escrito (Memorización Gradual)":
            if st.button("👁️ Mostrar Respuesta Maestra - Tema 1", key="btn_e1"):
                st.markdown('<div class="respuesta-maestra-box"><b>Respuesta Oficial:</b> Los Concilios de Toledo se consolidaron como asambleas político-religiosas y órganos colegisladores fundamentales tras la conversión al catolicismo en el 589 d.C. El monarca junto al Aula Real fijaba la agenda con el Tomus Regius, transformando los acuerdos en cánones convalidados mediante la Lex in confirmatione concilii. El III Concilio decretó la conversión de Recaredo, unificando el territorio. El IV Concilio, presidido por San Isidoro, institucionalizó la monarquía electiva (canon 75) contra el morbo gótico. El VIII Concilio redactó la primera edición del Liber Iudiciorum bajo Recesvinto. El XII Concilio validó a Ervigio y endureció las leyes antisemitas. El XIII Concilio otorgó el Habeas Corpus Visigodo, protegiendo a los nobles de arrestos reales arbitrarios.</div>', unsafe_allow_html=True)
            st.text_area("✍️ Redacta tu desarrollo:", key="txt_e1", height=110)
        else:
            st.markdown("**Enunciado:** ¿Mediante qué mecanismo legal las decisiones aprobadas unánimemente en los Concilios de Toledo se promulaban como leyes civiles del Reino Visigodo?")
            a1 = st.radio("Opciones:", ["A) La Lex in confirmatione concilii dictada por el monarca.", "B) El Tomus Regius del Oficio Palatino.", "C) El Fuero de Albedrío del Senatus.", "D) El canon conciliar eclesiástico."], index=None, key="op_1")
            if a1:
                if a1.startswith("A)"): st.success("✅ ¡Correcto!")
                else: st.error("❌ Incorrecto. Opción correcta: A)")

    # --- TEMA 2 ---
    with t2:
        st.markdown("### 🏡 Eje 2: Cartas Pueblas y Fueros")
        if modo == "Cuestionario Escrito (Memorización Gradual)":
            if st.button("👁️ Mostrar Respuesta Maestra - Tema 2", key="btn_e2"):
                st.markdown('<div class="respuesta-maestra-box"><b>Respuesta Oficial:</b> El derecho local altomedieval surgió por la fragmentación política tras la invasión del 711 d.C. y la urgencia de repoblar las fronteras cristianas. Las Cartas Pueblas constituyeron el tipo documental más primario, regulando solo condiciones económicas y agrarias para los colonos. Los Fueros evolucionaron otorgando estatutos jurídicos privilegiados, exención fiscal y autonomía organizativa municipal. Los fueros breves fijaban exenciones básicas para la supervivencia fronteriza. Los fueros extensos (siglos XII-XIII, como el de Cuenca) estructuraron ordenamientos íntegros penales, civiles y procesales. Este particularismo creó un mosaico normativo autónomo que debilitó el poder central real.</div>', unsafe_allow_html=True)
            st.text_area("✍️ Redacta tu desarrollo:", key="txt_e2", height=110)
        else:
            st.markdown("**Enunciado:** ¿Qué diferencia jurídica fundamental existía en la Alta Edad Media entre las Cartas Pueblas primarias y los Fueros extensos municipales?")
            a2 = st.radio("Opciones:", ["A) Las Cartas Pueblas eran eclesiásticas.", "B) Las Cartas Pueblas regulaban solo condiciones económicas y agrarias de asentamiento; los Fueros extensos eran ordenamientos jurídicos municipales integrales.", "C) Las Cartas Pueblas eran costumbres orales.", "D) Las Cartas Pueblas regían en zona islámica."], index=None, key="op_2")
            if a2:
                if a2.startswith("B)"): st.success("✅ ¡Correcto!")
                else: st.error("❌ Incorrecto. Opción correcta: B)")

    # --- TEMA 3 ---
    with t3:
        st.markdown("### ⚔️ Eje 3: Fuero de Albedrío y Fazañas")
        if modo == "Cuestionario Escrito (Memorización Gradual)":
            if st.button("👁️ Mostrar Respuesta Maestra - Tema 3", key="btn_e3"):
                st.markdown('<div class="respuesta-maestra-box"><b>Respuesta Oficial:</b> El derecho castellano altomedieval fue consuetudinario, popular, no escrito e independiente del Liber. En el 843 d.C., Castilla rechazó formalmente las leyes visigodas de León quemando los textos. Adoptó el Fuero de Albedrío, un sistema donde jueces de la comunidad resolvían litigios según equidad y costumbres. Las Fazañas eran estas sentencias judiciales que operaban de inmediato como precedentes vinculantes. Ante una situación nueva fronteriza, el fallo del juez se convertía en la regla jurídica obligatoria para casos futuros, creando un orden dinámico y flexible.</div>', unsafe_allow_html=True)
            st.text_area("✍️ Redacta tu desarrollo:", key="txt_e3", height=110)
        else:
            st.markdown("**Enunciado:** En Castilla, ¿qué eran las Fazañas?")
            a3 = st.radio("Opciones:", ["A) Leyes escritas del monarca.", "B) Contratos agrarios reales.", "C) Sentencias de los jueces de albedrío que se convertían en precedentes judiciales vinculantes.", "D) Ordalías de la Iglesia."], index=None, key="op_3")
            if a3:
                if a3.startswith("C)"): st.success("✅ ¡Correcto!")
                else: st.error("❌ Incorrecto. Opción correcta: C)")

    # --- TEMA 4 ---
    with t4:
        st.markdown("### 🎓 Eje 4: Formación del Derecho Común")
        if modo == "Cuestionario Escrito (Memorización Gradual)":
            if st.button("👁️ Mostrar Respuesta Maestra - Tema 4", key="btn_e4"):
                st.markdown('<div class="respuesta-maestra-box"><b>Respuesta Oficial:</b> El Ius Commune integró el derecho romano justinianeo, el canónico y el feudal en la Baja Edad Media. Inició en el siglo XI al redescubrirse el Digesto y fundarse la Escuela de Bolonia (1088 d.C.) por Irnerio. Los Glosadores (siglos XI-XIII) hicieron un análisis teórico y exegético literal fijando el sentido mediante glosas interlineales. Los Comentaristas (siglos XIII-XV), liderados por Bartolo de Sassoferrato, adaptaron el derecho romano a la práctica de los tribunales. Se complementó con el Decreto de Graciano (1140 d.C.), que armonizó cánones de la Iglesia, sirviendo a los monarcas para centralizar el poder.</div>', unsafe_allow_html=True)
            st.text_area("✍️ Redacta tu desarrollo:", key="txt_e4", height=110)
        else:
            st.markdown("**Enunciado:** ¿Objetivo central de los Comentaristas?")
            a4 = st.radio("Opciones:", ["A) Aplicar y adaptar de forma práctica el derecho romano a las realidades y litigios reales.", "B) Estudiar exégesis germánica.", "C) Fijar el significado literal original.", "D) Redactar el Credo Niceno."], index=None, key="op_4")
            if a4:
                if a4.startswith("A)"): st.success("✅ ¡Correcto!")
                else: st.error("❌ Incorrecto. Opción correcta: A)")

    # --- TEMA 5 ---
    with t5:
        st.markdown("### 👑 Eje 5: Tradición de Asturias-León")
        if modo == "Cuestionario Escrito (Memorización Gradual)":
            if st.button("👁️ Mostrar Respuesta Maestra - Tema 5", key="btn_e5"):
