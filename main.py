from flask import Flask, request, redirect, render_template

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    form = request.form
    f = open("static/savedFoal.txt", "a")
    f.write(f"({form['NameGet']}):  ({form['PhoneNumber']}):  ({form['Class']}):  ({form['Subjects']});\n")
    f.close()
    return redirect("/")

app.run(host='0.0.0.0', port=81)
