from flask import Flask, request, jsonify, make_response

app = Flask(__name__)


@app.route('/mail', methods=['GET', 'POST', 'PUT', 'DELETE'])
def mail_api():
    if request.content_type!="application/json":
        return make_response(400)

    if request.method == "GET":
        #no lazy loading
        #call datastore.py
        return 'Hello, World!'

    elif request.method == "POST":

        return 'Hello, World!'

    elif request.method == "PUT":
        return 'Hello, World!'

    elif request.method == "DELETE":
        return 'Hello, World!'

    return 'Hello, World!'


if __name__ == '__main__':
    app.run(debug=True)
