import functools
from flask import(
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint('index', __name__, url_prefix='/index')


@bp.route('/student', methods=('GET', 'POST'))
def index_student():
    return render_template('index.html')


@bp.route('/comitee', methods=('GET', 'POST'))
def index_comitee():
    return render_template('index.html')


@bp.route('/teacher', methods=('GET', 'POST'))
def index_teacher():
    return render_template('index.html')
