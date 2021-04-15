#! /usr/bin/python

from fileapp.events_pb2 import *
import sys
from fileapp.schema import User, Process, Application, Pe_file, Report
from fileapp import app, db

#Custom insert definitions for the internal database

def insertReport(report_no):
    report = Report(id=1)
    db.session.add(report)
    db.session.commit()

def insertProcesses(processes, report_no):
    for p in processes:
        process = Process(id=p.id, report_no=report_no, parent_process_id=p.parent_process_id, process_id=p.process_id, start_time=p.start_time, user_id=p.user_id, application_id=p.application_id)
        db.session.add(process)
    db.session.commit()

def insertUsers(users):
    for u in users:
        user = User(id=u.id, security_identifier=u.security_identifier, username=u.username, domain=u.domain)
        db.session.add(user)
    db.session.commit()

def insertApplications(applications):
    for a in applications:
        application = Application(id=a.id, pe_file_id=a.pe_file_id, name=a.name, vendor=a.vendor, version=a.version)
        db.session.add(application)
    db.session.commit()

def insertPeFiles(pe_files):
    for pe in pe_files:
        pe_file = Pe_file(id=pe.id, sha256=pe.sha256, name=pe.name, path=pe.path, modified_time=pe.modified_time, version=pe.version)
        db.session.add(pe_file)
    db.session.commit()

#Get data from .bin file and insert it into the database
def ParseData(file):

    db.create_all()
    messages = Message()
    messages.ParseFromString(file.read())

    print("Parsing data from ", file.filename)

    #logic would be implemented for this if there were multiple uploads
    report_no = 1

    insertReport(report_no)
    insertProcesses(messages.processes, report_no)
    insertUsers(messages.users)
    insertApplications(messages.applications)
    insertPeFiles(messages.pe_files)

    return "Saved " + file.filename + " to the database"