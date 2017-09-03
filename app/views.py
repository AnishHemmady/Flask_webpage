from flask import render_template,flash, redirect
from app import app
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index_page():
	user={'name':"ANISH"}
	posts=[{ 'author':{'name':"Rahul"},
			'body':'Good day in Indy'},
			{ 'author':{'name':"Vijay"},
			'body':'Good day in Ohio'}
			]
	return render_template("index.html",title="Home",posts=posts,user=user)
	

@app.route('/login',methods=['GET','POST'])
def login():	
	form=LoginForm()
	if form.validate_on_submit():
		flash('Login requested for OpenID="%s", remember_me=%s' %
				  (form.openid.data, str(form.remember_me.data)))
		return redirect('/index')
	return render_template('login.html', 
						   title='Sign In',
						   form=form,
						   providers=app.config['OPENID_PROVIDERS'])

