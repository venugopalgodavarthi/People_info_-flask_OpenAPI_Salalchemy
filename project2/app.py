import connexion
from hyper.ma import ma
from datetime import datetime
from hyper.db import db
from models.repositories import PeopleRepo
from models.entities import People
from flask import request, redirect, make_response
from flask import Flask, Response, render_template
from flask.templating import render_template
from flask import render_template
from fpdf import FPDF
import io
import csv

peoplerepo=PeopleRepo()
#Create the application instance
connex_app = connexion.App("__name__",specification_dir='./')
#read the swagger to configure the endpoints
connex_app.add_api('swagger.yml')

app = connex_app.app

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True



@app.before_first_request
def create_tables():
    db.create_all()

@app.route("/")
def home():
    """
    This function just responds to the browser URL
    localhost:5000/

    :return:        the rendered template "home.html"
    """
    return render_template("home.html")

@app.route('/add', methods=['GET',"POST"])
def profile():
    if request.method=='POST': 
        pid = request.form.get("pid")
        name = request.form.get("name")
        ptype = request.form.get("ptype")
        age = request.form.get("age")
        desc = request.form.get("desc")
        checked = request.form.get("checked")
        print(pid,name,ptype,age,desc,checked)
        if pid != '' and name != '' and ptype !='' and age != '' and desc != ''and checked != '':
            p = People(pid=pid,name=name,ptype=ptype,age=age,desc=desc,date=datetime.now(), check=True)
            peoplerepo.create(p)
            print("hai")
            return redirect('/')
        else:
            return redirect('/')
@app.route('/update/<int:pk>/', methods=['GET',"PUT",'POST'])
def update(pk):
    data = db.session.query(People).filter_by(pid=pk).first()
    if request.method=='POST': 
        pid = request.form.get("pid")
        name = request.form.get("name")
        ptype = request.form.get("ptype")
        age = request.form.get("age")
        desc = request.form.get("desc")
        checked = request.form.get("checked")
        print(pid,name,ptype,age,desc,checked)
        if pid != '' and name != '' and ptype !='' and age != '' and desc != ''and checked != '':
            p = People(pid=pid,name=name,ptype=ptype,age=age,desc=desc,date=datetime.now(), check=True)
            peoplerepo.update(p)
            return redirect('/')
        else:
            return redirect('/')
    else:
        return render_template('update.html', data=data)

@app.route('/delete/<int:pk>/', methods=['GET',"DELETE",'POST'])
def delete(pk):
    data = db.session.query(People).filter_by(pid=pk).first()
    return render_template('delete.html', data=data)


@app.route('/report/pdf', methods=['GET'])
def download_report():
    try:
        result = peoplerepo.fetchAll()
        output = io.StringIO()
        writer = csv.writer(output)
        line = ['People Id', 'People Name', 'People Type', 'People Age','People_Description','Date','People Check']
        writer.writerow(line)
        for row in result:
            line = [row.pid, row.name, row.ptype, row.age, row.desc, row.date, row.check]
            writer.writerow(line)
        output.seek(0)
        return Response(output, mimetype="text/csv", headers={"Content-Disposition":"attachment;filename=people_report.csv"})
    except Exception as e:
        print(e)


if __name__ == '__main__':
    db.init_app(app)
    ma.init_app(app)
    app.run(port=5000, debug=True)


    