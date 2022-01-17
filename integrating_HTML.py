## Bulding URL dynamically
## Variable rules and URL building

from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route('/')
def welcome():
    #return 'Welcome guys!'
    return render_template('index1.html')

@app.route('/success/<int:score>')
def success(score):
    res = ''
    if score >=50:
        res = 'Pass'
    else:
        res = 'Fail'

    # return f'The person has passed with {str(score)} marks'
    return render_template('result.html', result = res)

@app.route('/fail/<int:score>')
def fail(score):
    #return f'The person has failed with {str(score)} marks'
    return '<html><body><h1> The Result is Fail</body></html>'

## REsult checker
@app.route('/results/<int:marks>')
def results(marks):
    result = ''
    if marks < 50:
        result = 'fail'
    else:
        result = 'success'
        
    #return result
    return redirect(url_for(result, score = marks)) 

## Result checker for submit HTML page
# import request library to read the posted values
@app.route('/submit', methods=['POST', 'GET'])
def submit():
    total_score = 0
    if request.method == 'POST':
        science = float(request.form['Science'])
        maths = float(request.form['Maths'])
        c = float(request.form['C Prog'])
        datascience = float(request.form['DataScience'])
        total_score = (science+maths+c+datascience)/4
    
    return redirect(url_for('success', score = total_score)) 



if __name__ == '__main__':
    app.run(debug=True)
    #app.run()