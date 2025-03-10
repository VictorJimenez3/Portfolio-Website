from flask import Flask, render_template

app = Flask(__name__)

# Define routes
@app.route('/')
def animation():
    return render_template('animation.html')

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/example')
def example():
    return render_template('example.html')
'''
@app.route('/test')
def test():
    return render_template('test.html')
'''
@app.route('/projects')
def projects():
    return render_template("projects.html")

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
