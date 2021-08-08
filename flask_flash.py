from flask import Flask, render_template, flash, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)

app.config['SECRET_KEY'] = 'AOA'

class InfoForm(FlaskForm):
    
    group_name = StringField("당신이 좋아하는 그룹은 어디인가요?")
    submit = SubmitField('제출')
    
@app.route('/', methods=['GET','POST'])
def home():

    group_name = False
    form = InfoForm()

    if form.validate_on_submit():
        session['group_name'] = form.group_name.data
        # flash 부분은 get_flashed_messages에서 message부분에 나오는 글자입니다.
        flash('당신이 제출한 그룹의 이름은 ' + session['group_name'] + ' 입니다.')
        return redirect(url_for('home'))
    return render_template('home.html', form=form)



if __name__ == '__main__':
    app.run(debug=True)