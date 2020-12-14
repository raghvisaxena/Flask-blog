from flask import Flask,render_template,url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY']= 'a60773a584fe792fd8ec9061e7ca6c00'

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

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)



if __name__=='__main__':
    app.run(debug=True)
