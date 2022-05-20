from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class LibraryForm(FlaskForm):
    book_name = StringField(label="Book Name", validators=[DataRequired('Field Cannot Be Blank')])
    book_author = StringField("Book Author", validators=[DataRequired('Field Cannot Be Blank')])
    rating = SelectField(label='Rating', choices=['⭐', '⭐⭐', '⭐⭐⭐', '⭐⭐⭐⭐', '⭐⭐⭐⭐⭐'])
    submit = SubmitField('Submit')


all_books = []


@app.route('/')
def home():
    return render_template("index.html")


@app.route("/add", methods=["post", "get"])
def add():
    # use below code if using wtf quick form
    # library_form = LibraryForm()
    # if library_form.validate_on_submit():
    #     print("True")
    # return render_template("add_wtf_quick_form.html", form=library_form)
    # new_entry = {}
    test = request.form['bookname']
    print(test)
    # new_entry['author'] = request.form['bookauthor']
    # new_entry['rating'] = request.form['bookrating']
    return render_template('add.html')

if __name__ == "__main__":
    app.run(debug=True)

