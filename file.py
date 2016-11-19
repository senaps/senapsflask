from flask import Flask, render_template, url_for, request, session, redirect, flash

app = Flask(__name__)
app.config['SECRET_KEY']= 'youd never guessed it! :)'

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

@app.route('/login')
def log_in():
    title = 'login page!'
    return render_template('login.html', title= title)

@app.route('/loginsuccess', methods=['POST'])
def login_success():
    session['name'] = request.form['name']
    session['log_in'] = True
    flash('success!')
    return redirect(url_for('index'))

@app.route('/logout')
def log_out():
    session.pop('name')
    session['log_in']= False
    return redirect(url_for('index'))


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

if __name__ == '__main__':
    app.run(debug=True)

