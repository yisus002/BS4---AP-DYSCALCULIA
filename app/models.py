from app import db

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    group = db.Column(db.String(32), index=True)
    subject = db.Column(db.String(64), index=True)
    grade = db.Column(db.Float)

    def __repr__(self):
        return f'<Student {self.name}>'