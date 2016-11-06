from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    mytitle = 'this is from code!'
    return render_template('index.html', title= mytitle)

@app.route('/contact')
def contact():
    title = 'contact form!'
    return render_template('contact.html', title= title)

@app.route('/about')
def about():
    title = 'about us!'
    return render_template('about.html', title= title)


if __name__ == '__main__':
    app.run()

