from flask import Flask,render_template
app=Flask(__name__);
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/aboutICT')
def about():
    return render_template('aboutICT.html')
@app.route('/servicesICT')
def services():
    return render_template('servicesICT.html')

if __name__ == '__main__':
    app.run(debug=True)
