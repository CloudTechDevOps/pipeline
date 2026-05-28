
from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "message": "Website running successfully"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
