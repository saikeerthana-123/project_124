# Hello World Application

from flask import Flask, jsonify, request
app = Flask(__name__) # constructor of class flask will take name of current module i.e. flask

# creating an array of tasks with each task as a different object in it
tasks = [
    {
        'id':1,
        'title':u'Buy Groceries',
        'description':u'Milk, Cheese, Pizza, Fruits',
        'done':False
    },
    {
        'id':2,
        'title':u'Learn Python',
        'description':u'Need to find a good python tutorial on the web',
        'done':False
    }
]

@app.route("/add-data", methods=["POST"]) # define route; flask class-decarator

def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"Please provide the data"
        },400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'Name': request.json['Name'],
        'Contact': request.json.get('Contact', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({
        "status":"success",
        "message":"Task added successfully"
    })

@app.route("/get-data") # define route; flask class-decarator

def get_task():
    return jsonify({
        'data':tasks,
    })

# Running web app
if __name__ == "__main__":
    app.run(debug=True)