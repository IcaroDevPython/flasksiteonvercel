from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.errorhandler(Exception)
def error(error):
    return render_template('errorpage.html', context={'error': error})

if __name__ == '__main__':
    app.run()