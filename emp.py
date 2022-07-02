import csv
import io 
import boto3

client=boto3.resource("dynamodb")
table = client.Table("emp-table")

#Loading the data
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
    print(email)


