import streamlit as st
import random
from datetime import datetime

# Configuración de la página web
st.set_page_config(page_title="COGNUSS Extenso V2", page_icon="⚖️", layout="centered")

# Banco de Datos Original
banco_extenso = {
    "1. Periodo Visigodo y Liber Iudiciorum": [
        {"p": "¿En qué consiste la teoría de la 'personalidad de las leyes'?", "a": ["A) Aplicación por igual a todo habitante.", "B) Visigodos e hispanorromanos bajo ordenamientos separados."], "c": "B", "e": "Eurico para visigodos y Breviario de Alarico para hispanorromanos."},
        {"p": "¿Qué hito ocurrió en el III Concilio de Toledo (589)?", "a": ["A) Cánones con fuerza de ley civil y unión Iglesia-Estado.", "B) Abolición del derecho romano vulgar."], "c": "A", "e": "Conversión al catolicismo de Recaredo para unificar espiritualmente el reino."},
        {"p": "¿Qué norma se fijó en el IV Concilio de Toledo (633)?", "a": ["A) Monarquía puramente hereditaria.", "B) Carácter electivo de la monarquía por magnates y obispos."], "c": "B", "e": "Buscaba frenar las constantes guerras civiles ('morbus gothicus')."},
        {"p": "¿Qué impacto territorial tuvo el Liber Iudiciorum (654)?", "a": ["A) Unificó el derecho territorialmente derogando textos previos.", "B) Otorgó plena autonomía a los duques locales."], "c": "A", "e": "Puso fin a la dualidad jurídica penal y civil peninsular."},
        {"p": "¿Qué reforma introdujo Ervigio al Liber en 681?", "a": ["A) Dura legislación de persecución y exclusión contra judíos.", "B) Tradujo los manuscritos oficiales al romance castellano."], "c": "A", "e": "Adaptó las normas a las presiones doctrinales de la Iglesia."},
        {"p": "¿Qué fue la versión Vulgata del Liber (Siglo VIII)?", "a": ["A) Copia custodiada de forma secreta en Roma.", "B) Edición no oficial con adiciones que ayudó a sobrevivir el texto."], "c": "B", "e": "Juristas del norte añadieron costumbres locales tras la caída toledana."}
    ],
    "2. Alta Edad Media y Derecho Local": [
        {"p": "¿Cómo afectó la invasión de 711 al norte cristiano?", "a": ["A) Colapso estatal, dispersión legal y auge de costumbre oral.", "B) Aplicación inmediata del Corpus Iuris en Asturias."], "c": "A", "e": "El aislamiento geográfico fragmentó la ley escrita en la península."},
        {"p": "¿Qué eran las Fazañas castellanas medievales?", "a": ["A) Sentencias de jueces (albedrío) ante la falta de ley escrita.", "B) Leyes territoriales obligatorias del rey de León."], "c": "A", "e": "Fijaban precedentes basados en las costumbres locales y la equidad."},
        {"p": "¿Cuál era la diferencia entre Fueros Breves y Extensos?", "a": ["A) Breves daban exenciones básicas; extensos regulaban la vida civil.", "B) Breves para siervos, extensos para la alta nobleza."], "c": "A", "e": "Los extensos (siglos XII-XIII) protegían la autonomía frente al rey."},
        {"p": "¿Cuál era el fin de las Cartas Pueblas en la frontera?", "a": ["A) Financiar con tributos las campañas militares.", "B) Atraer población mediante propiedad de tierra y perdón de delitos."], "c": "B", "e": "Se requería asegurar militarmente las zonas colindantes con Al-Ándalus."}
    ],
    "3. Baja Edad Media y Derecho Comun": [
        {"p": "¿Qué fuentes combinadas dieron origen al Derecho Común?", "a": ["A) Corpus Iuris Civilis, Derecho Canónico y Derecho Feudal.", "B) Fuero Juzgo, Siete Partidas y Ordenamiento de Alcalá."], "c": "A", "e": "Surgió formalmente a partir del siglo XII en la Universidad de Bolonia."},
        {"p": "¿Cuál era el método de estudio de los Glosadores?", "a": ["A) Notas aclaratorias marginales (glosas) al texto literal romano.", "B) Redactar códigos modernos basados en la razón natural."], "c": "A", "e": "Su enfoque era estrictamente exegético para recuperar la pureza clásica."},
        {"p": "¿En qué se diferenciaban los Postglosadores o Comentaristas?", "a": ["A) Abandonaron el uso técnico del latín académico.", "B) Adaptaron los textos romanos a la práctica de su época."], "c": "B", "e": "Su método pragmático permitió aplicar el derecho romano en tribunales."},
        {"p": "¿Por qué las monarquías impulsaron el Derecho Común?", "a": ["A) Sostenía que la voluntad del monarca tiene fuerza de ley.", "B) Fomentaba libertades democráticas vecinales."], "c": "A", "e": "Utilizaron el derecho técnico para socavar los privilegios feudales."},
        {"p": "¿Por qué las Siete Partidas no se aplicaron de inmediato?", "a": ["A) Resistencia de nobles y municipios que defendían sus fueros.", "B) El clero consideró que contradecía los decretales."], "c": "A", "e": "El fuerte absolutismo del código real provocó el rechazo estamental."}
    ],
    "4. Unificacion Legislativa de Castilla": [
        {"p": "¿Qué conflicto resolvió el Ordenamiento de Alcalá (1348)?", "a": ["A) Fijó una escala jerárquica de fuentes obligatorio.", "B) Decretó la sumisión total al tribunal de la Rota."], "c": "A", "e": "Estableció con claridad qué leyes aplicar en primer y segundo orden."},
        {"p": "Según Alcalá, ¿cuál era la posición de las Siete Partidas?", "a": ["A) Aplicación inmediata en primer lugar penal.", "B) Tercer lugar, aplicándose de forma supletoria."], "c": "B", "e": "Entraron en vigor oficial subordinadas a leyes reales y fueros usar."},
        {"p": "¿Qué fue el Ordenamiento de Montalvo (1484)?", "a": ["A) Recopilación oficial para unificar leyes y pragmáticas dispersas.", "B) Tratado de paz militar con las milicias de frontera."], "c": "A", "e": "Encargado por los Reyes Católicos para robustecer el Estado Moderno."}
    ]
}

