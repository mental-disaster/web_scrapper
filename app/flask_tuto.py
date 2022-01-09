from flask import Flask, render_template, request, redirect, send_file
from scrapper import get_datas
from exporter import save_to_file

app = Flask("SuperScrapper")

@app.route("/")
def home():
    return render_template("potato.html")

@app.route("/report")
def report():
    word = request.args.get('word')
    if(word):
        word = word.lower()
        global datas
        datas = get_datas(word)
        if(not datas):
            return render_template("noData.html", searchingBy=word)
        return render_template("report.html", searchingBy=word, resultsNumber=len(datas), datas=datas)
    else:
        return redirect("/")

@app.route("/export")
def export():
    try:
        word = request.args.get('word')
        if(not word):
            raise Exception()
        word = word.lower()
        if(not datas):
            raise Exception()
        save_to_file(datas)
        return send_file("datas_by_flask.csv")
    except:
        return redirect("/")

app.run(host='0.0.0.0', port=80)