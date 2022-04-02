from flask import Flask, render_template, session, request, redirect
import random

app = Flask(__name__)
app.secret_key = 'lalalala'

@app.route('/')
def index():
    if 'num' not in session:
        session['num'] = random.randint(1,100)
    print(session['num'])
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    session['guess'] = int(request.form['numgame'])
    print(session['guess'])
    return redirect('/')




if __name__ == ('__main__'):
    app.run(debug=True)