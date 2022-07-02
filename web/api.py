#Api for DynaamoDB loading

import io
import boto3

from flask import Flask, request

client=boto3.resource("dynamodb")
table = client.Table("emp-table2")

app = Flask(__name__)
@app.route("/")
def hello_world():
    return "<p> Hello, World!</p>"

#Create api endpoint
@app.route("/create")
def create():
    with io.open("emp.csv","r",encoding="utf-8")as f1:
        data=f1.read()
        f1.close()

    #Splitting the data
    data=data.split("\n")[1:]
    for line in data:
        name=line.split(",")[0]
        phone=line.split(",")[1]
        email=line.split(",")[2]
        country=line.split(",")[3]

        response = table.put_item(
            Item={
                'name': name,
                'email': email,
                'phone': phone,
                'country':country}
                )
    return "<p> Created!</p>"
#Update api endpoint
@app.route("/update")
def update():
    email = request.args["email"]
    city = request.args["city"]
    table.update_item(Key={"email":email},
                       UpdateExpression="SET city=:new",
                        ExpressionAttributeValues={":new":city},
                        ReturnValues='UPDATED_NEW'
                        )
    return "<p> Updated!</p>"

#Read api endpoint
@app.route("/read")
def read():
    email = request.args["email"]
    response = table.get_item(
        Key={"email":email}
        )
    return response["Item"]

#Delete api endpoint
@app.route("/delete")
def delete():
    email = request.args["email"]
    response = table.delete_item(
        Key={"email":email}
        )
    return response
app.run()


