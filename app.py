from flask import Flask, jsonify

app = Flask(__name__)

# Define a demo API endpoint
@app.route('/api/demo', methods=['GET'])
def demo_api():
    data = {
        'message': 'Hello, this is a demo API!',
        'status': 'success'
    }
    return jsonify(data)

# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
