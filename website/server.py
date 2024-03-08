from flask import Flask, render_template, request
from tinydb import TinyDB

app = Flask(__name__)
db = TinyDB("caminhos.json")



@app.route("/")
def index():
    return render_template("index.html")

# rota para cadastrar um novo ponto para o robo
@app.route("/novo", methods=[ "POST"])
def sobre(name=None):
    if request.method == "POST":
        name = request.form["name"]
        x_loc = request.form["x_loc"]
        y_loc = request.form["y_loc"]
        z_loc = request.form["z_loc"]
        r_loc = request.form["r_loc"]
        db.insert({"name": name, "x_loc": x_loc, "y_loc": y_loc, "z_loc": z_loc, "r_loc": r_loc})
    # posts = db.all()
    return render_template("index.html", name=name)

# rota para pegar um id de caminho e retornar os pontos
@app.route("/pegar_caminho/<int:id_input>", methods=["GET"])
def pegar_caminho(id_input):
    id = int(id_input)
    return db.get(doc_id=id)

# rota que retorna todos os ids e nomes de caminhos cadastrados 
@app.route("/listas_caminhos", methods=["GET"])
def listas_caminhos():
    return db.search({})


# rota que atualiza um caminho com base no id 
@app.route("/atualizar_caminho", methods=["PUT"])   
def atualizar_caminhos(id, name, x_loc, y_loc, z_loc, r_loc):
    id = id
    name = name
    x_loc = x_loc
    y_loc = y_loc
    z_loc = z_loc
    r_loc = r_loc
    db.update({"name": name, "x_loc": x_loc, "y_loc": y_loc, "z_loc": z_loc, "r_loc": r_loc}, doc_ids=id)
    return "Caminho atualizado com sucesso"



# rota que deleta um caminho com base no id
@app.route("/deletar_caminho", methods=["DELETE"])
def deletar_caminho():
    id = request.form["id_delete"]
    db.remove(doc_ids=[id])
    return "Caminho deletado com sucesso"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)