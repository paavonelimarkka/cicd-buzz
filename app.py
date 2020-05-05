import os
from flask import Flask
from buzz import generator

app = Flask(__name__)

@app.route("/")
def generate_buzz():
    page = '<html><body style="background: #0F0F0F;"><h1 style="margin: 30px; color: #F6F6F6;">'
    page += generator.generate_buzz()
    page += '</h1></body></html>'
    return page

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))