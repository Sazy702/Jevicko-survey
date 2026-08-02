from flask import Flask,render_template,request

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    phone = request.form['phone']
    service = request.form['service']
    location = request.form['location']
    return f"<h1>Thank you {name}!</h1><p>We got your request for {service} at {location}. We will call you on {phone}</p>"

if __name__ == '__main__':
    app.run(debug=True)