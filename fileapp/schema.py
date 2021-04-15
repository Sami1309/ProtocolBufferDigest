from fileapp import db
from datetime import datetime


#Schema definitions for internal database

class Report(db.Model):
    __tablename__ = 'report'
    id = db.Column(db.Integer, db.ForeignKey('process.report_no'), primary_key=True)
    created_date = db.Column(db.DateTime, default=datetime.now)


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    security_identifier = db.Column(db.String(100))
    username = db.Column(db.String(100))
    domain = db.Column(db.String(100))
    
    processes = db.relationship('Process', backref='author', lazy=True)

    def __repr__(self):
        return f'User(id:{self.id}, security_identifier:{self.security_identifier}, username:{self.username}, domain:{self.domain})'

class Process(db.Model):
    __tablename__ = 'process'
    id = db.Column(db.Integer, primary_key=True,autoincrement=False)
    report_no = db.Column(db.Integer, primary_key=True, autoincrement=False)
    parent_process_id = db.Column(db.Integer)
    process_id = db.Column(db.Integer)
    start_time = db.Column(db.String(100))

    reports = db.relationship('Report', backref='author', lazy=True)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    application_id = db.Column(db.Integer, db.ForeignKey('application.id'), nullable=False)

    def __repr__(self):
        return f'Process(id:{self.id}, parent_process_id:{self.parent_process_id}, process_id:{self.process_id}, user_id:{self.user_id}, application_id:{self.application_id})'

class Application(db.Model):
    __tablename__ = 'application'
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    pe_file_id = db.Column(db.Integer, db.ForeignKey('pe_file.id'))
    name = db.Column(db.String(100))
    vendor = db.Column(db.String(100))
    version = db.Column(db.String(100))

    processes = db.relationship('Process', backref='process', lazy=True)

    def __repr__(self):
        return f'Application(id:{self.id}, pe_fie_id={self.pe_file_id}, name={self.name}, vendor:{self.vendor}, version:{self.version})'

class Pe_file(db.Model):
    __tablename__ = 'pe_file'
    id = db.Column(db.Integer, primary_key=True,autoincrement=False)
    sha256 = db.Column(db.String(100))
    name = db.Column(db.String(100))
    path = db.Column(db.String(100))
    modified_time = db.Column(db.String(100))
    version = db.Column(db.String(100))

    applications = db.relationship('Application', backref='application', lazy=True)

    def __repr__(self):
        return f'Pe_file(id:{self.id}, name:{self.name}, path:{self.path}, version:{self.version})'


