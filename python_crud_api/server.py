from flask import Flask, request, jsonify, make_response

app = Flask(__name__)


@app.route('/mail', methods=['GET', 'POST', 'PUT', 'DELETE'])
def update():
    if request.content_type!="application/json":
        return jsonify(error_msg="bad content type"),400

    if request.method == "GET":
        return 'Hello, World!'

    elif request.method == "POST":
        return 'Hello, World!'

    elif request.method == "PUT":
        req_data = request.get_json()

        str_mail_id = req_data['id']
        mail_subject = req_data['subject']

        if str_mail_id is "":
            return make_response(400)

        mail_id = 0
        try:
            mail_id = int(str_mail_id)

        except ValueError:
            return make_response(400)



        return 'Hello, World!'

    elif request.method == "DELETE":
        return 'Hello, World!'

    return 'Hello, World!'


if __name__ == '__main__':
    app.run(debug=True)
