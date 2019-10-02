from flask import Flask, request, jsonify, render_template
from request import parse_data
from  datetime import date, datetime, timedelta
from pymemcache.client import base
import ast
from cache import cached_data

app = Flask("app")




cache_data = cached_data()

@app.route('/currency', methods=['GET'])
def get():
    return jsonify(cached_data())


@app.route('/currency/<code>', methods=['GET'])
def usd(code):
    for item in cached_data():
        if item["code"] == code:
            return jsonify(item)
    return jsonify({"error":"melumat tapilmadi"})

app.run(debug=True, host='0.0.0.0', port=8000)