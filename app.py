from flask import Flask, jsonify
from gempa_news import gempanews_instance

#status code
HTTP_ERR = 404

#Flask 
app = Flask(__name__)

#create routes for GempaNews
@app.route('/api/gempa', methods=['GET'])
def news_gempa():
    try:
        data = gempanews_instance.getNews()
        return jsonify(data)
    except:
        return {
            'status': HTTP_ERR,
            'result': 'error'
        }

if __name__ == '__main__':
    app.run(debug=True, port=3001)
