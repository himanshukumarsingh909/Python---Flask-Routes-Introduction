
from ast import For
import colorama 
from colorama import Back,Fore,Style


from flask import Flask,jsonify,request ,url_for,redirect,session,render_template
colorama.init()




app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = "Thisisasecret!"



@app.route('/')
def index():
    print(Back.GREEN + "Inside the Index Function")
    return '<h1>Hello world!</h2>'


@app.route('/printdata')
def printData():
    print("Singh is king")
    dict1 = { 
        'name': "Himanshu Kumar Singh",
        'batch': "Singh is king"
    }
    
    return dict1

#Add default Route
@app.route('/home',methods=['Post','GET'],defaults={'name':'Homosapaien'})
@app.route('/home/<string:name>',methods=['POST','GET'])
def home(name):
    session['name'] = name
    return render_template('home.html',name1=name,display=False)

@app.route('/json')
def json():
    name = session['name']
    return jsonify({'name':name,'key2':[1,2,3,4,5,6,7,8]})


# Now working with query String 
@app.route('/query',methods=['GET'])
def query():
    name = request.args.get('name')
    location = request.args.get('location')
    return "Hi {},you are from {}. You are on query page".format(name,location)


# Handling submit form 
@app.route('/theform' ,methods=['GET','POST'])
def theform():
    if request.method == 'GET':

        return render_template('form.html')
    else:
        name = request.form['name']
        location = request.form['location']
        # return "The form is sumbitted successfully. Hello {} ,you are from {}. Hahahaha".format(name,location)
        
        print(Fore.GREEN + "Entered Name : {}".format(name))
        print(Fore.BLUE + "Entered location : {}".format(location))
        print("hello World")

        return redirect(url_for('home',name=name))


# This route can only be accessed after submiting the FORM.
# @app.route("/process",methods=['Post'])
# def process():
#     name = request.form['name']
#     location = request.form['location']
    
#     return "The form is sumbitted successfully. Hello {} ,you are from {}. Hahahaha".format(name,location)


# Route for processing json
@app.route('/processjson',methods=['POST'])
def processjson():
    data = request.get_json()
    print(Fore.BLUE+ str(data))

    name = data['name']
    location = data['location']
    return jsonify({'result':'Success!!!','Submited Name':name,'Submitted Location':location})



if __name__ == "__main__":
    app.run()

