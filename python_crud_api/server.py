from flask import Flask, request, jsonify, make_response, current_app
import json

from datastore import create_mail, read_all, update_mail, delete_mail

app = Flask(__name__)


@app.route('/mail', methods=['GET', 'POST', 'PUT', 'DELETE'])
def mail_api():
    if request.method == "GET":
        mails = read_all()
        mail_json = [mail.__dict__ for mail in mails]
        current_app.logger.info(mail_json)

        # mocked_mail_json = json.load(current_app.open_resource('mock_store.json'))
        return jsonify(mail_json), 200

    if request.content_type != "application/json":
        return make_response(400)

    elif request.method == "POST":
        req_data = request.get_json()
        subject = req_data['subject']

        create_mail(subject)

        return make_response('', 200)

    elif request.method == "PUT":
        req_data = request.get_json()

        str_mail_id = req_data['id']
        mail_subject = req_data['subject']

        if str_mail_id is "":
            return make_response(400)

        try:
            mail_id = int(str_mail_id)

        except ValueError:
            return make_response(400)

        update_mail(mail_id, mail_subject)

        return make_response('', 200)

    elif request.method == "DELETE":
        return 'Hello, World!'

    return 'Hello, World!'


if __name__ == '__main__':
    app.run(debug=True)
