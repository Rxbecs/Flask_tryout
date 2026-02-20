from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():
    return "<p>Les 11 flask NHA opleidingen</p>"
if __name__ == "__main__":
    app.run()