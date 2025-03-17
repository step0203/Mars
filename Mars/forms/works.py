from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms import BooleanField, SubmitField
from wtforms.validators import DataRequired


class WorkForm(FlaskForm):
    team_leader = StringField('Team Leader id', validators=[DataRequired()])
    job = StringField('Задание', validators=[DataRequired()])
    work_size = StringField('Объем работы', validators=[DataRequired()])
    collaborators = StringField('Помощники id')
    is_finished = BooleanField("Закончено?")
    submit = SubmitField('Применить')
