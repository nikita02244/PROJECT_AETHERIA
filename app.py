from flask import Flask
from flask_cors import CORS
from routes.auth import auth
from routes.wallet import wallet
from routes.nft import nft

app = Flask(_name_)
app.secret_key = 'your_secret_key'
CORS(app)

# Register blueprints
app.register_blueprint(auth, url_prefix='/auth')
app.register_blueprint(wallet, url_prefix='/wallet')
app.register_blueprint(nft, url_prefix='/nft')

if _name_ == '_main_':
    app.run(debug=True)