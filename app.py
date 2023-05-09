from flask import Flask


from routes.cards import cards
from extentions.config import db

app = Flask(__name__)

app.register_blueprint(cards, url_prefix='/cards')



@app.route('/')
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)