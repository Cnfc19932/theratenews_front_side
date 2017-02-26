# encoding=utf8  
import sys, requests
from flask import Flask,render_template,url_for,jsonify, abort, redirect, session
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

	def __init__(self, request, lang = 'ru'):
		self.request = self.api_server + request
		self.data = {'lang' : lang}
		logging.debug( u'Установлен адрес '+self.request)

	## Выполняем запрос
	def go(self):
		if (self.request):
			logging.info( u'Запрос на '+self.request )
			t = requests.post(self.request,params = self.data) 
			#print self.data
			if t.status_code == 200:
				logging.info( u'Запрос прошел успешно (Code: 200)')
				logging.debug( u'Ответ '+t.content)
				return json.loads(t.content)
			else:
				logging.warning( u'Запрос вернул '+ t.status_code)
				return json.loads(jsonify({}))
		else:
			logging.warning( u'Не задан адрес' )

		


def setlang(lang,session_lang = ''):
	if lang == 'def':
		return 'ru'
	else:
		if lang == 'en':
			 return 'en'
	return 'ru'

@app.errorhandler(404) 
def page_not_found(error):
	
    return render_template('404.html'), 404

@app.route("/<string:lang>/")
@app.route("/")
def index(lang = 'def'):
	lang = setlang(lang)
	model = API('theratenews/pages/index/').go()
	model.update(API('theratenews/modules/firstLine/',lang).go())
	model.update(API('theratenews/modules/secondLine/',lang).go())
	model.update({'lang': lang})
	return render_template('index.html', data = model)


@app.route("/<string:lang>/i/<int:post_id>/")
@app.route("/i/<int:post_id>/")
def item(post_id,lang = 'def'): 
	lang = setlang(lang)
	model = API('theratenews/pages/index/').go()
	try:
		model.update(API('theratenews/news/'+str(post_id)+'/',lang).go())
	except Exception:
		abort(404)
	model.update(API('theratenews/modules/secondLine/',lang).go())
	model.update({'lang': lang})
	return render_template('item.html', data = model)

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0',port = 80) 

