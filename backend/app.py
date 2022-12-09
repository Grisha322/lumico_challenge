from flask import Flask, jsonify, request
from flask_cors import CORS
from markupsafe import escape
from server import Server

app = Flask(__name__)
server = Server()

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

@app.get("/vessels/")
def main():
    server.reload()
    return getCurrentData()
    
@app.post("/vessels/")
def add_vessel():
    post_data = request.get_json()
    server.addVessel(escape(post_data.get('name')), escape(post_data.get('lat')), escape(post_data.get('long')))
    return jsonify({
        'status': 'success'
    })

@app.put("/vessels/<int:bookId>")
def edit_vessel(bookId):
    post_data = request.get_json()
    server.editVessel(escape(bookId), escape(post_data.get('name')), escape(post_data.get('lat')), escape(post_data.get('long')))
    return jsonify({
        'status': 'success'
    })  

@app.delete("/vessels/<int:bookId>")
def delete_vessel(bookId):
    server.removeVessel(escape(bookId))
    return jsonify({
        'status': 'success'
    })

def getCurrentData():
    return jsonify({
        'status': 'success',
        'vessels': [vessel.toJson() for vessel in server.vessels]
    })