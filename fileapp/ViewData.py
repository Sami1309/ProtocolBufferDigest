from fileapp.schema import User, Process, Application, Pe_file, Report
from fileapp import app, db
import json

def getUploads():
    data = ""
    try:
        data = Report.query.all()
    except:
        print("Table does not exist")
    returnList = []
    for d in data:
        returnDict = {}
        returnDict['Report Number'] = d.id
        returnDict['Upload Time'] = d.created_date
        returnList.append(returnDict)
    return returnList

        
#Get a digest of the joined database information and return it as a list
def returnDict(rep_num):

    #rep_num corresponds to the report version we want to query
    
    #Data columns is the column format for the returned list
    data_columns = ["Name", "PID", "Parent PID", "Start Time", "User", "Path", "Version"]

    data = Report.query\
        .filter_by(id = rep_num)\
        .join(Process, Report.id == Process.report_no)\
        .join(User)\
        .join(Application)\
        .join(Pe_file, Application.pe_file_id == Pe_file.id)\
        .add_columns(Application.name, Process.process_id, Process.parent_process_id, Process.start_time, User.username, Pe_file.path, Application.version)\
        .all()
    
    #Extract only the data values that correspond to data_columns
    returnList = []
    for d in data:
        returnDict = {}
        valuables = d[1:]
        for i, v in enumerate(valuables):
            returnDict[data_columns[i]] = v
        returnList.append(returnDict)

    return returnList

