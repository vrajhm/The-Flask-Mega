from lecture1 import app

@app.route("/")
@app.route("/index")
def printHello():
    return "Hello World!"