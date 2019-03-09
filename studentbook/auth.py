import functools
from flask import(
	Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from werkzeug.security import check_password_hash, generate_password_hash

from studentbook.db import get_db
from studentbook import forms
bp = Blueprint('auth',__name__,url_prefix='/auth')

@bp.route('/register_s', methods=('GET','POST'))
def register_student():
	form = forms.RegisterFormSt()
		
	if request.method == 'POST':
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
			'SELECT id FROM student WHERE username = ?',(username,)
		).fetchone is not None:	
			error = f'user {username} is already registered'
			print(error)
		if error is None:	
			db.execute(
				'INSERT INTO student (username,password) VALUES (?,?)',
				(username, generate_password_hash(password))
			)
			db.commit()
		return redirect(url_for('home'))

		flash(error)

	return render_template("register_student.html",title="Register-Student",form=form)		
