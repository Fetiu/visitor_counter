from flask import Flask, render_template, make_response, request
import random
app =Flask(__name__)

color_list=['RED','MAROON','BLUE','AQUA','GREEN','LIME','PURPLE','FUCHSIA']

@app.route('/visitcounter')
def index():
	if 'cnt' in request.cookies:
		count = int(request.cookies.get('cnt'))
	else: count = 0
	count+=1
	resp= make_response(render_template('index.html', 
					    size=str(random.randrange(5,10)),
					    color=random.choice(color_list), 
					    number=str(count)
					   ))
	resp.set_cookie('cnt',str(count))
	return resp

if __name__=='__main__':
	app.run(host='0.0.0.0', port=5050, debug=True)

