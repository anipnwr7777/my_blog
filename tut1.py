from flask import Flask, render_template   # flask module me se flask class import ki
app = Flask(__name__)     # app define ki

@app.route('/')           # jab bhi koi user mere website ki is endpoint pe jaye to ye function call hona chaiye.
def hello_world():
    return render_template('index.html')    # aur ye function hello world print kar raha.

@app.route('/contact')           
def anirudh():
    return render_template('about.html') 

if( __name__ == "__main__"):
    app.run(debug=True)

# debug = true kar lo warna reload hi nhi hoga kuch bhi karoge to.