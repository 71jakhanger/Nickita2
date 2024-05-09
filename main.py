from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    with open("static/index.html", "r", encoding="utf-8") as f:
        return f.read()

@app.route("/process", methods=["POST"])
def process():
    form = request.form
    f = open("static/savedFoal.txt", "a")
    f.write(f"({form['NameGet']}):  ({form['PhoneNumber']}):  ({form['Class']}):  ({form['Subjects']});\n")
    f.close()
    return redirect("/")

app.run(host='0.0.0.0', port=81)
