print("Hola mundo, esta es mi primera interfaz, bienvenidos")

a=45
b=875
c=74

def multi():
    print(a*b*c)

multi()

def funcion_info(ruta_archivo)
    import pandas as pd
    df = pd.read_csv(ruta_archivo)
    return {
        "filas_columnas": df.shape,
        "columnas": df.columns.tolist(),
        "tipos_dato": df.dtypes,
        "estadisticas": df.describe(include='all')
    }