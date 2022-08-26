from crypt import methods
from flask import Flask,jsonify,request

app=Flask(__name__)

contacts=[
    {
    'id':1,
    'name':'Karl',
    'contact':9398478133,
    'done':False
},
{
'id':2,
'name':'Joseph',
'contact':9834773423,
'done':False
}
]

@app.route('/add-data',methods=['POST']) 

def add_task():
    if not request.json:
        return jsonify({
        'status':"error",
        'message':'please enter the data'
        },400)

    contact={
    'id':contacts[-1]['id']+1,
    'name':request.json('Name'),
    'contact':request.json.get('Contact',""),
    'done':False
    }
    contacts.append(contact)
    return jsonify({ 
        'status':'complete',
        'message':'contact added successfully'  
    })

if(__name__=='__main__'):
    app.run(debug=True)    