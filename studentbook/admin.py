from flask import Blueprint, g, render_template, redirect, request, url_for
from studentbook.db import get_db

bp = Blueprint('Admin', __name__, url_prefix='/Admin')


@bp.route('/data', methods=('GET', 'POST'))
def get_data():
    if request.method == 'POST':
        admin_name = request.form['admin_name']
        admin_password = request.form['admin_pass']
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
            return redirect(url_for('showall'))
        else:
            return redirect(url_for('showall'))


@bp.route('/showall', methods=('GET', 'POST'))
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
