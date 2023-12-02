from flask import Flask, redirect, url_for, render_template, request
import random
import string

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def default():
    print("Welcome To this Application")
    content = ""
    if request.method == "POST":
        website = request.form['web']
        max_length = request.form['leng']
        if max_length == 0 or max_length == "0":
            content = "Please Enter the length of the password"
        else:
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
            content = "".join(pass_list)
            
            # Redirect to a new URL after successful form submission
            return redirect(url_for('show_password', password=content))

    return render_template("home.html", content=content)

@app.route('/<name>')
def special(name):
    return f"welcome {name}"

@app.route('/admin')
def admin():
    return redirect(url_for("default"))

@app.route('/show_password/<password>')
def show_password(password):
    return render_template("home.html", content=password)

if __name__ == "__main__":
    #app.run(debug=True, port=5000)
    app.run(debug=True,host='0.0.0.0',port=5000)
