from flask import Flask,render_template
app = Flask(__name__)

JOBS = [
    {
    'id' : 1,
    'title' : 'Data Analyst',
    'location' : 'Benganluru, India',
    'salary' : 'Rs, 1000000',
    },
    {
    'id' : 2,
    'title' : 'Data Analyst',
    'location' : 'Delhi, India',
    'salary' : 'Rs, 1500000',
    },
    {
    'id' : 3,
    'title' : 'Forntend Engineer ',
    'location' : 'Remote',
    'salary' : 'Rs, 1200000',
    },
    {
    'id' : 4,
    'title' : 'Backend engineer ',
    'location' : 'Benganluru, India',
    'salary' : 'Rs, 1000000',
    },
]

@app.route("/")
def hello_world():
    return render_template('home.html',jobs=JOBS,company_name ='Microsoft')

if __name__ == '__main__':
    app.run(debug=True)

   