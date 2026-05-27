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

if "preg_act" not in st.session_state: st.session_state.preg_act = 1
if "a1" not in st.session_state: st.session_state.a1 = None
if "a2" not in st.session_state: st.session_state.a2 = None
if "a3" not in st.session_state: st.session_state.a3 = None
if "a4" not in st.session_state: st.session_state.a4 = None
if "a5" not in st.session_state: st.session_state.a5 = None
if "a6" not in st.session_state: st.session_state.a6 = None

if opcion_bloque == "--- Seleccionar ---":
    st.title("🛡️ COGNUSS EXTENSO V2")
    st.subheader("Programa creado por Miguel López Lavados | Caduca: 30-Jun-2026")
    st.markdown("---")
    st.info("👈 Selecciona el Bloque 5 en el menú lateral izquierdo para cargar el examen de repetición.")

elif opcion_bloque == "Bloque 5: Examen Repetición":
    st.title("⚖️ Examen de Repetición")
    st.caption("Cuestionario Maestro Integrado")
    st.markdown("---")
    
    modo = st.radio("👉 **Selecciona la modalidad:**", ["Cuestionario Escrito", "Test de Alternativas Cortas"], index=1)
    st.markdown("---")
    
    if modo == "Cuestionario Escrito":
        st.info("⏱️ Respuesta en pantalla por 25 segundos fijos.")
        if st.session_state.preg_act == 1:
            st.markdown("#### Eje N.º 1: Importancia de los Concilios de Toledo")
            if st.button("👁️ Mostrar Respuesta Maestra - Tema 1", key="b1"):
                st.markdown('<div class="respuesta-maestra-box"><b>Respuesta Oficial:</b> Los Concilios de Toledo se consolidaron como asambleas político-religiosas y órganos colegisladores fundamentales tras la conversión al catolicismo en el 589 d.C. El monarca junto al Aula Real fijaba la agenda con el Tomus Regius, transformando los acuerdos en cánones convalidados mediante la Lex in confirmatione concilii. El III Concilio decretó la conversión de Recaredo, unificando el territorio. El IV Concilio, presidido por San Isidoro, institucionalizó la monarquía electiva (canon 75) contra el morbo gótico. El VIII Concilio redactó la primera edición del Liber Iudiciorum bajo Recesvinto. El XII Concilio validó a Ervigio y endureció las leyes antisemitas. El XIII Concilio otorgó el Habeas Corpus Visigodo, protegiendo a los nobles de arrestos reales arbitrarios.</div>', unsafe_allow_html=True)
            st.text_area("✍️ Redacta tu desarrollo:", key="ie1", height=110)
        elif st.session_state.preg_act == 2:
            st.markdown("#### Eje N.º 2: El Derecho Local en la Alta Edad Media")
            if st.button("👁️ Mostrar Respuesta Maestra - Tema 5", key="b5"):
                st.markdown('<div class="respuesta-maestra-box"><b>Respuesta Oficial:</b> El derecho local altomedieval surgió por la fragmentación política tras la invasión del 711 d.C. y la urgencia de repoblar las fronteras cristianas. Las Cartas Pueblas constituyeron el tipo documental más primario, regulando solo condiciones económicas y agrarias para los colonos. Los Fueros evolucionaron otorgando estatutos jurídicos privilegiados, exención fiscal y autonomía organizativa municipal. Los fueros breves fijaban exenciones básicas para la supervivencia fronteriza. Los fueros extensos (siglos XII-XIII, como el de Cuenca) estructuraron ordenamientos íntegros penales, civiles y procesales. Este particularismo creó un mosaico normativo autónomo que debilitó el poder central real.</div>', unsafe_allow_html=True)
            st.text_area("✍️ Redacta tu desarrollo:", key="ie5", height=110)
        elif st.session_state.preg_act == 3:
            st.markdown("#### Eje N.º 3: Fuero de Albedrío y Fazañas")
            if st.button("👁️ Mostrar Respuesta Maestra - Tema 10", key="b10"):
                st.markdown('<div class="respuesta-maestra-box"><b>Respuesta Oficial:</b> El derecho castellano altomedieval fue consuetudinario, popular, no escrito e independiente del Liber. En el 843 d.C., Castilla rechazó formalmente las leyes visigodas de León quemando los textos. Adoptó el Fuero de Albedrío, un sistema donde jueces de la comunidad resolvían litigios según equidad y costumbres. Las Fazañas eran estas sentencias judiciales que operaban de inmediato como precedentes vinculantes. Ante una situación nueva fronteriza, el fallo del juez se convertía en la regla jurídica obligatoria para casos futuros, creando un orden dinámico y flexible.</div>', unsafe_allow_html=True)
            st.text_area("✍️ Redacta tu desarrollo:", key="ie10", height=110)
        elif st.session_state.preg_act == 4:
            st.markdown("#### Eje N.º 4: Formación del Derecho Común")
            if st.button("👁️ Mostrar Respuesta Maestra - Tema 13", key="b13"):
                st.markdown('<div class="respuesta-maestra-box"><b>Respuesta Oficial:</b> El Ius Commune integró el derecho romano justinianeo, el canónico y el feudal en la Baja Edad Media. Inició en el siglo XI al redescubrirse el Digesto y fundarse la Escuela de Bolonia (1088 d.C.) por Irnerio. Los Glosadores (siglos XI-XIII) hicieron un análisis teórico y exegético literal fijando el sentido mediante glosas interlineales. Los Comentaristas (siglos XIII-XV), liderados por Bartolo de Sassoferrato, adaptaron el derecho romano a la práctica de los tribunales. Se complementó con el Decreto de Graciano (1140 d.C.), que armonizó cánones de la Iglesia, sirviendo a los monarcas para centralizar el poder.</div>', unsafe_allow_html=True)
            st.text_area("✍️ Redacta tu desarrollo:", key="ie13", height=110)
        elif st.session_state.preg_act == 5:
            st.markdown("#### Eje N.º 5: El Derecho Territorial en Asturias-León")
            if st.button("👁️ Mostrar Respuesta Maestra - Tema 18", key="b18"):
                st.markdown('<div class="respuesta-maestra-box"><b>Respuesta Oficial:</b> Asturias-León defendió la continuidad legalista escrita del reino visigodo mediante el neogoticismo, oponiéndose al albedrío castellano. Aplicó rigurosamente el Liber Iudiciorum en el tribunal regio (Palatium). La territorialización se consolidó en el 1017 d.C. con las leyes territoriales de Alfonso V en las Cortes de León. En 1241 d.C., Fernando III ordenó su traducción oficial al romance bajo el nombre de Fuero Juzgo. Este texto unificado rigió las ciudades reconquistadas y se proyectó a América, aplicándose formalmente en tribunales chilenos hasta el siglo XIX ante la falta de un Código Penal patrio.</div>', unsafe_allow_html=True)
            st.text_area("✍️ Redacta tu desarrollo:", key="ie18", height=110)
        elif st.session_state.preg_act == 6:
            st.markdown("#### Eje N.º 6: Proyección de la Tradición Legalista en Chile")
            if st.button("👁️ Mostrar Respuesta Maestra - Tema 6", key="b6"):
                st.markdown('<div class="respuesta-maestra-box"><b>Respuesta Oficial:</b> La tradición legalista del Liber Iudiciorum demostró una persistencia jurídica colosal. Tras su traducción al castellano como Fuero Juzgo en 1241, se incorporó a las Leyes de Toro y a la Nueva Recopilación, traspasándose íntegramente al Derecho Indiano que rigió en América. En la época republicana de Chile, a falta de una codificación penal propia, las antiguas leyes castellano-visigodas siguieron plenamente vigentes. El hito culbre ocurrió en el año 1856, oportunidad en la que la Corte de Apelaciones de Valparaíso aplicó formalmente las disposiciones criminales del Fuero Juzgo visigodo para fallar un delito de incendio intencional, proyectando de manera extraordinaria una ley del siglo VII en los albores del Chile moderno.</div>', unsafe_allow_html=True)
            st.text_area("✍️ Redacta tu desarrollo:", key="ie6", height=110)

        st.markdown("<br>", unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        with c1:
            if st.session_state.preg_act > 1:
                if st.button("⬅️ Eje Anterior", key="esc_atras"):
                    st.session_state.preg_act -= 1
                    st.rerun()
        with c2:
            if st.session_state.preg_act < 6:
                if st.button("Siguiente Eje ➡️", key="esc_sig"):
                    st.session_state.preg_act += 1
                    st.rerun()

    else:
        st.info(f"📋 **Pregunta Actual: {st.session_state.preg_act} de 6** -- Responda para activar la navegación.")
        
        if st.session_state.preg_act == 1:
            st.markdown("##### **Pregunta 1 de 6** -- España Visigoda")
