from flask import Flask, render_template, url_for, request

app = Flask(__name__)


@app.route('/index/')
@app.route('/')
def index():
    mytitle = 'this is from code!'
    return render_template('index.html', title= mytitle)

@app.route('/contact', methods=('GET', 'POST'))
def contact():
    if request.method == 'POST':
        obj = {'name': request.form['name'],
               'email': request.form['email'],
               'comment': request.form['comment']}
        return render_template('contact.html', usercomment= obj, title= 'form sent!')
    else:
        title = 'contact form!'
        return render_template('contact.html', title= title)

@app.route('/about')
def about():
    title = 'about us!'
    return render_template('about.html', title= title)


if __name__ == '__main__':
    app.run(debug=True)

