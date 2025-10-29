from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def base():
    return render_template("base.html")

@app.route('/calculo')
def calculo():
    return render_template("calculo.html")

@app.route('/resultado')
def resultado():
    return render_template("resultado.html")

if __name__ == "__main__":
    app.run(debug=True)