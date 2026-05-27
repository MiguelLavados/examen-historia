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

# --- BASE DE DATOS MAESTRA (6 EJES ACADÉMICOS) ---
banco_preguntas = [
    {
        "id": 1,
        "titulo": "1. Importancia de los Concilios en la España Visigoda (Toledo 3, 4, 8, 12 y 13)",
        "enunciado": "¿Mediante qué mecanismo legal las decisiones aprobadas unánimemente en los Concilios de Toledo se promulaban como leyes civiles del Reino Visigodo?",
        "opciones": ["A) La Lex in confirmatione concilii dictada por el monarca.", "B) El Tomus Regius del Oficio Palatino de forma unilateral.", "C) El Fuero de Albedrío decretado oralmente por el Senatus.", "D) El canon conciliar en cuanto disposición de valor puramente eclesiástico."],
        "letra_correcta": "A)",
        "desarrollo": "Los Concilios de Toledo se consolidaron como asambleas político-religiosas y órganos colegisladores fundamentales tras la conversión al catolicismo en el 589 d.C. El monarca junto al Aula Real fijaba la agenda con el Tomus Regius, transformando los acuerdos en cánones convalidados mediante la Lex in confirmatione concilii. El III Concilio decretó la conversión de Recaredo, unificando el territorio. El IV Concilio, presidido por San Isidoro, institucionalizó la monarquía electiva (canon 75) contra el morbo gótico. El VIII Concilio redactó la primera edición del Liber Iudiciorum bajo Recesvinto. El XII Concilio validó a Ervigio y endureció las leyes antisemitas. El XIII Concilio otorgó el Habeas Corpus Visigodo, protegiendo a los nobles de arrestos reales arbitrarios."
    },
    {
        "id": 2,
        "titulo": "5. El Derecho Local en la Alta Edad Media: Cartas Pueblas y Fueros",
        "enunciado": "¿Qué diferencia jurídica fundamental existía en la Alta Edad Media entre las Cartas Pueblas primarias y los Fueros extensos municipales?",
        "opciones": ["A) Las Cartas Pueblas eran de naturaleza eclesiástica y los Fueros extensos regulaban la guerra feudal.", "B) Las Cartas Pueblas regulaban solo condiciones económicas y agrarias de asentamiento; los Fueros extensos eran ordenamientos jurídicos municipales integrales.", "C) Las Cartas Pueblas eran de origen romano escrito y los Fueros extensos costumbres puramente orales.", "D) Las Cartas Pueblas regían en la España islámica y los Fueros extensos en la zona de influencia atlántica."],
        "letra_correcta": "B)",
        "desarrollo": "El derecho local altomedieval surgió por la fragmentación política tras la invasión del 711 d.C. y la urgencia de repoblar las fronteras cristianas. Las Cartas Pueblas constituyeron el tipo documental más primario, regulando solo condiciones económicas y agrarias para los colonos. Los Fueros evolucionaron otorgando estatutos jurídicos privilegiados, exención fiscal y autonomía organizativa municipal. Los fueros breves fijaban las exenciones básicas para la supervivencia fronteriza. Los fueros extensos (siglos XII-XIII, como el de Cuenca) estructuraron ordenamientos íntegros penales, civiles y procesales. Este particularismo creó un mosaico normativo autónomo que debilitó el poder central real."
    },
    {
        "id": 3,
        "titulo": "10. Características del Derecho Territorial en Castilla: Fuero de Albedrío y Fazañas",
        "enunciado": "En el contexto del desarrollo del derecho territorial castellano medieval, ¿qué eran técnicamente las denominadas Fazañas?",
        "opciones": ["A) Leyes escritas de factura romana dictadas de forma centralizada por la corona.", "B) Contratos agrarios bilaterales celebrados de forma solemne ante los funcionarios reales.", "C) Sentencias de los jueces de albedrío que se convertían de inmediato en precedentes judiciales vinculantes.", "D) Mecanismos penales de ordalías o juicios de Dios regulados por las costumbres locales."],
        "letra_correcta": "C)",
        "desarrollo": "El derecho castellano altomedieval fue consuetudinario, popular, no escrito e independiente del Liber. En el 843 d.C., Castilla rechazó formalmente las leyes visigodas de León quemando los textos. Adoptó el Fuero de Albedrío, un sistema donde jueces de la comunidad resolvían litigios según equidad y costumbres. Las Fazañas eran estas sentencias judiciales que operaban de inmediato como precedentes vinculantes. Ante una situación nueva fronteriza, el fallo del juez se convertía en la regla jurídica obligatoria para casos futuros, creando un orden dinámico y flexible."
    },
    {
        "id": 4,
        "titulo": "13. Formación del Derecho Común Romano Canónico: Glosadores y Comentaristas",
        "enunciado": "¿Cuál era el objetivo metodológico y práctico central de la Escuela de los Comentaristas o Postglosadores en comparación con la labor teórica de los Glosadores?",
        "opciones": ["A) Aplicar y adaptar de forma práctica el derecho romano justinianeo a las realidades y litigios reales de los tribunales bajomedievales.", "B) Estudiar de manera exclusiva la exégesis literal de las costumbres consuetudinarias germánicas.", "C) Limitarse a fijar de forma dogmática el significado original del texto de Justiniano mediante glosas marginales.", "D) Redactar la profesión oficial de fe cristiana del Credo Niceno en concilios ecuménicos."],
        "letra_correcta": "A)",
        "desarrollo": "El Ius Commune integró el derecho romano justinianeo, el canónico y el feudal en la Baja Edad Media. Inició en el siglo XI al redescubrirse el Digesto y fundarse la Escuela de Bolonia (1088 d.C.) por Irnerio. Los Glosadores (siglos XI-XIII) hicieron un análisis teórico y exegético literal fijando el sentido mediante glosas interlineales. Los Comentaristas (siglos XIII-XV), liderados por Bartolo de Sassoferrato, adaptaron el derecho romano a la práctica de los tribunales. Se complementó con el Decreto de Graciano (1140 d.C.), que armonizó cánones de la Iglesia, sirviendo a los monarcas para centralizar el poder."
    },
    {
        "id": 5,
        "titulo": "18. El Derecho Territorial en el Reino de Asturias-León y la vigencia del Liber Iudiciorum",
        "enunciado": "¿Cuál fue la característica institucional esencial que diferenció al Derecho Territorial de Asturias-León del modelo consuetudinario implementado en Castilla?",
        "opciones": ["A) El predominio absoluto del derecho consuetudinario no escrito y la imposición del Fuero de Albedrío.", "B) Un sistema marcadamente legalista basado en la vigencia, primacía y aplicación formal de las leyes del Liber Iudiciorum.", "C) La adopción e internalización del derecho islámico derivado de la fragmentación de las taifas.", "D) El rechazo absoluto de las leyes reales escritas en latín clásico y la quema de textos normativos."],
        "letra_correcta": "B)",
        "desarrollo": "Asturias-León defendió la continuidad legalista escrita del reino visigodo mediante el neogoticismo, oponiéndose al albedrío castellano. Aplicó rigurosamente el Liber Iudiciorum en el tribunal regio (Palatium). La territorialización se consolidó en el 1017 d.C. con las leyes territoriales de Alfonso V en las Cortes de León. En 1241 d.C., Fernando III ordenó su traducción oficial al romance bajo el nombre de Fuero Juzgo. Este texto unificado rigió las ciudades reconquistadas y se proyectó a América, aplicándose formalmente en tribunales chilenos hasta el siglo XIX ante la falta de un Código Penal patrio."
    },
    {
        "id": 6,
        "titulo": "Proyección Histórica: Vigencia del Liber Iudiciorum (Fuero Juzgo) en los Tribunales de Chile",
        "enunciado": "¿Qué hito de la judicatura republicana en el Chile del siglo XIX demuestra la extraordinaria permanencia de la tradición legalista visigoda?",
        "opciones": ["A) El uso del Fuero de Albedrío por parte de los jueces de Valparaíso para dirimir contratos comerciales marítimos.", "B) La aplicación de normas del Fuero Juzgo (Liber Iudiciorum) por la Corte de Valparaíso en 1856 para sancionar un delito de incendio ante la ausencia de un Código Penal nacional.", "C) La obligatoriedad legal de rendir ordalías de hierro candente en los juicios criminales rurales de Santiago.", "D) El uso del Decreto de Graciano canónico para regular de forma privativa la propiedad raíz civil."],
        "letra_correcta": "B)",
