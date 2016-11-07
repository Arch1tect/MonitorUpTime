from bottle import post, route, request, run
from time import gmtime, strftime


@post('/')
def qtime_down():

	with open("../qtime/src/restart.log", "a") as myfile:
	    myfile.write(strftime("%Y-%m-%d %H:%M:%S", gmtime())+"\n")


	return "succeed!"


run(host='0.0.0.0', port=8081)