# Verificación de Caducidad
if datetime.now() > datetime(2026, 6, 30):
    st.error("❌ ENTORNO DE EVALUACIÓN CADUCADO")
    st.warning("Este programa de estudio expiró el 30 de junio de 2026. Comunícate con el administrador para una actualización.")
    st.info("Creado por Miguel López Lavados — mlopezlavado@gmail.com")
    st.stop()

# Encabezado Visual
st.title("📚 COGNUSS EXTENSO V2")
st.subheader("HISTORIA DEL DERECHO MEDIEVAL")
st.caption("Programa creado por Miguel López Lavados | Contacto: mlopezlavado@gmail.com")
st.caption("Derechos Reservados — Caducidad: 30 de Junio de 2026")
st.markdown("---")

# Inicialización de variables de estado
if 'preguntas' not in st.session_state:
    st.session_state.preguntas = []
    st.session_state.puntos = 0
    st.session_state.respondido = {}
    st.session_state.test_iniciado = False

# Sidebar de Configuración del Examen
st.sidebar.header("⚙️ Configuración del Test")
bloques = list(banco_extenso.keys())
opcion_bloque = st.sidebar.selectbox("Selecciona Bloque Temático:", ["--- Seleccionar ---"] + bloques + ["Evaluar Todo el Cedulario Mezclado"])
modo = st.sidebar.radio("Modalidad de Evaluación:", ["Modo Alternativas", "Modo Escrito (Desarrollo)"])

if st.sidebar.button("🚀 Iniciar / Reiniciar Examen"):
    if opcion_bloque != "--- Seleccionar ---":
        if opcion_bloque == "Evaluar Todo el Cedulario Mezclado":
            st.session_state.preguntas = [q for b in banco_extenso.values() for q in b]
            random.shuffle(st.session_state.preguntas)
        else:
            st.session_state.preguntas = banco_extenso[opcion_bloque].copy()
        
        st.session_state.puntos = 0
        st.session_state.respondido = {}
        st.session_state.test_iniciado = True
    else:
        st.sidebar.error("Por favor selecciona un bloque temático.")

# Desarrollo del Cuestionario
if st.session_state.test_iniciado:
    st.write(f"### 📋 Evaluando: {opcion_bloque}")
    
    with st.form("formulario_examen"):
        for idx, p in enumerate(st.session_state.preguntas):
            st.markdown(f"**Pregunta {idx + 1}:** {p['p']}")
            
            if modo == "Modo Alternativas":
                opcion_usuario = st.radio(f"Selecciona tu respuesta para la pregunta {idx+1}: ", p['a'], key=f"p_{idx}")
                st.session_state.respondido[idx] = opcion_usuario
            else:
                st.text_area("Redacta tu respuesta analítica:", key=f"t_{idx}")
                evalua = st.radio("¿Tu respuesta abarcó los conceptos del criterio oficial?", ["No evaluar aún", "Sí (Sumar punto)", "No (Cero puntos)"], key=f"e_{idx}")
                st.session_state.respondido[idx] = evalua
            
            st.markdown("---")
        
        enviar = st.form_submit_button("📥 Finalizar y Obtener Nota")
        
        if enviar:
            puntos_obtenidos = 0
            total_preguntas = len(st.session_state.preguntas)
            
            st.write("## 📊 Resultados de la Evaluación")
            
            for idx, p in enumerate(st.session_state.preguntas):
                st.write(f"**Pregunta {idx + 1}:** {p['p']}")
                
                if modo == "Modo Alternativas":
                    resp_u = st.session_state.respondido.get(idx)
                    if resp_u and resp_u.startswith(p['c']):
                        st.success(f"¡Correcto! Elegiste {resp_u}")
                        puntos_obtenidos += 1
                    else:
                        st.error(f"Incorrecto. Elegiste {resp_u}. La opción correcta era la {p['c']}.")
                else:
                    evaluacion_u = st.session_state.respondido.get(idx)
                    if evaluacion_u == "Sí (Sumar punto)":
                        puntos_obtenidos += 1
                        st.success("Punto sumado por autoevaluación.")
                    else:
                        st.info("No se sumó puntaje.")
                
                st.info(f"💡 **Fundamento de Cátedra:** {p['e']}")
                st.markdown("---")
            
            nota = round((puntos_obtenidos / total_preguntas) * 6 + 1, 1) if total_preguntas > 0 else 1.0
            
            st.metric(label="Puntaje Total", value=f"{puntos_obtenidos} de {total_preguntas}")
            if nota >= 4.0:
                st.balloons()
                st.success(f"🎉 ¡Aprobado! Tu nota estimada es: **{nota}**")
