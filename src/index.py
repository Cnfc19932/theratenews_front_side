# encoding=utf8  
import sys, requests
from flask import Flask,render_template,url_for,jsonify
import logging
import json

reload(sys)  
sys.setdefaultencoding('utf8')

app = Flask(__name__)

global model 
 
model = {}

api_server = ''

## Обработка ответов от api

class API:
	""" Класс для работы с API """
	api_server = "http://127.0.0.1:8080/"

	def __init__(self, request):
		self.request = self.api_server + request
		logging.debug( u'Установлен адрес '+self.request)

	## Выполняем запрос
	def go(self):
		if (self.request):
			logging.info( u'Запрос на '+self.request )
			t = requests.get(self.request) 
			if t.status_code == 200:
				logging.info( u'Запрос прошел успешно (Code: 200)')
				logging.debug( u'Ответ '+t.content)
				return json.loads(t.content)
			else:
				logging.warning( u'Запрос вернул '+ t.status_code)
				return json.loads(jsonify({}))
		else:
			logging.warning( u'Не задан адрес' )

		



##-----------------------------------------------------##
#t = requests.get("http://127.0.0.1:8080/theratenews/pages/index/")
#print t.status_code


 
@app.route("/")
def index():
	model = API('theratenews/pages/index/').go()

	model.update({ 
		'title' : "Title",
	}) 

	model.update(API('theratenews/modules/firstLine/').go())
	model.update(API('theratenews/modules/secondLine/').go())

	return render_template('index.html', data = model)

@app.route("/i/<int:post_id>/")
def item(post_id): 
	model = API('theratenews/pages/index/').go()


	 
	model.update(API('theratenews/news/511/').go())



	model.update({ 
		'title' : "Title",
	}) 

	model.update(API('theratenews/modules/secondLine/').go())

	return render_template('item.html', data = model)

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0',port = 8801) 
