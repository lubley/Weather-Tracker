from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    city = request.args.get("city")
    weather = None
    if city:
        # Temporary: mock data for now just for testing.
        weather = {"temp": 25, "desc": "Sunny"}
    return render_template("index.html", weather=weather)

if __name__ == "__main__":
    app.run(debug=True)
