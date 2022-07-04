from apps import app
from libs import db, services
services.create_database()

@app.route('/', methods=['GET'])
def index():
  
  response_schemas = {
  	'title' : 'SRS Delman',
  	'message' : 'Welcome to Sistem Rumah Sakit Delman'
  }
  return jsonify(response_schemas)

if __name__ == '__main__':
    app.run(debug=True)

