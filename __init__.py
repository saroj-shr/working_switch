from flask import *
from switch_file import switch
import time

pi = switch()
pi.first_switch(False)
pi.first_switch(True)

app = Flask(__name__)

@app.route('/')
def hello_world():
	return render_template('index.html')

@app.route('/switch_1/<int:state>', methods = ['POST'])
def switch_1(state):
	if state == 0:
		pi.first_switch(True)
	elif state == 1:
		pi.first_switch(False)
	else:
		return ('Unknow LED state!!', 400)

	return('',200)

@app.route('/switch_2/<int:state>', methods = ['POST'])
def switch_2(state):
	if state == 0:
		pi.second_switch(True)
	elif state == 1:
		pi.second_switch(False)
	else:
		return ('Unknow LED state!!', 400)

	return('',200)	



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True, threaded = True)