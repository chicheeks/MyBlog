from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def welcome():
    return render_template('index.html')


@app.route('/comment', methods=['GET', 'POST'])
def commentMenu():
    name = ""
    if request.method == 'POST' and 'username' in request.form:
        name = request.form.get('username')
        comment = request.form.get('comment')
        commentFile = open('Websitecomments.txt', 'a')
        commentFile.write(comment + ' by ' + name + '\n')
        commentFile.close()
    return render_template('comment.html',
                           name=name)


@app.route('/view_comments', methods=['GET', 'POST'])
def view_comments():
    with open("Websitecomments.txt", "r") as data_file:
        for line in data_file.readlines():
            data = line.split()

    return render_template('view_comments.html', column_names=['Comment by Name'],
                           data=data, line=line, data_file=open("Websitecomments.txt", "r"))


@app.route('/progress')
def progressMenu():
    return render_template('progress.html')


@app.route('/contact')
def contactMenu():
    return render_template('contact.html')


if __name__ == "__main__":
    app.run(debug=True)
