from flask import Flask,redirect,url_for,render_template,request
import random 
import string
app = Flask(__name__)

@app.route('/',methods=["GET","POST"])
def default():
    print("Welcome To this Application")
    return render_template("home.html")

@app.route('/<name>')
def special(name):
    return f"welcome {name}"

@app.route('/onsubmit',methods=["GET","POST"])
def logout():
    
    website = request.form['web']
    max_length = request.form['leng']
    atoz = string.ascii_lowercase
    atozcap = string.ascii_uppercase
    numbers = string.digits
    nonalphanumeric = string.punctuation
    char = ""
    for d in range(int(max_length)):
        char += random.choice(atoz)
        char += random.choice(atozcap)
        char += random.choice(numbers)
        char += random.choice(nonalphanumeric)
    pass_list = list(char)
    random.shuffle(pass_list)
    new_pass = "".join(pass_list)
    return render_template("home.html",content=new_pass)


@app.route('/admin')
def admin():
    return redirect(url_for("logout"))


if __name__ == "__main__":
    #makes changes live[no need of restarting]
    app.run(debug=False,host='0.0.0.0')