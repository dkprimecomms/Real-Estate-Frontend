import os
from flask import Flask, render_template, jsonify, request


app = Flask(__name__)


@app.get("/")
def home():
return render_template("index.html")


@app.post("/api/echo")
def echo():
data = request.get_json(silent=True) or {}
msg = (data.get("message") or "").strip()
return jsonify({"reply": msg or "(empty)"})


if __name__ == "__main__":
# App Runner injects PORT; default to 8080 for local dev
port = int(os.environ.get("PORT", 8080))
app.run(host="0.0.0.0", port=port)
