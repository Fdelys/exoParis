# from flask import Flask
# from flask_bootstrap import Bootstrap
# from flask import render_template
# from flask import make_response
# from flask import request, redirect
# from flask_wtf import FlaskForm
# from wtforms import StringField, SubmitField
# from wtforms.validators import DataRequired, Length, Email
# from flask_wtf.file import FileField 

# import re


# app = Flask(__name__)
# # app.config['SECRET_KEY'] = 'Les hamburgers sont des navettes spatiales filant en raviolis'


# # class NameForm(FlaskForm):
# #     pattern_1 = StringField('Premier pattern', validators=[DataRequired(), Length(4)])
# #     pattern_2 = StringField('Deuxième pattern', validators=[DataRequired(), Length(4)])
# #     text = StringField('Votre texte ici', validators=[DataRequired(), Length(10)])
# #     submit = SubmitField('Submit')

# # @app.route('/')
# # def acceuil():
# #     return "Hello you"
    
# # @app.route('/text', methods=['GET', 'POST'])
# # def remplir():
# #     pattern_1 = ""
# #     pattern_2 = ""
# #     text = None
# #     count_1 = 0
# #     count_2 = 0
# #     form = NameForm()
# #     if form.validate_on_submit():
# #         pattern_1 = form.pattern_1.data
# #         pattern_2 = form.pattern_2.data
# #         text = form.text.data
# #         #form.name.data = ''
# #         a = re.findall(pattern_1, text.lower())
# #         b = re.findall(pattern_2, text.lower())
# #         for i in a:
# #             count_1+=1
# #         for j in b:
# #             count_2+=1
# #     return render_template('text.html', form=form, text=text, count_1=count_1, count_2=count_2)

# bootstrap = Bootstrap(app)
# app.config['SECRET_KEY'] = 'bisous carlos'
# app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024

# class FileForm(FlaskForm):
#     file = FileField('File')
#     submit = SubmitField("Submit")

# @app.route('/')
# def welcome( ):
#    return render_template('welcome.html')

# @app.route('/file', methods=['GET', 'POST'])
# def bootstrap():
#     form = FileForm()
#     if form.validate_on_submit():
#         uploaded_file = form.file.data
#         if uploaded_file.filename != '':
#             uploaded_file.save(uploaded_file.filename)
#         # Faire le traitement sur le fichier
#     return render_template("welcome.html", form=form)

import os
from flask import Flask
from flask import render_template
from flask_wtf import FlaskForm
from flask_wtf.file import FileField 
from wtforms import SubmitField
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

from dash import Dash, dcc, html

app = Flask(__name__)
dash_app = Dash(
    __name__,
    server=app,
    url_base_pathname='/dash/'
)

dash_app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),
    html.Div(children='''
        Dash: Rapid move in a direction resulting from a special ability
    '''),
])


@app.route("/dash")
def my_dash_app():
    return dash_app.index()