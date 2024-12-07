from flask import Flask, request, render_template, render_template_string

app = Flask(__name__)


@app.route("/")
def index():
    return render_template_string(open("templates/home.html").read())


@app.route("/persegi", methods=["POST"])
def persegi():
    panjang = int(request.form["panjang"])
    lebar = int(request.form["lebar"])
    luas_persegi = panjang * lebar
    keliling_persegi = 2 * (panjang + lebar)
    text = f"""
    Bangun Datar : Persegi <br>
    Luas : {luas_persegi} <br>
    Keliling : {keliling_persegi} <br>
    """

    return render_template("result.html", text=text)


@app.route("/segitiga", methods=["POST"])
def segitiga():
    alas = int(request.form["alas"])
    tinggi = int(request.form["tinggi"])
    luas = round(alas * tinggi / 2)
    text = f"""
    Bangun Datar : Segitiga <br>
    Luas : {luas:.0f} <br>
    """

    return render_template("result.html", text=text)


@app.route("/lingkaran", methods=["POST"])
def lingkaran():
    pi = 22 / 7
    r = int(request.form["r"])
    luas = pi * r * r

    text = f"""
    Bangun Datar : Lingkarang <br>
    Luas : {luas:.0f} <br>
    """

    return render_template("result.html", text=text)


@app.route("/volume-balok", methods=["POST"])
def volume():
    panjang = int(request.form["panjang"])
    lebar = int(request.form["lebar"])
    tinggi = int(request.form["tinggi"])
    volume = panjang * lebar * tinggi
    text = f"""
    Bangun Ruang : Balok <br>
    Volume : {volume:.0f}cm3 <br>
    """

    return render_template("result.html", text=text)


app.run(debug=True)
