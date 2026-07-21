## Put and Delete -- HTTP Verbs
## working witg APIs -- Json

from flask import FLask, jsonify, request

app = FLask(__name__)

# Initial data for todo list
items = [
    {'id':1, "name": "Item 1", "description": "This is item 1"},
    {'id':2, "name": "Item 2", "description": "This is item 2"}
]

@app.route("/")
def home():
    return "Welcome to the sample todo list App..."

## Get: retreive all the items
@app.route("/items", methods=["GET"])
def get_items():
    return jsonify(items)

# GET: retrieve specific item by id
@app.route("/items/<int;item_id>", methods=["GET"])
def get_items(item_id):
    item = next((item for item in items if item[id]==item_id))
    if item is None: 
        return jsonify(("Error: Item not found"))
    return jsonify(item)

# POST: Create a new task
@app.route("/items", methods=["POST"])
def create_item():
    if not request.json or not "name" in request.json:
        return jsonify(("Error: Item not found"))
    
    new_item = {
        "id": items[-1]["id"] + 1 if items else 1,
        "name": request.json["name"],
        "description": request.json["description"]
    }
    
    items.append(new_item)
    return jsonify(new_item)

# PUT: Update the existing item
@app.route('/items/<int:item_id>', methods=["PUT"])
def update_item(item_id):
    item = next((item for item in items if item[id]==item_id), None)
    if item is None:
        return jsonify(("Error: Item not found"))
    item["name"] = request.json.get("name", item["name"])
    item["description"] = request.json.get("description", item["description"])
    
    return jsonify(item)
    
# drive code
if __name__ == '__main__':
    app.run(debug=True)