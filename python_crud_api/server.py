from flask import Flask, request, jsonify, make_response, current_app
from flask_cors import cross_origin,CORS
from datastore import create_mail, read_all, update_mail, delete_mail

app = Flask(__name__)


@app.route('/mail', methods=['GET', 'POST', 'PUT'])
@cross_origin()
def mail_api():
    if request.method == "GET":
        mails = read_all()
        mail_json = [mail.__dict__ for mail in mails]
        current_app.logger.info(mail_json)

        return jsonify(mail_json), 200

<<<<<<< HEAD
    # if request.content_type != "application/json":
    #     return make_response('',400)
=======
    if request.content_type != "application/json":
        return make_response('', 400)
>>>>>>> 7c08f8986bef075acadeaaa538b5803de7bc8b40

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
            return make_response('',400)

        try:
            mail_id = int(str_mail_id)

        except ValueError:
            return make_response('',400)

        update_mail(mail_id, mail_subject)

        return make_response('', 200)



    return 'Hello, World!'

@app.route('/deleteMail', methods=['POST'])
@cross_origin()
def delete_api():
    if request.method == "POST":
        current_app.logger.info(request)
        req_data = request.get_json()
        current_app.logger.info(req_data)
        str_mail_id = req_data['id']

        if str_mail_id is "":
            return make_response('',400)

        try:
            mail_id = int(str_mail_id)

        except ValueError:
            return make_response('',400)

        delete_mail(mail_id)

        return make_response('',200)


if __name__ == '__main__':
    app.run(debug=True)
