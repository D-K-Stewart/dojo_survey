from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'import os; print(os.urandom(.007!))'


@app.route('/')
def index():
    return render_template("index.html")

    
@app.route('/process', methods=['POST'])
def result():
    print("Submitted Information")
    print(request.form)
    session['username'] = request.form['name']
    session['userlocation'] = request.form['location']
    session['userlanguage'] = request.form['language']
    session['usercomment'] = request.form['comment']
    return redirect("/result")
    
@app.route('/result')
def show_user():
    return render_template('result.html', name=session['username'], location=session['userlocation'], language=session['userlanguage'], comment=session['usercomment'])





#KEEP THIS AT THE BOTTOM!
if __name__=="__main__":       
    app.run(debug=True)