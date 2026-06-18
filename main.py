from flask import Flask, render_template, session, redirect, url_for

app = Flask(__name__)
app.secret_key = "campeonato"

TIMES = ["Leões", "Tigres", "Águias", "Lobos"]

@app.route("/")
def inicio():

    if "placar" not in session:
        session["placar"] = {
            "Leões": 0,
            "Tigres": 0,
            "Águias": 0,
            "Lobos": 0
        }

    placar = session["placar"]

    lider = max(placar, key=placar.get)

    return render_template(
        "index.html",
        placar=placar,
        lider=lider
    )

@app.route("/ponto/<time>")
def adicionar_ponto(time):

    if time in session["placar"]:
        session["placar"][time] += 1
        session.modified = True

    return redirect(url_for("inicio"))

@app.route("/tirar/<time>")
def tirar_ponto(time):

    if time in session["placar"] and session["placar"][time] > 0:
        session["placar"][time] -= 1
        session.modified = True

    return redirect(url_for("inicio"))

@app.route("/zerar")
def zerar():

    session["placar"] = {
        "Leões": 0,
        "Tigres": 0,
        "Águias": 0,
        "Lobos": 0
    }

    return redirect(url_for("inicio"))

if __name__ == "__main__":
    app.run(debug=True)