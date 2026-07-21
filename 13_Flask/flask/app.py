from flask import Flask

'''
It will create an instance of Flask class,
which will be the WSGI (Web Server Gateway Interface) for application.
'''
## WSGI Application
app = Flask(__name__) # adding the entry point

@app.route("/")
def welcome():
    return "Welcome to Flask...This is really amazing!!"

@app.route("/index")
def index():
    return "Welcome to the index page..."


if __name__ == '__main__':
    app.run(debug=True)