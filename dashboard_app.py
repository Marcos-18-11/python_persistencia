import streamlit as st
import repositorio_dashboard as rd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="📊 Dashboard de rendimiento académico",
    layout="wide"
)

st.title("📊 Dashboard de rendimiento académico")

st.sidebar.title("Filtros")

curso = st.sidebar.selectbox(
    "Curso",
    ["Todos", "Java", "Python"]   
)
asignatura = st.sidebar.selectbox(
    "Asignatura",
    ["Todas","Bases de datos", "Java", "Python"]   
)
grupo = st.sidebar.selectbox(
    "Grupo",
    ["Todos", "A", "B"]   
)
evaluacion = st.sidebar.selectbox(
    "Evaluación",
    ["Todas", "1", "2"]   
)

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric(
    "Alumnos evaluados",
    rd.contar_alumnos(curso, asignatura, grupo, evaluacion)
)

col2.metric(
    "Nota media",
    rd.calcular_media(curso, asignatura, grupo, evaluacion)
)

col3.metric(
    "Nota máxima",
    rd.calcular_maxima(curso, asignatura, grupo, evaluacion)
)

col4.metric(
    "Nota mínima",
    rd.calcular_minima(curso, asignatura, grupo, evaluacion)
)

col5.metric(
    "Aprobados",
    rd.calcular_aprobados(curso, asignatura, grupo, evaluacion)
)

st.header("Estadísticas por asignatura")

df=rd.estadisticas_asignatura(curso, asignatura, grupo, evaluacion)
st.dataframe(df, use_container_width=True)

#graficos
st.subheader("Representación gráfica")

tab1,tab2, tab3=st.tabs(["Notas por asignatura","Evolución de evaluaciones","Distribución de notas"])
with tab1:
    st.pyplot(rd.grafico_notas_asignaturas(rd.df))
with tab2:
    st.pyplot(rd.estadisticas_asignatura(rd.df))

