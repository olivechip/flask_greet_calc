from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    html = """
    <body>
        <h1>Welcome App</h1>
        <ul>
            <li><a href='/welcome'>welcome</li>
            <li><a href='/welcome/home'>welcome home</li>
            <li><a href='/welcome/back'>welcome back</li>
        </ul>
    </body>
    """
    return html
    
@app.route('/welcome')
def welcome():
    return 'welcome'

@app.route('/welcome/home')
def welcome_home():
    return 'welcome home'

@app.route('/welcome/back')
def welcome_back():
    return 'welcome back'