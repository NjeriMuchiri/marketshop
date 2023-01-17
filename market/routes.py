from market import app
from flask import render_template, redirect,url_for,flash,request
from market.models import Item,User
from market.forms  import RegisterForm,LoginForm,PurchaseItemForm
from market import db
from flask_login import login_user,current_user

@app.route("/")
@app.route('/home')
def home_page():
    return render_template('home.html')
@app.route('/market', methods=['GET', 'POST'])
def market_page():
    purchase_form = PurchaseItemForm()
    if request.method == "POST":
       purchased_item = request.form.get('purchased_item')
       p_item_object = Item.query.filter_by(name=purchased_item).first()
       if p_item_object:
           p_item_object.owner = current_user.id
           current_user.budget -= p_item_object.price
           db.session.commit()
           flash(f'Congratulations!you purchased {p_item_object.name} for {p_item_object.price}')
    if request.method == 'GET':     
        items = Item.query.filter_by(owner=None)
        return render_template('market.html', items=items, purchase_form=purchase_form)

        

@app.route('/register', methods=['GET','POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,
                              email_address=form.email_address.data,
                              password=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('market_page'))
    if form.errors != {}:#if there are not errors from the validations
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a user: {err_msg}',category='danger')
    
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(attempted_password = form.password.data):
            login_user(attempted_user)
            flash(f'{attempted_user.username} has been logged in successfuly!', category='success')
            return redirect(url_for('market_page'))
        else:
            flash(f'Username and password for {attempted_user.username} do not match. Please try Again! ', category='danger')
        
    return render_template('login.html', form=form)
    


















