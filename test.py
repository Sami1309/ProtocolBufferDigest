from fileapp import app, db
from fileapp.events_pb2 import *
import sys
from fileapp.schema import User, Process, Application, Pe_file
from fileapp.readData import insertApplications, insertPeFiles, insertProcesses, insertUsers
from fileapp.ViewData import returnDict
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json



def close_session(session=None):
    db.session.commit()

#Make sure no errors pop up when requesting the data view
def view_data_test():

    returnDict(1)

#Tests the data parsing mechanisms of the application
def parse_data_test():

    f = open("testfiles/events.bin", "rb")
    db.create_all()
    messages = Message()
    messages.ParseFromString(f.read())

    print("Parsing data from file")

    insertProcesses(messages.processes, 1)
    insertUsers(messages.users)
    insertApplications(messages.applications)
    insertPeFiles(messages.pe_files)

    processes = Process.query.all()
    assert(len(processes)==216)
    users = User.query.all()
    assert(len(users) == 8)
    applications = Application.query.all()
    assert(len(applications)==38)
    pe_files = Pe_file.query.all()
    assert(len(pe_files) == 69)
    
    view_data_test()

    close_session()

    os.remove("fileapp/database/test.db")

    print("Parse data test succesful")


def run_tests():
    parse_data_test()


if __name__ == "__main__":
    run_tests()