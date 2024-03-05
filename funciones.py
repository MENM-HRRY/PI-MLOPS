import pickle
import pandas as pd
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import pyarrow.parquet as pq

def welcome():
    '''
    Biemvenida a los usuarios
    
    Returns:
    str: Pagina web de bienvenida.
    '''
    return '''
    <html>
        <head>
            <link rel="shortcut icon" href="https://fastapi.tiangolo.com/img/favicon.png">
            <link rel="preconnect" href="https://fonts.googleapis.com">
            <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
            <link href="https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,200..1000;1,200..1000&display=swap" rel="stylesheet">
            <title>PI MLOPS memn</title>
            <style>
                body {
                    background-color:#000000 ;
                    font-family: "Poppins", sans-serif;
                    padding: 20px;
                }
                h1 {
                    color: #ffffff;
                    text-align: center;
                }
                p {
                    color: #ffffff;
                    text-align: center;
                    font-size: 18px;
                    margin-top: 20px;
                }
                
            </style>
        </head>
        <body>
            <p align='center'>
            <img src ="https://d31uz8lwfmyn8g.cloudfront.net/Assets/logo-henry-white-lg.png" style="display: inline-block;">
            <p>
            <h1>Henrry labs Deploy Render Fast API para la plataforma Steam</h1>
            <p>Machine Learning Operations (MLOps).</p>
            <br>
            <p>Haz click aquí <br> <a href=" http://127.0.0.1:8000/docs"><img alt="FAST API" src="https://store.akamai.steamstatic.com/public/shared/images/header/logo_steam.svg?t=962016" style="display: inline-block; width: 250px;"></a><br></p>
            <br>
            <p> Visita mi repositorio en <a href="https://github.com/MENM-HRRY/PI_MLOPS.git"><img alt="GitHub" src="https://img.shields.io/badge/GitHub-black?style=flat-square&logo=github"></a></p>
            
        </body>
    </html>
    '''

# Cargar los DataFrames desde los archivos parquet
games=pd.read_parquet("games.parquet")

reviews=pd.read_parquet("reviews.parquet")

new_df = pd.read_parquet('modelo.parquet')


#funcion 1
def developer(desarrollador):
    if desarrollador not in games['developer'].unique():
        return {'error': 'El Desarrollador especificado no existe.'}
    #llamo a las columnas que necesito
    df = games[["item_id", "price","developer","año_lanzamiento"]] 
    
    #llamo al desarrollador
    developer = df[df["developer"] == desarrollador]
    
    #obtengo la cantidad por año 
    cantidad_item = developer.groupby("año_lanzamiento")["item_id"].count() 
    
    #juegos gratuitos del desarrollador
    gratis = developer[developer["price"] == 0] 
    
    #cantidad juegos gratis por año 
    total_gratis= gratis.groupby("año_lanzamiento")["price"].count() 

    #porcentaje gratis por año 
    cont_gratis_año = round((total_gratis/cantidad_item)*100,2) 

    #asigno nombre a las series
    cantidad_item.name = "Cantidad de Items"

    cont_gratis_año.name = "Contenido Free"
    #unimos las dos tablas para hacerla unica
    tabla = pd.merge(cantidad_item, cont_gratis_año,on="año_lanzamiento").reset_index() 

    #reemplazo los nan por 0
    tabla = tabla.fillna(0) 
    
    tabla["Contenido Free"] = tabla["Contenido Free"].apply(lambda x: f"{x}%")
    #convierto la tabla en diccionario
    diccionario = tabla.to_dict(orient="records") 
    
    return diccionario


#funcion 2 
#Realizar la unión de los DataFrames
merged_reviews_games = reviews.merge(games[['item_id', 'price']])
merged_reviews_games.drop(columns=['helpful','año',"sentiment_analysis"], inplace=True)

