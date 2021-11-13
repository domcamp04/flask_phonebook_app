from app import app, db
from flask import render_template, url_for, redirect, flash
from app.forms import LoginForm, UserInfoForm, EntryForm
from app.models import Phonebook, User
from flask_login import login_user, logout_user, login_required



@app.route('/')
def index():
    contacts = Phonebook.query.all()

    return render_template('index.html', contacts=contacts)



@app.route('/register', methods=['GET', 'POST'])
def register():
    register_form = UserInfoForm()
    if register_form.validate_on_submit():
        username = register_form.username.data
        email = register_form.email.data
        password = register_form.password.data

        existing_user = User.query.filter_by(username=username).all()
        if existing_user:
            flash(f'The username {username} is already in use. Please try again.', 'danger')
            return redirect(url_for('register'))
       
        new_user = User(username, email, password)
        db.session.add(new_user)
        db.session.commit()

        flash(f'Thank you {username} for registering.', 'success')
        return redirect(url_for('index'))

    return render_template('register.html', form=register_form)



@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = User.query.filter_by(username=username).first()


        if user is None or not user.check_password(password):
            flash('Your username or password is incorrect', 'danger')
            return redirect(url_for('login'))

        login_user(user)

        flash(f'Welcome {user.username}. You have successfully logged in.', 'success')
        return redirect(url_for('index'))
    return render_template('login.html', login_form=form)



@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))



@app.route('/new-entry', methods=['GET', 'POST'])
@login_required
def new_entry():
    entry = EntryForm()
    if entry.validate_on_submit():
        first = entry.first_name.data
        last = entry.last_name.data
        phone = entry.phone.data
        email = entry.email.data
        address = entry.address.data

        new_contact = Phonebook(first, last, phone, email, address)
        db.session.add(new_contact)
        db.session.commit()

        flash('Your entry has been added to the phone book.', 'success')
        return redirect(url_for('index'))
    return render_template('new_entry.html', form=entry)



@app.route('/delete_contact/<phonebook_id>', methods=['POST'])
@login_required
def delete_contact(phonebook_id):
    phonebook_id = Phonebook.query.get_or_404(phonebook_id)

    db.session.delete(phonebook_id)
    db.session.commit()
    flash('The entry has been deleted', 'success')
    return redirect(url_for('index'), phonebook_id=phonebook_id)