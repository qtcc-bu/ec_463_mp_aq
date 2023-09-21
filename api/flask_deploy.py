import server
from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

Server = server.ServerState()

@app.route('/')
def home():
    #return "<p>" + 'should add buttons to take the user places... probably' + "</p>"
    #print(Server.temp())
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
            return redirect(url_for('search',token=token))
    return render_template('login.html', error=error)
@app.route('/search/<token>', methods=['GET', 'POST'])
def search(token):
    token = float(token)
    chat_message = ''
    if request.method == 'POST':
        search_thing = request.form['query']
        return redirect(url_for('chat',token=token,endtoken=search_thing))
   

    return render_template('search.html', error=chat_message)
    return html_to_return
@app.route('/chat/<token>/<endtoken>', methods=['GET', 'POST'])
def chat(token,endtoken):
    token = float(token)
    endtoken = str(endtoken)
    conversation = ''
    is_email = True
    if '@' in endtoken:
        conversation = Server.find_convo_from_email(token,endtoken)
        is_email = True
    else:
        conversation = Server.find_convo_from_name(token,endtoken)
        is_email = False
    send_thing = ''
    if conversation == False:
        Server.send_message_to_convo(token,endtoken,endtoken,is_email,'Start of Chat')
    else:
        for message in conversation:
            send_thing += ("<p>" + message.user + ': '  + message.message + "</p>")
    if request.method == 'POST':
        new_message = request.form['new_chat_text']
        Server.send_message_to_convo(token,endtoken,endtoken,is_email,new_message)
    return render_template('chat.html',conversation=send_thing)
    