def userdata(user_id):
    if user_id not in merged_reviews_games['user_id'].unique():
        return {'error': 'El usuario especificado no existe.'}
    # Filtrar los datos para el usuario especificado
    user_data = merged_reviews_games[merged_reviews_games['user_id'] == user_id]
    # Calcular la cantidad de dinero gastado por el usuario
    dinero_gastado = user_data['price'].sum()

    # Calcular el porcentaje de recomendación en base a reviews.recommend
    recomendacion = user_data['recommend'].sum()
    porcentaje_recomendacion = recomendacion / len(user_data) * 100

    # Calcular la cantidad de items
    cantidad_de_items = user_data['item_id'].nunique()

    # Crear un diccionario con los resultados
    resultados = {
        'Cantidad de dinero gastado': dinero_gastado,
        'Porcentaje de recomendación': porcentaje_recomendacion,
        'Cantidad de items': cantidad_de_items
    }

    return resultados


#funcion 3

def UserForGenre(genero):
    df = pd.read_csv('items.csv')
    if genero not in df['Género'].values:
        return "El género que buscas no existe, prueba con  alguno de la lista"
    genre_df = df[df['Género'] == genero]
    hours_per_year = genre_df.iloc[:, 2].to_dict()  # get the 3rd column
    user_max_hours = max(hours_per_year, key=hours_per_year.get)
    return {"Usuario con más horas jugadas": hours_per_year[user_max_hours], "Horas jugadas por año": genre_df.iloc[:, 3].to_dict()} 





#funcion 4
# Realizar la unión de los DataFrames
merged_df = pd.merge(reviews, games, on='item_id')
    
def best_developer_year(year: int):
    if year not in merged_df['año'].unique():
        return {'error': 'El año especificado no existe.'}

    # Filtrar los juegos por año y por recomendación positiva
    df_year = merged_df[(merged_df['año'] == year) & (merged_df['recommend'] == True) & (merged_df['sentiment_analysis'] == 2)]

    # Contar el número de juegos recomendados por desarrollador y devolver los tres primeros desarrolladores
    top_desarrolladores = df_year['developer'].value_counts().head(3).index.tolist()

     # Devolver el top 3 de desarrolladores
    return {"Puesto 1" : top_desarrolladores[0], "Puesto 2" : top_desarrolladores[1], "Puesto 3" : top_desarrolladores[2]}
    

#funcion 5
merged = reviews.merge(games[['item_id', 'price',"developer"]], on='item_id')
def developer_reviews_analysis(desarrolladora:str):
    if desarrolladora not in games['developer'].unique():
        return {'error': 'El Desarrollador especificado no existe.'}
    
    #filtrar las columnas a utilizar 
    df = merged[['user_id', 'item_id','developer','año','sentiment_analysis']] 
    #filtrar los datos por desarrolladora
    df_merged = df[df["developer"] == desarrolladora] 

    # Se obtienen la cantidad de reviews positivas y negativas
    reviews_positivas = df_merged[df_merged["sentiment_analysis"] == 2].shape[0] 
    reviews_negativas = df_merged[df_merged["sentiment_analysis"] == 0].shape[0]

    # Se crea un string con el resumen de las reviews
    resumen_reviews = f"[Negative = {reviews_negativas}, Positive = {reviews_positivas}]" 
    # Se crea un diccionario con los resultados obtenidos
    dicc = {desarrolladora : resumen_reviews} 

    # Se devuelve un diccionario con los resultados obtenidos
    return dicc
 

#funcion 6
def recomendacion_usuario( id_usuario ):
    df = pd.read_parquet('modelo.parquet')
    if id_usuario not in df['user'].values:
        return {f"El usuario '{id_usuario}' que buscabas no existe."}
    user_data = df[df['user'] == id_usuario].reset_index(drop=True)
    result = {}
    for col in user_data.columns[1:]:
        if pd.notna(user_data[col][0]):
            result[col] = user_data[col][0]
        else:
            result[col] = None
    return result
   
    