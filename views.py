from app import app
from flask import render_template

# rotas
@app.route("/")
def index():
    return render_template("index.html")


