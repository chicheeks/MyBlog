#!python3

from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def welcome():
    return render_template('index.html')


@app.route('/comment', methods=['GET', 'POST'])
def commentMenu():
    name = ''
    if request.method == 'POST' and 'username' in request.form:
        name = request.form.get('username')
        comment = request.form.get('comment')
        commentFile = open('C:\\Users\\PC\\Documents\\Websitecomments.txt', 'a')
        commentFile.write(comment + '\n by ' + name + '\n')
    return render_template('comment.html',
                           name=name)


@app.route('/progress')
def progressMenu():
    return render_template('progress.html')


@app.route('/contact')
def contactMenu():
    return render_template('contact.html')


app.run(debug=True)
