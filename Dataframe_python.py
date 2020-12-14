
import pandas as pd

datos = pd.read_csv(
    "C:\\Users\\home\\Desktop\\DataFrame_py\\Data.csv", encoding="ISO-8859-1")
# datos = {"Nombres": ["Marisol", "Pedro", "Carlos", "Felipe"],
#        "Calificaciones": ["100", "50", "60", "90"],
#       "Deportes": ["Futbol", "Baloncesto", "Rugby", "Voleibol"],
#      "Materias": ["cálculo", "Física", "Química", "constitución"]}
#df = pd.DataFrame(datos)
# df["Calificaciones"] = df.Calificaciones.astype(
#   int)  # convertí los strings a int para sumarlos
# n = df.iloc[:, 1]  # seleccione la columna calificaciones
# h = n.sum()  # suma la columna
# u = df.describe() #descipción general de la columna 1
#t = df.replace(60, "N/A")
# utilice el .loc para acceder a un valor y modificarlo
#df.loc[1, "Calificaciones"] = 56
df = pd.DataFrame(datos)

# las primeras "" hacen referencia a la columna
#k = df.loc[df["Location"].str.endswith("New York")]
# y las segundas "" al tipo de dato qur vamos a filtrar
# k = df.columns # muestra la lista de columnas
# filtre la columna series y la columna Location
filtro = df[(df['Series'] == "Grand Slam") & (df['Location'] == "New York")]
filtro.to_csv("datos_nuevos.csv")
print(filtro.tail(10))
