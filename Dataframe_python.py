import pandas as pd

datos = {"Nombres": ["Marisol", "Pedro", "Carlos", "Felipe"],
         "Calificaciones": ["100", "50", "60", "90"],
         "Deportes": ["Futbol", "Baloncesto", "Rugby", "Voleibol"],
         "Materias": ["cálculo", "Física", "Química", "constitución"]}
df = pd.DataFrame(datos)
df["Calificaciones"] = df.Calificaciones.astype(int)
print(df)
