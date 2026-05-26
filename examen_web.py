import streamlit as st
import random
from datetime import datetime

# Configuración de la página web optimizada para móviles
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

# Control de Caducidad
if datetime.now() > datetime(2026, 6, 30):
    st.error("❌ ENTORNO DE EVALUACIÓN CADUCADO")
    st.stop()

# Inicialización de variables de estado fijas en memoria (Evita lag)
if 'preguntas' not in st.session_state:
    st.session_state.preguntas = []
    st.session_state.respuestas_usuario = {}
    st.session_state.indice_actual = 0
    st.session_state.examen_activo = False
    st.session_state.finalizado = False

# Título de la App
st.title("📚 COGNUSS EXTENSO V2")
st.caption("Programa creado por Miguel López Lavados | Caduca: 30-Jun-2026")
st.markdown("---")

# Panel de control lateral
st.sidebar.header("⚙️ Menú Examen")
bloques = list(banco_extenso.keys())
opcion_bloque = st.sidebar.selectbox("Selecciona Bloque:", ["--- Seleccionar ---"] + bloques + ["Todo Mezclado"])
modo = st.sidebar.radio("Modalidad:", ["Alternativas", "Escrito (Desarrollo)"])

if st.sidebar.button("🚀 Iniciar Test"):
    if opcion_bloque != "--- Seleccionar ---":
        if opcion_bloque == "Todo Mezclado":
            st.session_state.preguntas = [q for b in banco_extenso.values() for q in b]
            random.shuffle(st.session_state.preguntas)
        else:
            st.session_state.preguntas = banco_extenso[opcion_bloque].copy()
        
        st.session_state.respuestas_usuario = {}
        st.session_state.indice_actual = 0
        st.session_state.examen_activo = True
        st.session_state.finalizado = False
    else:
        st.sidebar.error("Selecciona un bloque válido.")

# Lógica de navegación rápida (Pregunta por pregunta)
if st.session_state.examen_activo and not st.session_state.finalizado:
    total = len(st.session_state.preguntas)
    idx = st.session_state.indice_actual
    p = st.session_state.preguntas[idx]
    
    st.write(f"### 📋 Pregunta {idx + 1} de {total}")
    st.info(p['p'])
    
    # Capturar respuesta sin refrescar bruscamente la página
    if modo == "Alternativas":
        opcion_guardada = st.session_state.respuestas_usuario.get(idx, None)
        indice_defecto = p['a'].index(opcion_guardada) if opcion_guardada in p['a'] else 0
        
        resp = st.radio("Elige tu opción:", p['a'], index=indice_defecto, key=f"radio_{idx}")
        st.session_state.respuestas_usuario[idx] = resp
    else:
        texto_guardado = st.session_state.respuestas_usuario.get(idx, "")
        resp_t = st.text_area("Escribe tu respuesta analítica:", value=texto_guardado, key=f"text_{idx}")
        st.session_state.respuestas_usuario[idx] = resp_t
        
        st.markdown("**Criterio de Evaluación de Cátedra:**")
        st.caption(p['e'])
        evalua = st.radio("¿Tu respuesta cumple el criterio?", ["No evaluado", "Sí (Sumar punto)", "No (Cero puntos)"], key=f"eval_{idx}")
        st.session_state.respuestas_usuario[f"eval_{idx}"] = evalua

    st.markdown("---")
    
    # Botones de navegación en horizontal para móviles
    col1, col2, col3 = st.columns()
    
    with col1:
        if idx > 0:
            if st.button("⬅️ Anterior"):
                st.session_state.indice_actual -= 1
                st.rerun()
                
    with col2:
        if idx < total - 1:
            if st.button("Siguiente ➡️"):
                st.session_state.indice_actual += 1
                st.rerun()
                
    with col3:
        if st.button("📥 Terminar"):
            st.session_state.finalizado = True
            st.rerun()

# Pantalla final de Resultados (Súper rápida)
elif st.session_state.finalizado:
    st.success("## 📊 Resultados de la Evaluación")
    puntos = 0
    total = len(st.session_state.preguntas)
    
    for idx, p in enumerate(st.session_state.preguntas):
        st.markdown(f"**{idx + 1}. {p['p']}**")
        resp_u = st.session_state.respuestas_usuario.get(idx, "")
        
        if modo == "Alternativas":
            if resp_u and resp_u.startswith(p['c']):
                st.success(f"Correcto. Respondiste: {resp_u}")
                puntos += 1
            else:
                st.error(f"Incorrecto. Respondiste: {resp_u} | Correcta: {p['c']}")
        else:
            eval_u = st.session_state.respuestas_usuario.get(f"eval_{idx}", "")
            if eval_u == "Sí (Sumar punto)":
                puntos += 1
                st.success("Punto aprobado en autoevaluación.")
            else:
                st.info("No sumó puntaje.")
