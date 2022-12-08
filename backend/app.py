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
    server.addVessel(post_data.get('name'), post_data.get('lat'), post_data.get('long'))
    return jsonify({
        'status': 'success'
    })

@app.put("/vessels/<int:bookId>")
def edit_vessel(bookId):
    post_data = request.get_json()
    server.editVessel(bookId, post_data.get('name'), post_data.get('lat'), post_data.get('long'))
    return jsonify({
        'status': 'success'
    })  

@app.delete("/vessels/<int:bookId>")
def delete_vessel(bookId):
    server.removeVessel(bookId)
    return jsonify({
        'status': 'success'
    })

def getCurrentData():
    return jsonify({
        'status': 'success',
        'vessels': [vessel.toJson() for vessel in server.vessels]
    })