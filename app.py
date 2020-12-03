from flask import Flask,render_template,url_for
app = Flask(__name__)

posts=[
    {
        'author':'raghvi',
        'title':'first blog',
        'content':'lorem ipsum dolor si amet',
        'date_posted':'December 3,2020'
    },
    {
        'author':'dummy',
        'title':'blog two',
        'content':'lorem ipsum dolor si',
        'date_posted':'December 2,2020'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html',title='About')

if __name__=='__main__':
    app.run(debug=True)
