from flask import Flask, request, jsonify
import uuid
from receipt_processor.calc_pts import calculate_points

app = Flask(__name__)
receipts_storage = {}

# Path: /receipts/process
# Method: POST
# Payload: Receipt JSON
# Response: JSON containing an id for the receipt
@app.route('/receipts/process', methods=['POST'])
def process_receipt():
  data = request.get_json()
  receipt_id = str(uuid.uuid4())
  points = calculate_points(data)
  receipts_storage[receipt_id] = points
  return jsonify({"id": receipt_id})


# Path: /receipts/{id}/points
# Method: GET
# Response: A JSON object containing the number of points awarded
@app.route('/receipts/<receipt_id>/points', methods=['GET'])
def get_points(receipt_id):
  points = receipts_storage.get(receipt_id)
  if points is None:
    return jsonify({"error": "receipt not found"}), 404
  return jsonify({"points": points})
