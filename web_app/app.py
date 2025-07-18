from flask import Flask, render_template, request
from knowledge_base import rules
from inference_engine import forward_chaining

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        gejala_input = request.form["gejala"].lower()
        gejala_user = [g.strip() for g in gejala_input.split(",")]
        penyakit, saran = forward_chaining(gejala_user, rules)
        result = {"penyakit": penyakit, "saran": saran}
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
