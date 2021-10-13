import requests
from flask import Flask, render_template,request
from images import image_data
from flask import Blueprint, jsonify
from api.webapi import api_bp


from pathlib import \
    Path  # https://medium.com/@ageitgey/python-3-quick-tip-the-easy-way-to-deal-with-file-paths-on-windows-mac-and-linux-11a072b58d5f


# create a Flask instance
app = Flask(__name__)

app.register_blueprint(api_bp)

# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("index.html")

# connects /kangaroos path to render kangaroos.html
@app.route('/kangaroos/')
def kangaroos():
    return render_template("kangaroos.html")

@app.route('/walruses/')
def walruses():
    return render_template("walruses.html")


@app.route('/hawkers/')
def hawkers():
    return render_template("hawkers.html")


@app.route('/stub/')
def stub():
    return render_template("stub.html")

@app.route('/greet', methods=['GET', 'POST'])
def greet():
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:
            return render_template("greet.html", name=name)
    return render_template("greet.html", name="World")



@app.route("/binary/", methods=['GET', 'POST'])
def binary():
    BITS = 8
    imgBulbOn = "/static/assets/blub_on.gif"
    # second time you call it, its a post action
    if request.method == 'POST':
        BITS = int(request.form['BITS'])
        #imgBulbOn = request.form['lightOn']
    #return render_template("binary.html", imgBulbOn=imgBulbOn, BITS=BITS)
    return render_template("binary.html", BITS=BITS)

@app.route("/Binary_RGB")
def Binary_RGB():
    return render_template("Binary-RGB.html")

@app.route('/rgb/')
def rgb():
    return render_template('rgb.html', images=image_data())

@app.route('/joke', methods=['GET', 'POST'])
def joke():

    # use this url to test on and make modification on you own machine
    #url = "http://127.0.0.1:5000/api/joke"

    url = "https://csp.nighthawkcodingsociety.com/api/joke"
    response = requests.request("GET", url)
    return render_template("joke.html", joke=response.json())


@app.route('/jokes', methods=['GET', 'POST'])
def jokes():

    # use this url to test on and make modification on you own machine
    #url = "http://127.0.0.1:5000/api/jokes"

    url = "https://csp.nighthawkcodingsociety.com/api/jokes"

    response = requests.request("GET", url)
    return render_template("jokes.html", jokes=response.json())

@app.route('/covid19', methods=['GET', 'POST'])
def covid19():
    url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api"
    headers = {
        'x-rapidapi-key': "dec069b877msh0d9d0827664078cp1a18fajsn2afac35ae063",
        'x-rapidapi-host': "corona-virus-world-and-india-data.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)
    print(type(response))
    # uncomment this code to test from terminal
    world = response.json().get('world_total')
    print(type(world))
    countries = response.json().get('countries_stat')
    print(world['total_cases'])
    print(type(countries))
    for country in countries:
        print(country['country_name'])

    return render_template("covid19.html", stats=response.json())

# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
