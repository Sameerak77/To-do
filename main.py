from flask import Flask,render_template,request,url_for,redirect
from flask_sqlalchemy import SQLAlchemy 
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///blog.db'
db=SQLAlchemy(app)
@app.route('/')
def home():
	tits=To.query.all()
	return render_template('home.html',values=tits)
	
@app.route('/all')
def all():
	tits=To.query.all()
	return render_template('home.html',values=tits)

@app.route('/add',methods=['POST'])
def add():
	title=request.form.get('title')
	ele=To(title=title,complete=False)
	db.session.add(ele)
	db.session.commit()
	return redirect(url_for('all'))

@app.route('/update/<int:to_id>')
def update(to_id):
	ids=To.query.filter_by(id=to_id).first()
	ids.complete = not ids.complete
	db.session.commit()
	return redirect(url_for('all'))

@app.route('/delete/<int:to_id>')
def delete(to_id):
	ids=To.query.filter_by(id=to_id).first()
	db.session.delete(ids)
	db.session.commit()
	return redirect(url_for('all'))

class To(db.Model):
	id=db.Column(db.Integer(),primary_key=True)
	title=db.Column(db.String(100))
	complete=db.Column(db.Boolean())





