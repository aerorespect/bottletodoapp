from bottle import route, run, template, debug, request, redirect, static_file
#import requests
import mysql.connector

"""
generate webpage to display all task, either completed or not
"""
@route('/')
def all_task():
    mydb = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        passwd='Fandri54',
        database='todoapp'
    )
    c = mydb.cursor()
    c.execute("SELECT id, task, status FROM todo")
    result = c.fetchall()
    c.close()
    output = template('make_table', rows=result)
    return output

"""
generate webpage to display current todo list
"""
@route('/todo')
def todo_list():
    mydb = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        passwd='Fandri54',
        database='todoapp'
    )
    c = mydb.cursor()
    c.execute("SELECT id, task, status FROM todo WHERE status LIKE '1'")
    result = c.fetchall()
    c.close()
    output = template('make_table', rows=result)
    return output


"""
generate webpage to add new todo list
"""
@route('/new', method='GET')
def new_item():
    if request.GET.save:
        new = request.GET.task.strip()

        mydb = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            passwd='Fandri54',
            database='todoapp'
        )
        c = mydb.cursor()

        c.execute("INSERT INTO todo (task,status) VALUES (%s,%s)", (new, 1))
        # new_id = c.lastrowid

        mydb.commit()
        c.close()
        redirect("/")
        # return '<p>The new task was inserted into the database, the ID is %s</p>' % new_id
    else:
        return template('new_task.tpl')

"""
generate webpage to edit current new todo list
"""
@route('/edit/<no:int>', method='GET')
def edit_item(no):
    mydb = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        passwd='Fandri54',
        database='todoapp'
    )
    c = mydb.cursor()
    c.execute("UPDATE todo SET status = IF(status = 1, 0, 1) WHERE id = %s", (str(no),))
    mydb.commit()
    redirect("/")


debug(True)

run(host='localhost', port=8080)
