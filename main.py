from flask import Flask
from flask import render_template
from flask import request  
from flask import session, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json


with open('config.json', 'r') as c:
    params = json.load(c)["params"]

local_server = True

app = Flask(__name__)   
app.secret_key = "super-secret-key"  
if (local_server):
    app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri']
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/codethunder'
db = SQLAlchemy(app)       # initialize the db variable




class Contacts(db.Model):

    '''  sno, name, email, phone_num, mes, date  '''
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(20), unique=True, nullable=False)
    phone_num = db.Column(db.String(12), unique=True, nullable=False)
    mes = db.Column(db.String(120), unique=False, nullable=False)
    date = db.Column(db.String(12), unique=False, nullable=True)


class Posts(db.Model):

    '''  sno, title, content , date, slug  '''
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=False, nullable=False)
    content = db.Column(db.String(120), unique=False, nullable=False)
    date = db.Column(db.String(12), unique=False, nullable=True)
    slug = db.Column(db.String(20), unique=False, nullable=False)
    img_file = db.Column(db.String(20), unique=False, nullable=False)
    tagline = db.Column(db.String(120), unique=False, nullable=False)





@app.route('/')           
def home():
    posts = Posts.query.filter_by().all()
    return render_template('index.html', params = params, posts=posts)    


@app.route('/dashboard', methods= ['GET', 'POST'])           
def login():

    ''' if the user is already logged in '''
    if('user' in session and session['user'] == params["admin_user"]):
        posts = Posts.query.all()
        return render_template('dashboard.html', params = params, posts= posts)

    if(request.method == 'POST'):
        '''SEND THEM TO THE ADMIN PANEL'''
        username = request.form.get('uname')
        password = request.form.get('pass')

        if(username == params['admin_user'] and password == params['admin_password']):
            ''' set the session variable '''
            session['user'] = username
            posts = Posts.query.all()
            return render_template('dashboard.html', params = params, posts = posts)
        else:
            return render_template('login.html', params = params) 



    else:
        ''' tell them to login again'''
        return render_template('login.html', params = params)    






@app.route('/contact', methods = ['GET', 'POST'])           
def contact():

    ''' if there is a post request then add to database the content. '''
    if (request.method == 'POST'):
        '''  ADD ENTRY TO THE DATABASE  '''

        '''  this is the entry fetched from the form  '''
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')

        '''  now add this entry to the database '''
        ''' fields of the database table : sno, name, email, phone_num, mes, date  '''
        entry = Contacts(name = name, phone_num = phone, mes = message, email = email, date = datetime.now())
        
        db.session.add(entry)
        db.session.commit()

    '''   do this by default for a get request. '''
    return render_template('contact.html' , params = params) 


@app.route('/logout')
def logout():
    session.pop('user')           
    return redirect('/dashboard')



@app.route('/about')           
def about():
    return render_template('about.html' , params = params) 


@app.route("/delete/<string:sno>" , methods = ['GET', 'POST'])     
def delete(sno):
    if('user' in session and session['user'] == params["admin_user"]):
        post = Posts.query.filter_by(sno = sno).first()
        db.session.delete(post)
        db.session.commit()
    return redirect('/dashboard')




@app.route("/edit/<string:sno>" , methods = ['GET', 'POST'])     
def edit(sno):
    if('user' in session and session['user'] == params["admin_user"]):
        if(request.method == 'POST'):
            box_title = request.form.get('title')
            tline = request.form.get('tline')
            content = request.form.get('content')
            slug = request.form.get('slug')
            date = datetime.now()
            img_file = 'ajpg.jpg'

            if(sno == '0'):
                post = Posts( title=box_title, slug=slug, content=content, tagline=tline, date= date, img_file=img_file)
                db.session.add(post)
                db.session.commit()

            else:
                post = Posts.query.filter_by(sno = sno).first()
                post.title = box_title
                post.slug = slug
                post.content = content
                post.tagline = tline
                post.img_file = img_file
                post.date = date
                db.session.commit()
                return redirect('/edit/' + 'sno')

        post = Posts.query.filter_by(sno = sno).first()
        return render_template('edit.html', params = params, post=post, sno=sno)



@app.route("/post/<string:post_slug>" , methods = ['GET'])           
def post_route(post_slug):
    '''  the parameter has to be same as the string passed in app route  '''

    post = Posts.query.filter_by(slug = post_slug).first()
    return render_template('post.html' , params = params , post=post) 






if( __name__ == "__main__"):
    app.run(debug=True)
