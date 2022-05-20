from flask import Flask, render_template, redirect, Blueprint, url_for
from views import my_view
import os


app = Flask(__name__)

picFolder = os.path.join

app.register_blueprint(my_view)

@app.errorhandler(404)
def error_message(e):
    return render_template('404.html', e=e)


@app.errorhandler(500)
def error_message(e):
    return render_template('404.html', e=e)


if __name__=='__main__':
    app.run(debug=True, port=8000)