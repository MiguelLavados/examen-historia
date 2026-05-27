import streamlit as st
import random
from datetime import date

st.set_page_config(page_title="COGNUSS Extenso V2", page_icon="🎓", layout="centered")

# Estilos CSS para el desvanecimiento de 25 segundos
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

# --- MENÚ LATERAL ---
st.sidebar.markdown("## ⚙️ Menú Examen")
opcion_bloque = st.sidebar.selectbox("Selecciona Bloque:", ["--- Seleccionar ---", "Bloque 5: Examen Repetición"])

st.sidebar.markdown("---")
st.sidebar.markdown("### 👥 Propiedad Intelectual & Créditos")
st.sidebar.info("* **Profesor Titular**: Dr. Oscar Enrique Dávila\n* **Recopilación (Escribana)**: Danitza Araya\n* **Desarrollador**: Miguel López Lavados\n* **Agente Colaborador IA**: IA\n* **Motor de Conocimientos**: COGNUSS 2\n\n--- \n🔒 **Derechos Reservados © 2026**\n📅 *Fecha de Caducidad: 30 de Jun-2026*")

# --- BASE DE DATOS UNIFICADA ---
banco_preguntas = [
    {
        "id": 1,
        "titulo": "1. Importancia de los Concilios en la España Visigoda (Toledo 3, 4, 8, 12 y 13)",
        "enunciado": "¿Mediante qué mecanismo legal las decisiones aprobadas unánimemente en los Concilios de Toledo se promulaban como leyes civiles del Reino?",
        "opciones": ["A) La Lex in confirmatione concilii dictada por el monarca.", "B) El Tomus Regius del Oficio Palatino.", "C) El Fuero de Albedrío del Senatus.", "D) El canon conciliar eclesiástico."],
        "letra_correcta": "A)",
        "desarrollo": "Los Concilios de Toledo se consolidaron como asambleas político-religiosas y órganos colegisladores fundamentales tras la conversión al catolicismo en el 589 d.C. El monarca junto al Aula Real fijaba la agenda con el Tomus Regius, transformando los acuerdos en cánones convalidados mediante la Lex in confirmatione concilii. El III Concilio decretó la conversión de Recaredo, unificando el territorio. El IV Concilio, presidido por San Isidoro, institucionalizó la monarquía electiva (canon 75) contra el morbo gótico. El VIII Concilio redactó la primera edición del Liber Iudiciorum bajo Recesvinto. El XII Concilio validó a Ervigio y endureció las leyes antisemitas. El XIII Concilio otorgó el Habeas Corpus Visigodo, protegiendo a los nobles de arrestos reales arbitrarios."
    },
    {
        "id": 5,
        "titulo": "5. El Derecho Local en la Alta Edad Media: Cartas Pueblas y Fueros",
        "enunciado": "¿Qué diferencia jurídica fundamental existía en la Alta Edad Media entre las Cartas Pueblas y los Fueros extensos?",
        "opciones": ["A) Las Cartas Pueblas eran eclesiásticas y los Fueros extensos regulaban la guerra civil.", "B) Las Cartas Pueblas regulaban solo condiciones económicas y agrarias de asentamiento; los Fueros extensos eran ordenamientos jurídicos municipales integrales.", "C) Las Cartas Pueblas eran escritas y los Fueros extensos costumbres orales.", "D) Las Cartas Pueblas regían en zona islámica y los Fueros en la atlántica."],
        "letra_correcta": "B)",
        "desarrollo": "El derecho local altomedieval surgió por la fragmentación política tras la invasión del 711 d.C. y la urgencia de repoblar las fronteras cristianas. Las Cartas Pueblas constituyeron el tipo documental más primario, regulando solo condiciones económicas y agrarias para los colonos. Los Fueros evolucionaron otorgando estatutos jurídicos privilegiados, exención fiscal y autonomía organizativa municipal. Los fueros breves fijaban exenciones básicas para la supervivencia fronteriza. Los fueros extensos (siglos XII-XIII, como el de Cuenca) estructuraron ordenamientos íntegros penales, civiles y procesales. Este particularismo creó un mosaico normativo autónomo que debilitó el poder central real."
    },
    {
        "id": 10,
        "titulo": "10. Características del Derecho Territorial en Castilla: Fuero de Albedrío y Fazañas",
        "enunciado": "En el derecho territorial castellano de la Alta Edad Media, ¿qué eran técnicamente las denominadas Fazañas?",
        "opciones": ["A) Leyes escritas dictadas de forma centralizada por el monarca.", "B) Contratos agrarios celebrados ante el Aula Real.", "C) Sentencias de los jueces de albedrío que se convertían en precedentes judiciales vinculantes.", "D) Mecanismos de ordalías de la Iglesia."],
        "letra_correcta": "C)",
        "desarrollo": "El derecho castellano altomedieval fue consuetudinario, popular, no escrito e independiente del Liber. En el 843 d.C., Castilla rechazó formalmente las leyes visigodas de León quemando los textos. Adoptó el Fuero de Albedrío, un sistema donde jueces de la comunidad resolvían litigios según equidad y costumbres. Las Fazañas eran estas sentencias judiciales que operaban de inmediato como precedentes vinculantes. Ante una situación nueva fronteriza, el fallo del juez se convertía en la regla jurídica obligatoria para casos futuros, creando un orden dinámico y flexible."
    },
    {
        "id": 13,
        "titulo": "13. Formación del Derecho Común Romano Canónico: Glosadores y Comentaristas",
        "enunciado": "¿Cuál era el objetivo central de la Escuela de los Comentaristas o Postglosadores en comparación con los Glosadores?",
        "opciones": ["A) Aplicar y adaptar de forma práctica el derecho romano a las realidades y litigios reales de los tribunales.", "B) Estudiar exégesis textual no escrita germánica.", "C) Limitarse a fijar el significado literal original mediante glosas.", "D) Redactar el Credo Niceno ecuménico."],
        "letra_correcta": "A)",
        "desarrollo": "El Ius Commune integró el derecho romano justinianeo, el canónico y el feudal en la Baja Edad Media. Inició en el siglo XI al redescubrirse el Digesto y fundarse la Escuela de Bolonia (1088 d.C.) por Irnerio. Los Glosadores (siglos XI-XIII) hicieron un análisis teórico y exegético literal fijando el sentido mediante glosas interlineales. Los Comentaristas (siglos XIII-XV), liderados por Bartolo de Sassoferrato, adaptaron el derecho romano a la práctica de los tribunales. Se complementó con el Decreto de Graciano (1140 d.C.), que armonizó cánones de la Iglesia, sirviendo a los monarcas para centralizar el poder."
    },
    {
        "id": 18,
        "titulo": "18. El Derecho Territorial en el Reino de Asturias-León",
        "enunciado": "¿Cuál fue la característica esencial que diferenció al Derecho Territorial del Reino de Asturias-León del modelo implementado en Castilla?",
        "opciones": ["A) El predominio del derecho consuetudinario no escrito y el Fuero de Albedrío.", "B) Un sistema marcadamente legalista basado en la vigencia y aplicación formal de las leyes del Liber Iudiciorum.", "C) La adopción del derecho islámico de las taifas.", "D) El rechazo absoluto de las leyes reales escritas en latín."],
        "letra_correcta": "B)",
        "desarrollo": "Asturias-León defendió la continuidad legalista escrita del reino visigodo mediante el neogoticismo, oponiéndose al albedrío castellano. Aplicó rigurosamente el Liber Iudiciorum en el tribunal regio (Palatium). La territorialización se consolidó en el 1017 d.C. con las leyes territoriales de Alfonso V en las Cortes de León. En 1241 d.C., Fernando III ordenó su traducción oficial al romance bajo el nombre de Fuero Juzgo. Este texto unificado rigió las ciudades reconquistadas y se proyectó a América, aplicándose formalmente en tribunales chilenos hasta el siglo XIX ante la falta de un Código Penal patrio."
    }
]

