from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
print("aaaaaaaaaaaaaaaaaaa", os.environ.get('DB_URI'))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_URI')
db = SQLAlchemy(app)
@app.route('/')
def hello_world():
    try: 
        db.session.query("1").from_statement("SELECT 1").all()
        return 'Hello, Docker! Database connection successful.'
    except Exception as e:
        return f'An error occurred: {str(e)}'
if __name__ == '__main__':
    app.run(host='0.0.0.0')