from flask import Flask
from flask import render_template

app = Flask(__name__)


MENU_ITEMS = [
    ('aims_and_scope', 'Aims and Scope'),
    ('editorial_board', 'Editorial Board'),
    ('history', 'History'),
    ('submission', 'Submission'),
    ('instructions_for_authors', 'Instructions for Authors'),
    ('instructions_for_editors', 'Instructions for Editors'),
    ('instructions_for_reviewers', 'Instructions for Reviewers'),
    ('current_issue', 'Current Issue'),
    ('archive', 'Archive'),
    ('contacts', 'Contacts'),
    ('terms_and_conditions', 'Terms and Conditions')
]


@app.route('/')
def default_page():
    return render_template('home.html', menu_items=MENU_ITEMS)


@app.route('/home')
def home():
    return render_template('home.html', menu_items=MENU_ITEMS)


@app.route('/aims-and-scope')
def aims_and_scope():
    return render_template('aims-and-scope.html', menu_items=MENU_ITEMS)


@app.route('/archive')
def archive():
    return render_template('archive.html', menu_items=MENU_ITEMS)


@app.route('/contacts')
def contacts():
    return render_template('contacts.html', menu_items=MENU_ITEMS)


@app.route('/current-issue')
def current_issue():
    return render_template('current-issue.html', menu_items=MENU_ITEMS)


@app.route('/editorial-board')
def editorial_board():
    return render_template('editorial-board.html', menu_items=MENU_ITEMS)


@app.route('/history')
def history():
    return render_template('history.html', menu_items=MENU_ITEMS)


@app.route('/instructions-for-authors')
def instructions_for_authors():
    return render_template('instructions-for-authors.html', menu_items=MENU_ITEMS)


@app.route('/instructions-for-editors')
def instructions_for_editors():
    return render_template('instructions-for-editors.html', menu_items=MENU_ITEMS)


@app.route('/instructions-for-reviewers')
def instructions_for_reviewers():
    return render_template('instructions-for-reviewers.html', menu_items=MENU_ITEMS)


@app.route('/submission')
def submission():
    return render_template('submission.html', menu_items=MENU_ITEMS)


@app.route('/terms-and-conditions')
def terms_and_conditions():
    return render_template('terms-and-conditions.html', menu_items=MENU_ITEMS)


if __name__ == '__main__':
    app.run(debug=True)

