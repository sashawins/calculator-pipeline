from flask import Flask, request, jsonify

app = Flask(__name__)


def is_valid_number(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


@app.route("/plus", methods=["POST"])
def plus():
    data = request.get_json()
    a = data.get("a")
    b = data.get("b")

    if not (is_valid_number(a) and is_valid_number(b)):
        return (
            jsonify(
                {"error": "Invalid input. Both 'a' and 'b' must be valid numbers."}
            ),
            400,
        )

    result = a + b
    return jsonify({"result": result})


@app.route("/minus", methods=["POST"])
def minus():
    data = request.get_json()
    a = data.get("a")
    b = data.get("b")

    if not (is_valid_number(a) and is_valid_number(b)):
        return (
            jsonify(
                {"error": "Invalid input. Both 'a' and 'b' must be valid numbers."}
            ),
            400,
        )

    result = a - b
    return jsonify({"result": result})


@app.route("/multiply", methods=["POST"])
def multiply():
    data = request.get_json()
    a = data.get("a")
    b = data.get("b")

    if not (is_valid_number(a) and is_valid_number(b)):
        return (
            jsonify(
                {"error": "Invalid input. Both 'a' and 'b' must be valid numbers."}
            ),
            400,
        )

    result = a * b
    return jsonify({"result": result})


@app.route("/divide", methods=["POST"])
def divide():
    data = request.get_json()
    a = data.get("a")
    b = data.get("b")

    if not (is_valid_number(a) and is_valid_number(b)):
        return (
            jsonify(
                {"error": "Invalid input. Both 'a' and 'b' must be valid numbers."}
            ),
            400,
        )

    if b == 0:
        return jsonify({"error": "Division by zero is not allowed."}), 400

    result = a / b
    return jsonify({"result": result})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
