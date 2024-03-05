<p align=center><img src=https://d31uz8lwfmyn8g.cloudfront.net/Assets/logo-henry-white-lg.png><p>

# <h1 align=center> **PROYECTO INDIVIDUAL Nº1** </h1>

# <h1 align=center>**`Machine Learning Operations (MLOps)`**</h1>

<p align="center">


¡Bienvenidos al primer proyecto individual de la etapa de labs! En esta ocasión, deberán hacer un trabajo situándose en el rol de un ***MLOps Engineer***.  

<hr>  

## **Introducciòn**
En el siguiente proyecto de Machine Learning se tiene como objetivo poner en pratica los conocimientos adquiridos en el Boot Camp de ciencia de datos y en lo particular en el modulo seis; acontinuacion comparto cuadenos de trabajo sobre el analisis y tratmiento de los datos y las tecnicas de ML aplicadas para resolver el reto.

## Descripciòn

Para entender la estructura de los datos y poder preparar los insumos para la siguiente etapa de desarrollo, mediante el cauderno [ETL](1ETL_.ipynb) abordo el tema de la limpieza de los dataset's eliminando valores nulos y convirtiendo en ceros los NA, ademas de la transformacion de archivos Json a formato parquet para optimizar las consultas.
En el cauderno de trabajo [EDA](2EDA.ipynb) realice el analisis necesario para encontrar las relaciones entre las variables con la finalidad de entender los patrones o las tendecias, por lo que observando la columna de los generos o tipos de juegos decidi utilizar la funciòn para explotar los registros del formato Json a columnas binarias ya que este cambio en la estructura del dataset  me permitìo la construcion de la funcion para la busqueda por genero, ademas de interactuar con los modelos de aprendizaje que me seran de utilidad de la construciòn de las funciones.

··El RETO:

+ def **developer( *`desarrollador` : str* )**:
    `Cantidad` de items y `porcentaje` de contenido Free por año según empresa desarrolladora. 
Ejemplo de retorno:

| Año  | Cantidad de Items | Contenido Free  |
|------|-------------------|------------------|
| 2023 | 50                | 27%              |
| 2022 | 45                | 25%              |
| xxxx | xx                | xx%              |


+ def **userdata( *`User_id` : str* )**:
    Debe devolver `cantidad` de dinero gastado por el usuario, el `porcentaje` de recomendación en base a reviews.recommend y `cantidad de items`.

Ejemplo de retorno: {"Usuario X" : us213ndjss09sdf, "Dinero gastado": 200 USD, "% de recomendación": 20%, "cantidad de items": 5}

+ def **UserForGenre( *`genero` : str* )**:
    Debe devolver el usuario que acumula más horas jugadas para el género dado y una lista de la acumulación de horas jugadas por año de lanzamiento.

Ejemplo de retorno: {"Usuario con más horas jugadas para Género X" : us213ndjss09sdf,
			     "Horas jugadas":[{Año: 2013, Horas: 203}, {Año: 2012, Horas: 100}, {Año: 2011, Horas: 23}]}
	
+ def **best_developer_year( *`año` : int* )**:
   Devuelve el top 3 de desarrolladores con juegos MÁS recomendados por usuarios para el año dado. (reviews.recommend = True y comentarios positivos)
  
Ejemplo de retorno: [{"Puesto 1" : X}, {"Puesto 2" : Y},{"Puesto 3" : Z}]

+ def **developer_reviews_analysis( *`desarrolladora` : str* )**:
    Según el desarrollador, se devuelve un diccionario con el nombre del desarrollador como llave y una lista con la cantidad total 
    de registros de reseñas de usuarios que se encuentren categorizados con un análisis de sentimiento como valor positivo o negativo. 

Ejemplo de retorno: {'Valve' : [Negative = 182, Positive = 278]}

<br/>

En el script de python llamado  [funciones](funciones.py) se encuentra desarrolladas paso a paso cada unas de las consignas anteriores con la finalidad de que mediante la herramienta Fast Api  se puedan invocar las funciones para su despliegue en la web.


# PI_MLOPS_STEAM-MEMN
