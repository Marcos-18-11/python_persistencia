"""

Proyecto gestión de alumnos:

-Alta de alumnos: A través de una ventana, se solicitan los datos de un
nuevo alumno y se guardan en la base de datos. No se admiten dnis duplicados
si se proporciona un dni que ya existe, el alumno no se añade
y se avisa mediante un mensaje al usuario

-Busqueda de alumnos por curso. Se selecciona un curso en un combo
y debajo se muestra una tabla con los datos de todos los alumnos
de ese curso. En cada fila, aparecerá un botón para borrar a ese alumno

-Busqueda de alumno por dni. Se introduce el dni de un alumno
y se muestran todos sus datos, si no existe, mensaje de advertencia.

"""

import streamlit as st
import mysql.connector as con

def crear_conexion():
    db = con.connect(
        host="localhost",
        user="root",
        password="root",
        port=3306,
        database="universidad"
    )
    return db
def buscar_por_curso(curso):
    sql = "select distinct nombre,dni  from alumnos where curso=%s"
    db = crear_conexion()
    cursor = db.cursor(dictionary=True)
    cursor.execute(sql, (curso,))
    resultado = cursor.fetchall()
    cursor.close()
    db.close()
    return resultado
def alta_alumno(dni, nombre, email, curso, nota):

    db = crear_conexion()
    cursor = db.cursor()
    sql_buscar = "select dni from alumnos where dni=%s"
    cursor.execute(sql_buscar, (dni,))
    resultado = cursor.fetchone()

    if resultado:
        cursor.close()
        db.close()
        return False

    sql = """insert into alumnos
    (dni,nombre,email,curso,nota)
    values (%s,%s,%s,%s,%s)"""

    cursor.execute(sql, (dni, nombre, email, curso, nota))
    db.commit()
    cursor.close()
    db.close()
    return True

def buscar_por_dni(dni):
    sql = "select * from alumnos where dni=%s"
    db = crear_conexion()
    cursor = db.cursor(dictionary=True)
    cursor.execute(sql, (dni,))
    resultado = cursor.fetchone()
    cursor.close()
    db.close()
    return resultado

def borrar_alumno(dni):
    sql = "delete from alumnos where dni=%s"
    db = crear_conexion()
    cursor = db.cursor()
    cursor.execute(sql, (dni,))
    eliminados = cursor.rowcount
    db.commit()
    cursor.close()
    db.close()
    return eliminados > 0
def actualizar(dni,nombre,email,curso,nota):
    sql="update alumnos set nombre=%s, email=%s, curso=%s, nota=%s where dni=%s"
    db=crear_conexion()
    cursor=db.cursor()
    cursor.execute(sql,(nombre,email,curso,nota,dni))
    db.commit()
    cursor.close()
    db.close()
    return True
tab_alta, tab_busqueda_por_curso, tab_busqueda_por_dni, tab_baja_alumno,tab_actualizar = st.tabs([
    "Alta de alumnos",
    "Buscar por curso",
    "Buscar por DNI",
    "Baja alumno",
    "Actualización de datos"
])

with tab_alta:

    st.title("Alta de alumnos")

    nombre = st.text_input("Introduce nombre:")
    email = st.text_input("Introduce email:")
    curso = st.selectbox("Seleccione curso:",["python", "Java", "C++", "RUST"])
    dni = st.text_input("Introduce dni:")
    nota = st.number_input("Introduce la nota", min_value=0, max_value=10)

    if st.button("Insertar"):
        if alta_alumno(dni, nombre, email, curso, nota):
            st.success("Alumno insertado correctamente")
        else:
            st.warning("Ya existe un alumno con ese DNI")
        

with tab_busqueda_por_curso:

    st.title("Buscar por curso")
    curso_1 = st.selectbox(
        "Selecciona un curso:",
        ["python", "Java", "C++", "RUST"]
    )

    alumnos = buscar_por_curso(curso_1)
    if alumnos:
        for alumno in alumnos:
            st.write("Nombre:", alumno["nombre"])
            st.write("DNI:", alumno["dni"])
            if st.button("Borrar", key=alumno["dni"]):
                if borrar_alumno(alumno["dni"]):
                    st.success("ELIMINADO!")
    else:
        st.warning("No hay alumnos en este curso")
with tab_busqueda_por_dni:

    st.title("Buscar por DNI")

    dni_1 = st.text_input("Introduce DNI:")

    if st.button("Buscar"):
        alumno = buscar_por_dni(dni_1)
        if alumno:
            st.table([alumno])
        else:
            st.warning("No existe ningún alumno con ese DNI")

with tab_baja_alumno:

    st.title("Dar de baja")
    dni_2 = st.text_input("Introduce DNI del alumno a eliminar:")
    if st.button("Eliminar"):
        if borrar_alumno(dni_2):
            st.success("Alumno eliminado correctamente")
        else:
            st.warning("No existe ningún alumno con ese DNI")
            
#def actualizar(dni,nombre,email,curso,nota):
with tab_actualizar:
    st.title("Actualizar")
    actualizador = st.text_input("Introduzca DNI:")
    if st.button("Buscar", key=2):
        alumno = buscar_por_dni(actualizador)
        if alumno:
            st.session_state["alumno_actualizar"] = alumno
        else:
            st.session_state["alumno_actualizar"] = None
            st.warning("No existe ningún alumno con ese DNI")

    if st.session_state.get("alumno_actualizar"):
    
        alumno = st.session_state["alumno_actualizar"]
        st.table([alumno])
        nuevo_nombre = st.text_input("Introduzca nombre:", value=alumno["nombre"] )
        nuevo_email = st.text_input("Introduzca email:",value=alumno["email"] )
        nuevo_curso = st.selectbox("Seleccion de curso:",["python", "Java", "C++", "RUST"])
        nuevo_nota = st.number_input("Introduzca la nota",min_value=0,max_value=10,value=alumno["nota"])

        if st.button("Actualizar alumno"):
            actualizar(alumno["dni"],nuevo_nombre,nuevo_email,nuevo_curso,nuevo_nota)
            st.toast("Actualización realizada correctamente")
            st.session_state["alumno_actualizar"] = None
