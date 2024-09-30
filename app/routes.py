from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db
from app.models import Student
from app.forms import StudentForm, SearchForm
from app.data_analysis import generate_grade_distribution, calculate_statistics

bp = Blueprint('main', __name__)

@bp.route('/', methods=['GET', 'POST'])
def index():
    form = StudentForm()
    search_form = SearchForm()
    students = Student.query.all()


    if form.validate_on_submit():
        student = Student(name=form.name.data, group=form.group.data,
                          subject=form.subject.data, grade=form.grade.data)
        db.session.add(student)
        db.session.commit()
        flash('Student added successfully!')
        return redirect(url_for('main.index'))

    grades = [student.grade for student in students]
    plot_url = generate_grade_distribution(grades)
    stats = calculate_statistics(grades)

    return render_template('index.html', form=form, search_form=search_form,
                           students=students, plot_url=plot_url, stats=stats)

@bp.route('/search')
def search():
    query = request.args.get('search')
    students = Student.query.filter(
        (Student.name.contains(query)) |
        (Student.group.contains(query)) |
        (Student.subject.contains(query))
    ).all()
    return render_template('search_results.html', students=students)

@bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_student(id):
    student = Student.query.get_or_404(id)
    form = StudentForm(obj=student)
    if form.validate_on_submit():
        student.name = form.name.data
        student.group = form.group.data
        student.subject = form.subject.data
        student.grade = form.grade.data
        db.session.commit()
        flash('Student updated successfully!')
        return redirect(url_for('main.index'))
    return render_template('edit_student.html', form=form, student=student)

@bp.route('/delete/<int:id>')
def delete_student(id):
    student = Student.query.get_or_404(id)
    db.session.delete(student)
    db.session.commit()
    flash('Student deleted successfully!')
    return redirect(url_for('main.index'))