from flask import Flask, render_template, url_for, redirect
from authlib.integrations.flask_client import OAuth
from flask_cors import CORS

app = Flask(__name__)
CORS(app, supports_credentials=True)

oauth = OAuth(app)

app.config['SECRET_KEY'] = "THIS SHOULD BE SECRET"
app.config['GITHUB_CLIENT_ID'] = "ed107ea04bbbc839a353"
app.config['GITHUB_CLIENT_SECRET'] = "bf58f3226dec535d2122e49a4253c6626b32b06c"

github = oauth.register (
  name='github',
    client_id=app.config["GITHUB_CLIENT_ID"],
    client_secret=app.config["GITHUB_CLIENT_SECRET"],
    access_token_url ='https://github.com/login/oauth/access_token',
    access_token_params =None,
    authorize_url ='https://github.com/login/oauth/authorize',
    authorize_params =None,
    api_base_url ='https://api.github.com/',
    client_kwargs ={'scope': 'user:email'},
)


# Github login route
@app.route('/login/github')
def github_login():
    github = oauth.create_client('github')
    redirect_uri = url_for('github_authorize', _external=True)
    return github.authorize_redirect(redirect_uri)


# Github authorize route
@app.route('/login/github/authorize')
def github_authorize():
    github = oauth.create_client('github')
    token = github.authorize_access_token()
    resp = github.get('user').json()
    print(f"\n{resp}\n")
    return "You are successfully signed in using github,ed107ea04bbbc839a353 "

@app.route('/')
def hello_world():
    return f'Hello, stranger'
