from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/<name>', methods=["GET"]) # Revisit decorators if you unclear of this syntax
def name(name):
    name = name.upper()
    signed_in = False
    return render_template('index.html', name=name, signed_in=signed_in)

@app.route('/')
def index():
    first_name = request.args.get('first_name')
    return render_template('index.html', first_name=first_name)

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route('/user/<string:username>') # adding string will ensure the username is a string otherwise no match
def user_page(username):
    return f'Hi {username[0:3]}'

if __name__ == '__main__': # Revisit previous challenge if you're uncertain what this does https://code.nextacademy.com/lessons/name-main/424
    app.run()
    # app.run(debug=True)