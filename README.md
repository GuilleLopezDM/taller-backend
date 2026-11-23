# 🛸 Rick and Morty — Explorador de personajes

> Taller de backend · Python + Flask + SQLite

Aplicación web que consume la [Rick and Morty API](https://rickandmortyapi.com/) para listar y buscar personajes y guardar tus favoritos en una base de datos local.

## ✨ Funcionalidades

- Listado paginado de personajes desde la API pública.
- Búsqueda por nombre, con mensaje si no hay resultados.
- Guardar personajes en favoritos (sin duplicados).
- Ver y eliminar favoritos guardados en SQLite.

## 🛠️ Stack

`Python` · `Flask` · `Flask-SQLAlchemy` · `SQLite` · `requests` · `Jinja2`

## 📡 Rutas

| Método | Ruta | Descripción |
|---|---|---|
| `GET` | `/?page=N&name=...` | Listado paginado o búsqueda por nombre |
| `POST` | `/save` | Guarda un personaje en favoritos |
| `GET` | `/favorites` | Lista los favoritos |
| `POST` | `/delete/<id>` | Elimina un favorito |

## 🚀 Ejecutar

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
flask run
```

Abrí `http://127.0.0.1:5000`. La base de datos se crea automáticamente en `instance/app.db`.

## 📁 Estructura

```text
app.py              # Rutas y consumo de la API
models.py           # Modelo Favorite (SQLAlchemy)
templates/          # index.html y favorites.html
```
