from model import app, db, Questions, Options
from flask import render_template, request, redirect, url_for


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/adddata', methods=['POST'])
def add_data():
    question = request.form.get('question_body')
    correct = request.form.get('correct_answer')
    option1 = request.form.get('option1')
    option2 = request.form.get('option2')
    option3 = request.form.get('option3')

    q = Questions(question)
    db.session.add(q)
    db.session.commit()

    c = Options(correct, q.id)
    db.session.add(c)

    o1 = Options(option1, q.id)
    db.session.add(o1)

    o2 = Options(option2, q.id)
    db.session.add(o2)

    o3 = Options(option3, q.id)
    db.session.add(o3)
    db.session.commit()

    return redirect(url_for('home'))
