from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)


@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name

@app.route('/form',methods = ['POST'])
def form():
    if request.method == 'POST':
        living_area = request.form['living area']
        # return redirect(url_for('success',name = user))
        # return f"the living area is :{living_area}"
        
        return render_template('result.html', est_price=living_area)
    

if __name__ == '__main__':
    app.run(port=5000, debug=True)