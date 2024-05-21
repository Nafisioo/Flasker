from flask import Flask, render_template

#create a flask instance
app = Flask(__name__)

#create a route decorator
@app.route('/')

#create a route
#def index():
    #return"<h1>Hello Worls!</h1>"

def index():
    return render_template("index.html")
#localhost: 5000/user/Nafis
@app.route('/user/<name>')

def user(name):
    return"<h1>Hello {}</h1>".format(name)


#creaate custom error pages

#invalid url
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

#internal server error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500