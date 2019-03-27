import functools
from flask import(
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
import os

bp = Blueprint('index', __name__, url_prefix='/index')


@bp.route('/student', methods=('GET', 'POST'))
def index_student():
    items = None
    items = session
    timetable = get_list_timetable()
    syllabus = get_list_syllabus()
    events = get_list_events()
    notice = get_list_notice()
    assignment = get_list_assignment()
    return render_template('index.html', items=items,
                            timetable=timetable,
                            syllabus=syllabus,
                            events=events,
                            notice=notice,
                            assignment=assignment)



@bp.route('/comitee', methods=('GET', 'POST'))
def index_comitee():
    items = None
    items = session
    timetable = get_list_timetable()
    syllabus = get_list_syllabus()
    events = get_list_events()
    notice = get_list_notice()
    assignment = get_list_assignment()
    return render_template('index_c.html', items=items , 
                            timetable=timetable,
                            syllabus=syllabus,
                            events=events,
                            notice=notice,
                            assignment=assignment)

@bp.route('/teacher', methods=('GET', 'POST'))
def index_teacher():
    items = None
    items = session
    timetable = get_list_timetable()
    syllabus = get_list_syllabus()
    events = get_list_events()
    notice = get_list_notice()
    assignment = get_list_assignment()
    return render_template('index_t.html', items=items , 
                            timetable=timetable,
                            syllabus=syllabus,
                            events=events,
                            notice=notice,
                            assignment=assignment)


# timetable
def get_list_timetable():
    path = 'studentbook/static/uploads/timetable/'
    file_list = []
    filename = os.listdir(path)
    for filename in filename :
        var = os.path.join('/static/uploads/timetable/', filename)
        file_list.append(var) 
    print("filelist:",file_list)
    return file_list

# assignment
def get_list_assignment():
    path = 'studentbook/static/uploads/assignment/'
    file_list = []
    filename = os.listdir(path)
    for filename in filename :
        var = os.path.join('/static/uploads/timetable/', filename)
        file_list.append(var) 
    print("filelist:",file_list)
    return file_list


# syllabus
def get_list_syllabus():
    path = 'studentbook/static/uploads/syllabus/'
    file_list = []
    filename = os.listdir(path)
    for filename in filename :
        var = os.path.join('/static/uploads/syllabus/', filename)
        file_list.append(var) 
    print("filelist:",file_list)
    return file_list


# events
def get_list_events():
    path = 'studentbook/static/uploads/events/'
    file_list = []
    filename = os.listdir(path)
    for filename in filename :
        var = os.path.join('/static/uploads/events/', filename)
        file_list.append(var) 
    print("filelist:",file_list)
    return file_list


#notice
def get_list_notice():
    path = 'studentbook/static/uploads/notice/'
    file_list = []
    filename = os.listdir(path)
    for filename in filename :
        var = os.path.join('/static/uploads/notice/', filename)
        file_list.append(var) 
    print("filelist:",file_list)
    return file_list