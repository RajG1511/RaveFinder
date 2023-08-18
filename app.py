from flask import Flask, render_template, request
import backend

app = Flask(__name__, static_folder='static')

# Import your rave scraping script and any other necessary modules

raves = []

@app.route("/", methods=["GET", "POST"])
def index():
    global raves
    if request.method == "POST":
        city = request.form.get("city")
        # Call your rave scraping function here using the provided city
        # raves = your_function_to_get_raves(city)
        backend.loadRaves(city)
        raves = backend.raveList
        # For demo purposes, I'm using placeholder raves
        #raves = ["Rave 1", "Rave 2", "Rave 3"]
        # print(raves)
        return render_template("index.html", raves=raves)
    sort_by = request.args.get("sort_by")
    return render_template("index.html")

@app.route("/add_to_calendar", methods=["POST"])
def add_to_calendar():
    rave_id = request.form.get("rave_id")
    backend.createEvent(int(rave_id))
    

    return "Added to Calendar: "

@app.route("/add_all_to_calendar", methods=["POST"])
def add_all_to_calendar():
    print("in this hoe")
    backend.addAllRaves()
    return "Added all raves to calendar"

if __name__ == "__main__":
    app.run(debug=True)