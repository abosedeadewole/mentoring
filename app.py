from flask import Flask, render_template, request, redirect, url_for, flash, session


app = Flask(__name__)

@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')