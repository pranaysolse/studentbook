import time
import functools
from flask import(
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from werkzeug.security import check_password_hash, generate_password_hash

from studentbook.db import get_db
from studentbook import forms
from studentbook.index import *

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/register_s', methods=('GET', 'POST'))
def register_student():
    form = forms.RegisterFormSt()
    if request.method == 'POST':
        print(str(request.data))
        username = request.form['username']
        print(username)
        password = request.form['password']
        name = request.form['name']
        print(name)
        divison = request.form['div']
        class_st = request.form['class_st']
        branch = request.form['branch']
        mobile = request.form['mob']
        email = request.form['email']
        address = request.form['add']
        # for i, v in request.form:
        #    print(i, '=', v)
        print(request.form)
        for i in request.form:
                print(i)
        db = get_db()
        error = None
        if not username:
            error = 'username is required.'
        elif not password:
            error = 'password is required'
        elif db.execute(
            'SELECT id FROM student WHERE username = ?', (username,)
        ).fetchone() is not None:
            error = f'user {username} is already registered'
            print(error)
            return redirect(url_for('auth.login_student'))
        if error is None:
            db.execute(
                '''INSERT INTO student (names, class, branch, divison,email,mobile,
                asddress,username, password)
                 VALUES (?,?,?,?,?,?,?,?,?)''',
                (name, class_st, branch, divison, email, mobile,
                 address, username, generate_password_hash(password))
            )
            db.commit()
            print("commited")
            return redirect(url_for('auth.login_student', username=username))
        print("flashing now")
        flash(error)
        if error is not None:
            print(error)
    return render_template("register_student.html",
                           title="Register-Student", form=form)


@bp.route('/login_s', methods=('GET', 'POST'))
def login_student():
    form = forms.LoginForm()
    error = None
    if request.method == 'POST':
        flash("login form")
        print(str(request.data))
        username = request.form['username']
        print(username)
        password = request.form['password']
        print(password)
        user_type = request.form['user_type']
        db = get_db()
        if username is None:
            error = 'username is required '
        elif password is None:
            error = 'password is required'
        elif user_type is None:
            error = 'user type is required'
        elif user_type != 'st':
            error = 'user type is wrong'
            print(error)
            flash(error)
            return render_template('login.html',
                                   title='login student', form=form,
                                   error=error)
        else:
            user = db.execute(
                'SELECT * FROM student WHERE username = ?', (username,)
            ).fetchone()
            print('executing')
            db.execute('SELECT * FROM student WHERE username = ?', (username,))
        if user is None:
            error = 'incorrect username'
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password'
        print(error)
        if error is None:
            print("error is None")
            session.clear()
            session['username'] = user['username']
            session['name'] = 'pranay'
            print(session['name'])
            # return redirect(url_for('index.index_student'))
            # return redirect(url_for('index.index_student'))
            return render_template("index.html", title="student")
            return None
        print("flashing now")
        flash(error)
    return render_template('login.html', title='login student', form=form,
                           error=error)

# ------------------------------------------------------------------------------------------
# ////////////////////////////////////////////////////////////////////////////////////////


@bp.route('/register_t', methods=('GET', 'POST'))
def register_teacher():
    form = forms.RegisterFormte()

    if request.method == 'POST':
        print(str(request.data))
        username = request.form['username']
        print(username)
        password = request.form['password']
        db = get_db()
        error = None

        if not username:
            error = 'username is required.'
        elif not password:
            error = 'password is required'
        elif db.execute(
            'SELECT id FROM teacher WHERE username = ?', (username,)
        ).fetchone() is not None:
            error = f'user {username} is already registered'
            print(error)
            return redirect(url_for('auth.login_teacher'))
        if error is None:
            db.execute(
                'INSERT INTO teacher (username,password) VALUES (?,?)',
                (username, generate_password_hash(password))
            )
            db.commit()
            print("commited")
            return redirect(url_for('auth.login_teacher'))
        print("flashing now")
        flash(error)
        if error is not None:
            print(error)
    return render_template("register_teacher.html", title="Register-teacher",
                           form=form)


@bp.route('/login_t', methods=('GET', 'POST'))
def login_teacher():
    form = forms.LoginForm()
    error = None
    if request.method == 'POST':
        flash("login form")
        print(str(request.data))
        username = request.form['username']
        password = request.form['password']
        user_type = request.form['user_type']
        db = get_db()

        if username is None:
            error = 'username is required '
        elif password is None:
            error = 'password is required'
        elif user_type is None:
            error = 'user type is required'
        elif user_type != 'te':
            error = 'wrong user type '
            print(error, 'huh')
            flash(error)
            return render_template('login.html',
                                   title='login teacher', form=form,
                                   error=error)
        else:
            user = db.execute(
                'SELECT * FROM teacher WHERE username = ?', (username,)
            ).fetchone()
        if user is None:
            error = 'incorrect username'
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password'
        print(error, ' huh')
        if error is None:
            print("error is None")
            session.clear()
            session['user_id'] = user['id']
            error = ''
            return redirect(url_for('index.index_teacher'))
            return None
        print("flashing now")
        flash(error)
    return render_template('login.html', title='login teacher', form=form,
                           error=error)

# -----------------------------------------------------------------------------
# /////////////////////////////////////////////////////////////////////////////


@bp.route('/register_c', methods=('GET', 'POST'))
def register_comitteehead():
    form = forms.RegisterFormco()
    if request.method == 'POST':
        print(str(request.data))
        username = request.form['username']
        print(username)
        password = request.form['password']
        db = get_db()
        error = None

        if not username:
            error = 'username is required.'
        elif not password:
            error = 'password is required'
        elif db.execute(
            'SELECT id FROM comitteehead WHERE username = ?', (username,)
        ).fetchone() is not None:
            error = f'user {username} is already registered'
            print(error)
            return redirect(url_for('auth.login_committee'))
        if error is None:
            db.execute(
                'INSERT INTO comitteehead (username,password) VALUES (?,?)',
                (username, generate_password_hash(password))
            )
            db.commit()
            print("commited")
            return redirect(url_for('auth.login_committee'))
        print("flashing now")
        flash(error)
        if error is not None:
            print(error)
    return render_template("register_committee.html",
                           title="Register-teacher", form=form)


@bp.route('/login_c', methods=('GET', 'POST'))
def login_committee():
    form = forms.LoginForm()
    error = None
    if request.method == 'POST':
        flash("login form")
        print(str(request.data))
        username = request.form['username']
        password = request.form['password']
        user_type = request.form['user_type']
        db = get_db()

        if username is None:
            error = 'username is required '
        elif password is None:
            error = 'password is required'
        elif user_type is None:
            error = 'user type is required'
        elif user_type != 'co':
            error = 'user type is wrong'
            flash(error)
            return render_template('login.html',
                                   title='login commitee', form=form,
                                   error=error)
        else:
            user = db.execute(
                'SELECT * FROM comitteehead WHERE username = ?', (username,)
            ).fetchone()
        print(username)
        if user is None:
            error = 'incorrect username'
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password'
        print(error)
        if error is None:
            print("error is None")
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('index.index_comitee'))
            return None
        print("flashing now")
        flash(error)
    return render_template('login.html', title='login commitee', form=form,
                           error=error)


@bp.route('/logout_c', methods=('GET', 'POST'))
def logout_comittee():
    session.pop('username', None)
    return redirect(url_for('home'))


@bp.route('/logout_t', methods=('GET', 'POST'))
def logout_teacher():
    session.pop('username', None)
    return redirect(url_for('home'))


@bp.route('/logout_s', methods=('GET', 'POST'))
def logout_student():
        session.pop('username', None)
        return redirect(url_for('about'))
    # return redirect(url_for('home'))
