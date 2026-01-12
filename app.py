from flask import Flask, render_template, request, jsonify, session

app = Flask(__name__)

@app.route("/")
def main():
    if request.form:
        return
    else:
        return render_template("main.html")
