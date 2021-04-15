from flask import Flask, render_template, request, flash, redirect
from fileapp.readData import ParseData
from fileapp.ViewData import returnDict, getUploads
from fileapp import app
import json



@app.route("/")
def main():

    #retrieve data to display previous uploads
    prevUploads = getUploads()
    if(len(prevUploads) == 0):
        return render_template('index.html')
    else:
        colnames = prevUploads[0].keys()
        return render_template('index.html', uploads=prevUploads, colnames=colnames)

@app.route("/upload", methods=['POST'])
def upload():
    file=request.files['inputFile']

    #parse data and send it to internal database
    outcome = ParseData(file)

    return redirect("localhost:5000/")

#To view data once it is uploaded from the home page. Displays nothing if database not yet created
@app.route("/reports/<rep_num>", methods=['GET'])
def display(rep_num):

    data = returnDict(1)

    if(len(data) == 0):
        return "No data to display"
    if(request.url[-5:] == '.json'):
        return {'data': data}
    else:
        colnames = data[0].keys()
        return render_template('display.html', records=data, colnames=colnames)

