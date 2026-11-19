import polars as pl
import matplotlib.pyplot as plt
df_dataframe_alumnos=pl.scan_csv("alumnos.csv")
df_dataframe_notas=pl.scan_csv("notas.csv")
df=df_dataframe_notas.join(df_dataframe_alumnos,on="id_alumno",how="inner")
print(df.collect())

def aplicar_filtros(curso, asignatura, grupo, evaluacion):

    filtros = []
    if curso != "Todos":
        filtros.append(pl.col("curso") == curso)
         
    if asignatura != "Todas":
        filtros.append(pl.col("asignatura") == asignatura)

    if grupo != "Todos":
        filtros.append(pl.col("grupo") == grupo)

    if evaluacion != "Todas":
        filtros.append(pl.col("evaluacion") == int(evaluacion))
        
    if filtros:
        return df.filter(pl.all_horizontal(filtros))
    return df
    

def contar_alumnos(curso,asignatura,grupo,evaluacion):
    
    resultado=aplicar_filtros(curso,asignatura,grupo,evaluacion).select(pl.col("id_alumno").n_unique()).collect()
    return resultado.item()

def calcular_media(curso,asignatura,grupo,evaluacion):
    resultado=aplicar_filtros(curso,asignatura,grupo,evaluacion).select(pl.col("nota").mean()).collect()
    return resultado.item()

def calcular_maxima(curso,asignatura,grupo,evaluacion):
    resultado=aplicar_filtros(curso,asignatura,grupo,evaluacion).select(pl.col("nota").max()).collect()
    return resultado.item()

def calcular_minima(curso,asignatura,grupo,evaluacion):
    resultado=aplicar_filtros(curso,asignatura,grupo,evaluacion).select(pl.col("nota").min()).collect()
    return resultado.item()

def calcular_aprobados(curso,asignatura,grupo,evaluacion):
    resultado=aplicar_filtros(curso,asignatura,grupo,evaluacion).select((pl.col("nota")>=5).mean()*100).collect()
    return resultado.item()

def estadisticas_asignatura(curso,asignatura,grupo,evaluacion):
    datos=aplicar_filtros(curso,asignatura,grupo,evaluacion)
    por_asignatura = datos.group_by(
    ["id_alumno", "nombre", "curso", "grupo", "asignatura"]
).agg(
    pl.col("nota").mean().alias("media_asignatura")
)
    resultado = por_asignatura.group_by(
    ["id_alumno", "nombre", "curso", "grupo"]
).agg(
    pl.col("media_asignatura").mean().round(2).alias("nota_media"),
    pl.col("media_asignatura").count().alias("asignaturas_evaluadas"),
    (pl.col("media_asignatura") >= 5).sum().alias("asignaturas_aprobadas")
)
    return resultado.sort(
            "nota_media",
            descending=True
        )
    
def grafico_notas_asignaturas(datos): #Recibe dataframe
    
    plt.bar(
        datos["asignatura"].to_list(),
        datos["nota_media"].to_list()
    )

    plt.title("Nota media por asignatura")
    plt.xlabel("Asignatura")
    plt.ylabel("Nota media")
    return plt
def grafico_evolucion_evaluaciones(datos):
    plt.plot(
        datos["evaluacion"].to_list(),
        datos["nota_media"].to_list(),
        marker="o"
    )

    plt.title("Evolución de las notas")
    plt.xlabel("Evaluación")
    plt.ylabel("Nota media")

    plt.xticks(datos["evaluacion"].to_list())
    plt.ylim(0, 10)

    plt.grid(alpha=0.3)
    return plt
#def rendimiento_alumno(): 
"""
def obtener_estadisticas_alumnos(curso, asignatura, evaluacion, grupo):

    datos = obtener_datos_filtrados(curso, asignatura, evaluacion, grupo    )

    por_asignatura = datos.group_by(["id_alumno", "nombre", "curso", "grupo", "asignatura"]).agg(
        pl.col("nota").mean().alias("media_asignatura")
    )
    resultado = por_asignatura.group_by(["id_alumno", "nombre", "curso", "grupo"]).agg(
        pl.col("media_asignatura").mean().round(2).alias("nota_media"),

        pl.col("media_asignatura").count().alias("asignaturas_evaluadas"),

        ((pl.col("media_asignatura") >= 5).sum()).alias("asignaturas_aprobadas")
    )

    return resultado.sort(
        "nota_media",
        descending=True
    )
"""
