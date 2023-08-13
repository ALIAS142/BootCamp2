from flask import Flask, render_template
from LoginForm import Lf
from AuthForm import AuthF

app = Flask(__name__)
app.config ['SECRET_KEY'] = 'hello hello hello hello hello world'

@app.route('/')
@app.route('/index')

def main():
    return render_template('base.html') 

@app.route('/register', methods=['GET', 'POST'])  
def reg():
    form = Lf()
    if form.validate_on_submit():
        if form.password_again.data!=form.password.data:
            return render_template('register.html', title='Registration', form=form, message='Passwords are not matched')


        with open('file.txt', 'a', encoding='utf-8') as file:
            file.write(f'{form.name.data};{form.email.data};{form.password.data}\n')

        return render_template('register.html', message='Registration is succesful')
    return render_template('register.html', title='Registration', form=form)

@app.route('/log', methods=['GET', 'POST'])
def log():
    form=AuthF()
    if form.validate_on_submit():
        with open('file.txt', 'r', encoding='utf-8') as file:
            data =' '.join(file.readlines())

        if form.email.data not in data:
            return render_template('login.html', form=form, message='You are not registrated')
        else:
            for i in data.split():
                if form.email.data in i:
                    if i.split(';')[-1] == form.password.data:
                        return render_template('login.html', form=form, message='You are regisstred succsed')

    return render_template('login.html', form=form)


if __name__=='__main__':
    app.run()