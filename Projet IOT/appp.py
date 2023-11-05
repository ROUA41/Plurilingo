from flask import Flask, render_template, redirect, url_for
app= Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")
@app.route('/index1')
def index1():
    return render_template("index1.html")
@app.route('/bouton-clique')
def bouton_clique():
    return redirect(url_for('index1'))
@app.route('/index2')
def index2():
    return render_template('index2.html')
@app.route('/bouton-clique1')
def bouton_clique1():
    return redirect(url_for('index2'))
@app.route('/index3')
def index3():
    return render_template('index3.html')
@app.route('/bouton-clique2')
def bouton_clique2():
    return redirect(url_for('index3'))
@app.route('/index4')
def index4():
    return render_template('index4.html')
@app.route('/bouton-clique3')
def bouton_clique3():
    return redirect(url_for('index4'))

if __name__=="__main__":
    app.run(host="0.0.0.0")
