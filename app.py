from flask import Flask, jsonify, render_template, request
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from controllers.email.master_email import getEmail
from controllers.email.send_email import getSendEmail
from controllers.event.master_event import getEvent

import scheduler

app = Flask(__name__)

@app.route('/')
def index():
    return 'okai'


### adl_user.adl_user ###
@app.route('/list-email')
def list_email():
    return render_template('list_email.html', data=getEmail())
    # return make_response(get(), 200)

@app.route('/list-event')
def list_event():
    return render_template('list_event.html', data=getEvent())

@app.route('/list-send-email')
def list_sending_email():
    return render_template('list_send_email.html', data=getSendEmail())

@app.errorhandler(404)
def not_found(error = None):
	message = {
		'status': 404,
		'message': 'Not Found: ' + request.url,
	}
	resp = jsonify(message)
	resp.status_code = 404

	return resp

if __name__ == "__main__":
	app.run(debug = True)