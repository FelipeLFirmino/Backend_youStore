from flask import flask 

app = Flask(__name__)

#rota da api para pegar TODOS os dados

@app.route("/products")
def Allproducts():
    return()


if __name__ == "__main__":
    app.run(debug = True)