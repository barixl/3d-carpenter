from flask import Flask, render_template, request

app = Flask(__name__)

@app.after_request
def add_header(response):
    if 'static/' in request.path:
        response.headers['Cache-Control'] = 'public, max-age=31536000'
    return response

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
