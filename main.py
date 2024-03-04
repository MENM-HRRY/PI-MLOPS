from typing import Union
from funciones import developer
from funciones import userdata
from funciones import welcome
from funciones import UserForGenre
from fastapi import FastAPI, Form
import uvicorn
from fastapi.responses import RedirectResponse 
from fastapi.responses import HTMLResponse
from funciones import best_developer_year  
import funciones
from funciones import  developer_reviews_analysis
from funciones import recomendacion_usuario
from fastapi.responses import JSONResponse
from typing import List, Dict, Tuple, Sequence, Any, Union, Optional, Callable
from fastapi import Response

app = FastAPI(title="PI MLOPS memn")

@app.get(path='/developer',
          description=""" 
    <html>
        <body style="background-color: #000000;">
            <h1 style="color: 3f888f;">INSTRUCCIONES</h1>
            <h3 style="color: 3f888f; font-family: 'Raleway';">
                1. Haga clic en "Try it out".<br>
                2. Ingrese el desarrollador en el cuadro de abajo.<br>
                3. La consulta devuelve la cantidad de items y porcentaje de contenido Free por año según empresa desarrolladora.<br>
                4. Ejemplo de desarrolladores: ||Kotoshiro||Trickjump Games Ltd|| Stainless Games Ltd|| ETGgames||  id Software ||Square Enix||MumboJumbo||Ubisoft.<br>
                5.Copie y pegue de las sugerencias y presione Execute nuevamente.
            </h3>         
        </body>
    </html>
    """,
         tags=["EndPoints Developer"])

def developer(desarrollador):
    developer = funciones.developer(desarrollador)
    return developer

    
@app.get(path = '/userdata',
          description=""" 
    <html>
        <body style="background-color: #000000;">
            <h1 style="color: 3f888f;">INSTRUCCIONES</h1>
            <h3 style="color: 3f888f; font-family: 'Poppins';">
                1. Haga clic en "Try it out".<br>
                2. Ingrese el usuario en el cuadro de abajo.<br>
                3. Observe el dinero gastado por el usuario, el porcentaje de recomendación y la cantidad de items que tiene el mismo.<br>
                4. Ejemplo usuarios: ||maplemage||starkillershadow553||sandwiches1||Nozomikat||mimimomoma||1337lolroflmao||AddzyTheBaddzy||NaruseAiria.<br>
                5. Para cambiar de usuario, copie y pegue de las sugerencias y presione Execute nuevamente.
            </h3>         
        </body>
    </html>
    """,
         tags=["EndPoints UserData"])
def userdata(user_id):
    result = funciones.userdata(user_id)
    return result





@app.get(path='/UserForGenre',
          description=""" 
    <html>
        <body style="background-color: #000000;">
            <h1 style="color: 3f888f;">INSTRUCCIONES</h1>
            <h3 style="color: 3f888f; font-family: 'Poppins';">
                1. Haga clic en "Try it out".<br>
                2. Ingrese el usuario en el cuadro de abajo.<br>
                3. El usuario que acumula más horas jugadas para el género dado y una lista de la acumulación de horas jugadas por año de lanzamiento.<br>
                4. Ejemplos de generos: ||Strategy||Indie||Simulation||RPG||Simulation||Sports||Multiplayer||Survival.<br>
                5. Para cambiar de usuario, copie y pegue de las sugerencias y presione Execute nuevamente.
            </h3>         
        </body>
    </html>
    """,
         tags=["Endpoints User For Genre"])
def UserForGenre(genero):
    resultado = funciones.UserForGenre(genero)
    return resultado


@app.get(path='/best_developer_year/{year}',
          description=""" 
    <html>
        <body style="background-color: #000000;">
            <h1 style="color: 3f888f;">INSTRUCCIONES</h1>
            <h3 style="color: 3f888f; font-family: 'Poppins';">
                1. Haga clic en "Try it out".<br>
                2. Ingrese el desarrollador en el cuadro de abajo.<br>
                3. Devuelve loa tres desarrolladores más recomendados por usuarios para el año selecionado<br>
                4. Ingrese un año para obtener el resultado ||2010||2011||2012||2013||2014||2015||<br>
                5. Para cambiar de usuario, copie y pegue de las sugerencias y presione Execute nuevamente.
            </h3>         
        </body>
    </html>
    """,
         tags=["Endpoints Best Developer Year"])
def Best_developer_year(year: str):
    year_int = int(year) 
    review = best_developer_year(year_int)
    return review
     




@app.get(path='/developer_reviews_analysis/{desarrolladora}',
          description=""" 
    <html>
        <body style="background-color: #000000;">
            <h1 style="color: 3f888f;">INSTRUCCIONES</h1>
            <h3 style="color: 3f888f; font-family: 'Poppins';">
                1. Haga clic en "Try it out".<br>
                2. Ingrese el desarrollador en el cuadro de abajo.<br>
                3. Utiliza el nombre de la desarrolladora, para consultar el número de votaciones positivas y negativos.<br>
                4. Ejeplos: ||Square Enix||Trickjump Games Ltd||Capcom||Valve||Epic Games||Rockstar Games||<br>
                5. Para cambiar de desrrolladora, copie y pegue de las sugerencias y presione Execute nuevamente.
            </h3>         
        </body>
    </html>
    """,
         tags=["Endpoints Developer Reviews Analysis"])
def developer_reviews_analysis(desarrolladora:str):
    resulta2 = funciones.developer_reviews_analysis(desarrolladora)
    return resulta2





@app.get(path='/recomendacion_usuario/{user_id}',
          description=""" 
    <html>
        <body style="background-color: #000000;">
            <h1 style="color: 3f888f;">INSTRUCCIONES</h1>
            <h3 style="color: 3f888f; font-family: 'Poppins';">
                1. Haga clic en "Try it out".<br>
                2. Ingrese el desarrollador en el cuadro de abajo.<br>
                3. Utiliza el nombre de la desarrolladora, para consultar el número de votaciones positivas y negativos.<br>
                4. Ejemplos: ||evcentric||Rivtex||WitchHunter4542||L4M1NAS||js41637||<br>
                5. Para cambiar de desrrolladora, copie y pegue de las sugerencias y presione Execute nuevamente.
            </h3>         
        </body>
    </html>
    """,
         tags=["Endpoints Recomendación por usuario"])
def get_recomendacion(user_id: str):
        resultado= recomendacion_usuario(user_id)
        return resultado


@app.get(path="/", 
         response_class=HTMLResponse,
         tags=["Landingpage"]
         )
def Landingpage():
    return welcome()