## Bulding URL dynamically
## Variable rules and URL building
from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def welcome():
    return 'Welcome guys!'

@app.route('/success/<int:score>')
def sucess(score):
    return f'The person has passed with {str(score)} marks'

@app.route('/fail/<int:score>')
def fail(score):
    return f'The person has failed with {str(score)} marks'

@app.route('/results/<int:marks>')
def results(marks):
    result = ''
    if marks < 50:
        result = 'fail'
    else:
        result = 'success'
        
    #return result
    return redirect(url_for(result, score = marks)) 


if __name__ == '__main__':
    app.run(debug=True)
    #app.run()