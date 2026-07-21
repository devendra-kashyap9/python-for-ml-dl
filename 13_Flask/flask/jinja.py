### Building URL Dynamically
### Variable Rule
### Jinja2 Template Engine

## Jinja2 Template Engine
'''
{{  }} expression to print output in html
{%  %} conditions, for loops
{#  #} this is for comments
'''

from flask import Flask, render_template, request, redirect, url_for

'''
It will create an instance of Flask class,
which will be the WSGI (Web Server Gateway Interface) for application.
'''
## WSGI Application
app = Flask(__name__) # adding the entry point

@app.route("/")
def welcome():
    return "<html><H1>Welcome to Flask...</H1></html>"

@app.route("/index", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

# @app.route("/submit", methods=["GET", "POST"])
# def submit():
#     if request.method == 'POST':
#         name = request.form['name']
#         return f"Hello {name}!"
#     return render_template("form.html")

## Variable Rule
@app.route("/success/<int:score>")
def success(score):
    ## return "The Marks you got is " + str(score)
    res = ""
    if score >= 50: res = "PASS"
    else: res = "FAIL"
    
    return render_template("results.html", results=res)

# for loop
@app.route("/successresult/<int:score>")
def successres(score):
    ## return "The Marks you got is " + str(score)
    res = ""
    if score >= 50: res = "PASS"
    else: res = "FAIL"
    
    exp = {'score': score, 'res': res}
    
    return render_template("newresult.html", results=exp)
        
# if condition
@app.route("/successif/<int:score>")
def successif(score):
    ## return "The Marks you got is " + str(score)
    return render_template("results.html", results=score)

@app.route("/fail/<int:score>")
def fail(score):
    return render_template("results.html", results=score)

# dynamic URL
# Form handling route (merged into a single function)
@app.route("/submit", methods=["GET", "POST"])
def submit():
    if request.method == 'POST':
        # Safely convert form values
        science = float(request.form.get('science', 0))
        maths = float(request.form.get('maths', 0))
        c = float(request.form.get('c', 0))
        data_science = float(request.form.get('datascience', 0))

        total_score = int((science + maths + c + data_science) / 4)

        # Redirect dynamically to successres route
        return redirect(url_for('successres', score=total_score))
    
    return render_template("getresult.html")
    
    

if __name__ == '__main__':
    app.run(debug=True)