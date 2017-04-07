from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)
app.secret_key = 'pizza'
@app.route('/')
def index():
    return render_template("index.html")
@app.route('/users', methods=["POST"])
def create_users():
    session['name'] = request.form['name']
    session['email'] = request.form['email']
    return redirect("/users")

@app.route('/users')
def show_user():
  return render_template('index.html', name=session['name'], email=session['email'])
app.run(debug=True)
