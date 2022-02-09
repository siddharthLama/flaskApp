from flask import Flask,jsonify,request, request_started
app =Flask(__name__)
tasks =[
    {
       "id": 1,
       "title" : u"contacts", 
       "dicription" : u"9876543210,9638796543,9876543215,837394279,7797392912",
       "done" :False

    }

]
@app.route('/')
def HelloWorld():
    return "Hello World"
@app.route('/get-data')
def getTask():
    return jsonify({
        "data" : tasks

    })

@app.route('/add-data',methods =["POST"] )
def addTask():
    if not request.json :
        return jsonify({
           "status" : "ERROR",
           "message" : " Pls Provide The Data"

        }),400
    contact = {
        "id":tasks[-1]["id"]+1,
        "Name" : request.json["Name"],
        "Contact" : request.json["Contact",""],
       "done" : False
     
    }
    tasks.append(contact)
    return jsonify({
        "status" :"Sucess",
        "message": "Contact Added Sucessfully"
    })
if __name__ == '__main__':
    app.run(debug=True)
