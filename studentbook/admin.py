from flask import Blueprint, g, render_template, redirect, request, url_for
from studentbook.db import get_db
from studentbook.forms import LoginForm
bp = Blueprint('Admin', __name__, url_prefix='/Admin')


@bp.route('/data', methods=('GET', 'POST'))
def get_data():
    form = LoginForm()
    if request.method == 'POST':
        admin_name = request.form['username']
        admin_password = request.form['password']
        db = get_db()
        error = None
        if not admin_name:
            error = 'admin name is required'
        if not admin_password:
            error = 'admin password is required'
        elif db.execute(
            'SELECT id FROM admin WHERE adminname = ?', (admin_name,)
        ).fetchone() is not None:
            print('legit admin')
            # return redirect(url_for('Admin.showall'))
            student_list = []
            db = get_db()
            for i in range(1, 100):
                a = (db.execute(
                    ''' SELECT username, password,
                    id, names, mobile, asddress, class,
                    branch, divison
                    FROM student
                     WHERE id = ?''', (i,)
                ).fetchone())
                if a is not None:
                    for member in a:
                        student_list.append(member)
                        print(student_list)
                        print(member, end=' ')
                    print()
    # return redirect(url_for('home'))
            return render_template("showall.html", title="show all",
                                   student_list=student_list)
        else:
            return render_template('adminlogin.html',
                                   tiltle='admin', form=form)
    return render_template('adminlogin.html', title='admin', form=form)


""" @bp.route('/showall', methods=('GET', 'POST'))
def showall():
    student_list = []
    db = get_db()
    for i in range(1, 100):
        a = (db.execute(
            'SELECT username, password FROM student WHERE id = ?', (i,)
        ).fetchone())
        if a is not None:
            for member in a:
                student_list.append(member)
                print(student_list)
                print(member, end=' ')
            print()

    # return redirect(url_for('home'))
    return render_template("showall.html", title="show all",
                           student_list=student_list)
"""
