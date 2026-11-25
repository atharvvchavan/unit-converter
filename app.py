import math
import os

from flask import Flask, jsonify, render_template, request

import converter

app = Flask(__name__)
VERSION = os.environ.get("APP_VERSION", "dev")


@app.route("/")
def index():
    return render_template("index.html", units=converter.UNITS)


@app.route("/api/convert")
def api_convert():
    category = request.args.get("category", "")
    from_unit = request.args.get("from", "")
    to_unit = request.args.get("to", "")

    try:
        value = float(request.args.get("value", ""))
    except ValueError:
        return jsonify(error="value must be a number"), 400

    if not math.isfinite(value):
        return jsonify(error="value must be a normal number"), 400

    try:
        result = converter.convert(category, value, from_unit, to_unit)
    except ValueError as err:
        return jsonify(error=str(err)), 400

    return jsonify(
        category=category,
        value=value,
        from_unit=from_unit,
        to_unit=to_unit,
        result=result,
    )


@app.route("/health")
def health():
    return jsonify(status="ok")


@app.route("/version")
def version():
    return jsonify(version=VERSION)
