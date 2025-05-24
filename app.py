from flask import Flask, request, render_template
import requests

app = Flask(__name__)
API_KEY = "4b5df509b6764a8a88333130252405"

@app.route("/", methods=["GET", "POST"])
def index():
    datos = {}
    if request.method == "POST":
        ciudad = request.form.get("ciudad")
        url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={ciudad}&lang=es"
        respuesta = requests.get(url)
        if respuesta.status_code == 200:
            clima = respuesta.json()
            datos = {
                "ciudad": clima["location"]["name"],
                "temperatura": clima["current"]["temp_c"],
                "estado": clima["current"]["condition"]["text"],
                "icono": "https:" + clima["current"]["condition"]["icon"]
            }
        else:
            datos = {"error": "No se encontró la ciudad"}
    return render_template("index.html", datos=datos)

if __name__ == "__main__":
    app.run(debug=True)