if opcion_bloque == "--- Seleccionar ---":
    st.title("🛡️ COGNUSS EXTENSO V2")
    st.subheader("Programa creado por Miguel López Lavados | Caduca: 30-Jun-2026")
    st.markdown("---")
    st.info("👈 Selecciona el Bloque 5 en el menú lateral izquierdo para cargar el examen de repetición.")

elif opcion_bloque == "Bloque 5: Examen Repetición":
    st.title("⚖️ Examen de Repetición")
    st.subheader("Cuestionario Maestro Integrado - Temas 1, 5, 10, 13 y 18")
    st.markdown("---")
    modo = st.radio("👉 **Selecciona la modalidad de evaluación:**", ["Cuestionario Escrito (Memorización Gradual)", "Test de Selección Múltiple (Alternativas Cortas)"], index=0)
    st.markdown("---")
    
    if modo == "Cuestionario Escrito (Memorización Gradual)":
        st.info("⏱️ **Método Gradual Activo**: Al presionar el botón, la respuesta oficial aparecerá por **25 segundos**.")
        for item in banco_preguntas:
            st.markdown(f"#### Tópico N.º {item['id']}: {item['titulo']}")
            if st.button(f"👁️ Mostrar Respuesta Maestra - Tema {item['id']}", key=f"btn_esc_{item['id']}"):
                st.markdown(f'<div class="respuesta-maestra-box"><b>Respuesta Oficial:</b> {item["desarrollo"]}</div>', unsafe_allow_html=True)
            st.text_area("✍️ Redacta tu desarrollo:", key=f"in_esc_{item['id']}", height=110)
            st.markdown("<br>", unsafe_allow_html=True)
        
    else:
        st.warning("⚠️ **Control de Memoria**: Ninguna opción viene marcada por defecto. Recibirá corrección inmediata.")
        respuestas_usuario = {}
        
        # Bucle automático para renderizar las 5 preguntas sin riesgo de cortes
        for idx, item in enumerate(banco_preguntas):
            st.markdown(f"##### **Pregunta {idx + 1}** -- *{item['titulo']}*")
            st.markdown(f"**Enunciado:** {item['enunciado']}")
