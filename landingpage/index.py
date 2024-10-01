from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('aims-and-scope.html')


@app.route('/aims-and-scope')
def aims_and_scope():
    return render_template('aims-and-scope.html')


@app.route('/archive')
def archive():
    return render_template('archive.html')


@app.route('/contacts')
def contacts():
    return render_template('contacts.html')


@app.route('/current-issue')
def current_issue():
    return render_template('current-issue.html')


@app.route('/editorial-board')
def editorial_board():
    return render_template('editorial-board.html')


@app.route('/history')
def history():
    return render_template('history.html')


@app.route('/instructions-for-authors')
def instructions_for_authors():
    return render_template('instructions-for-authors.html')


@app.route('/instructions-for-editors')
def instructions_for_editors():
    return render_template('instructions-for-editors.html')


@app.route('/instructions-for-reviewers')
def instructions_for_reviewers():
    return render_template('instructions-for-reviewers.html')


@app.route('/submission')
def submission():
    return render_template('submission.html')


@app.route('/terms-and-conditions')
def terms_and_conditions():
    return render_template('terms-and-conditions.html')


if __name__ == '__main__':
    app.run(debug=True)

