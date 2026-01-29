from flask import Flask, request, render_template,redirect
import requests
import os

from models import db
from models import Favorite

#instanciamos la app de flask
app = Flask(__name__)
Base_dir=os.path.abspath(os.path.dirname(__file__)) #ubicacion del archivo actual
DB_PATH=os.path.join(Base_dir,"instance","app.db") #ubicacion de la base de datos

app.config["SQLALCHEMY_DATABASE_URI"]=f"sqlite:///{DB_PATH}"#asignamos la ruta de la base de datos
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False #desactivamos una caracteristica de sql alchemy que no usamos

db.init_app(app) #inicializamos la base de datos con la app de flask
with app.app_context():# creamos el contexto de la app para crear las tablas
    db.create_all() #creamos las tablas en la base de datos
#uRL PARA LA API DE RICK AND MORTY
API_URL="https://rickandmortyapi.com/api/character"
@app.route("/")
def index():
    #Request que envia el usuario desde el html
    page=request.args.get("page",1)
    #obtenemos el nombre de la url y lo guardamos en una variable name
    name=request.args.get("name")
    if name:
        #Request a la API de Rick and Morty con el filtro de nombre
        response=requests.get(API_URL,params={"name":name})
        if response.status_code!=200:
            return render_template("index.html",characters=[],search=True,error_message="No se encontro el personaje.")
        data=response.json()
        return render_template("index.html",characters=data["results"],search=True)
    #Request a la API de Rick and Morty
    response=requests.get(API_URL,params={"page":page})
    data=response.json()
    return render_template("index.html",characters=data["results"],info=data["info"],page=int(page),search=False)
#Ruta para agregar un personaje a favoritos
@app.route("/save",methods=["POST"])
def save():
    api_id=request.form["api_id"]
    name=request.form["name"]
    image=request.form["image"]
    page=request.form.get("page",1)
    #esto nos permite guardar en la base de datos solo si el personaje no existe
    if not Favorite.query.filter_by(api_id=api_id).first():
        fav=Favorite(api_id=api_id,name=name,image=image)
        db.session.add(fav)
        db.session.commit()
    return redirect(f"/?page={page}")
@app.route("/favorites")#Ruta para ver los personajes favoritos
def favorites():#Ruta para ver los personajes favoritos
    favorites = Favorite.query.all()#obtenemos todos los personajes favoritos de la base de datos
    return render_template("favorites.html", favorites=favorites)# renderizamos la plantilla favorites.html y le pasamos los personajes favoritos
#ruta para eliminar un personaje de favoritos
@app.route("/delete/<int:id>", methods=["POST"])
def delete(id):
    fav = Favorite.query.get(id)
    if fav:
        db.session.delete(fav)
        db.session.commit()
    return redirect("/favorites")