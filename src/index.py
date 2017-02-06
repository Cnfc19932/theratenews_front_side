# encoding=utf8  
import sys  
from flask import Flask,render_template,url_for

reload(sys)  
sys.setdefaultencoding('utf8')

app = Flask(__name__)

global model 
 
model = {}

model = {
	'name' : 'TheRateNews',
	'logo' : 'TheRateNews',
	'seo' : {
		'ico' : 'i.ico'
	}, 
}
 
@app.route("/")
def index():
	model.update({
		'title' : "Title",
		'first_line' : [
			{ 'title' : 'Порошенко и Трамп по телефону обсудили ситуацию в Авдеевке' , 'id' : '1213' , 'img' : url_for('static', filename='img/1.jpg')},
			{ 'title' : 'МВД Австрии объяснило причину задержания группы выходцев из Чечни' , 'id' : '1231' , 'img' : url_for('static', filename='img/2.jpg')}
		],
		'second_line' : [
			{ 'title' : 'ЕСПЧ присудил Навальному €64 тыс. за незаконные задержания' , 'id' : '1213' , 'img' : 'img/1.jpg'},
			{ 'title' : 'ЕСПЧ присудил Навальному €64 тыс. за незаконные задержания' , 'id' : '1213' , 'img' : 'img/1.jpg'},
			{ 'title' : 'ЕСПЧ присудил Навальному €64 тыс. за незаконные задержания' , 'id' : '1213' , 'img' : 'img/1.jpg'},
			{ 'title' : 'ЕСПЧ присудил Навальному €64 тыс. за незаконные задержания' , 'id' : '1213' , 'img' : 'img/1.jpg'},
			{ 'title' : 'ЕСПЧ присудил Навальному €64 тыс. за незаконные задержания' , 'id' : '1213' , 'img' : 'img/1.jpg'},
			{ 'title' : 'ЕСПЧ присудил Навальному €64 тыс. за незаконные задержания' , 'id' : '1213' , 'img' : 'img/1.jpg'},
			{ 'title' : 'ЕСПЧ присудил Навальному €64 тыс. за незаконные задержания' , 'id' : '1213' , 'img' : 'img/1.jpg'},
			{ 'title' : 'ЕСПЧ присудил Навальному €64 тыс. за незаконные задержания' , 'id' : '1213' , 'img' : 'img/1.jpg'}
		]
	}) 
	return render_template('index.html', data = model)

@app.route("/i/<int:post_id>/")
def item(post_id): 
	model.update({
			'news' : {
				'title' : 'Трамп пообещал отменить «нелепое» судебное решение по миграционному указу',
				'text' : 'Президент',
				'img' : '',
				'id' : '' 
			}
	}) 
	return render_template('item.html', data = model)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0') 
