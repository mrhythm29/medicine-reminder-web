from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

file = "medicines.json"

# Load data
def load_data():
    try:
        with open(file, "r") as f:
            return json.load(f)
    except:
        return []

# Save data
def save_data(data):
    with open(file, "w") as f:
        json.dump(data, f)

# Initialize data
medicines = load_data()

@app.route("/", methods=["GET", "POST"])
def home():
    global medicines

    if request.method == "POST":
        name = request.form.get("name")
        time = request.form.get("time")

        medicines.append({"name": name, "time": time})
        save_data(medicines)
        return redirect(url_for("home"))

    return render_template("index.html", medicines=medicines)
@app.route("/delete/<int:index>")
def delete(index):
    global medicines

    if 0 <= index < len(medicines):
        medicines.pop(index)
        save_data(medicines)

    return redirect(url_for("home"))

if __name__ == "__main__":
   import os

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))