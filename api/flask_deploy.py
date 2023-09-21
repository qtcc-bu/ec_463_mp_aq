import server
from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

Server = server.ServerState()

@app.route('/')
def home():
    #return "<p>" + 'should add buttons to take the user places... probably' + "</p>"
    print(Server.temp())
    html_to_return = "<h1 id=\"sample-markdown\">Sample Markdown</h1>"
    html_to_return +=  "<p>This is some basic, sample markdown.</p>"
    html_to_return += ("<p>" + "New Message!" + "</p>")
    return html_to_return

    #return "<p>Hello, World!</p>"
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    error = None
    email = ''
    password = ''
    name = ''
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        name = request.form['name']
    if Server.sign_up(email,name,password):
        return redirect(url_for('home'))
    return render_template('signup.html', error=error)
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    email = ''
    password = ''
    if request.method == 'POST':
        email = request.form['username']
        password = request.form['password']
        token = Server.login(email,password)
        if not token:
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('chat',token=token))
    return render_template('login.html', error=error)
@app.route('/chat/<token>', methods=['GET', 'POST'])
def chat(token):
    token = float(token)
    html_to_return = ''
    html_to_return += ("<h1 id=\"sample-markdown\">" + str(Server._get_name_from_token(token)) + "'s Home Page" + "</h1>")
    html_to_return += '<form action="" method="post">'
    html_to_return +=    '<input type="text" placeholder="Email" name="email" value="{{request.form.email }}">'
    html_to_return +=       '<input class="btn btn-default" type="submit" value="Send">'
    html_to_return +=  '</form>'
    return html_to_return