from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')   
def hello_world():
    return 'Hello World!' 

@app.route('/dojo')   
def hello_world2():
    return 'Dojo!' 

@app.route('/say/<name>')   
def hello_world3(name):
    return f"Hi {name}" 

@app.route('/say/<name>')   
def hello_world4(name):
    return f"Hi {name}" 

@app.route('/repeat/<amount>/<message>')   
def hello_worl5(amount,message):
    string = ""
    for i in range(0, int(amount)):
        string += message
    return string






if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

