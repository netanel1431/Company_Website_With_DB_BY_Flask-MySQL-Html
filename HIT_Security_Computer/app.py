from flask import Flask, render_template, request,session,redirect
import re
from Main import *

app = Flask(__name__)
app.config['FONTAWESOME_STYLES'] = ['brands']

@app.route("/")
def homepage():
        return render_template('1_Homepage.html', message=None)

@app.route("/Login_Window", methods=['GET', 'POST'])
def Login_Window():
    if request.method == 'POST':
        if request.form['logInBtn'] == "Log In":
            data={
            "username":request.form.get('username'),
            "password":request.form.get('password'),
            }

            if request.form.get("loginwithsqlinjection") == "loginwithsqlinjection":
                if Enable_Login_With_SQL_Injection(username=data["username"],password=hash_new_password(data["password"])):
                    return render_template('1_1_Successful_Login.html')
                else:
                    return render_template('1_2_Failed_Login.html', message=[data["username"], data["password"]])


            user_login=Login(input_password=data["password"],input_username=data["username"])
            if user_login.User_Login() :
                return render_template('1_1_Successful_Login.html')
            else:
                return render_template('1_2_Failed_Login.html',message=[data["username"],data["password"]])


        elif request.form['logInBtn'] == "Create New Account":
            return render_template('2_Create_New_Account.html')

        elif request.form['logInBtn'] == "Change Current Password":
            return render_template('5_Change_Current_Password.html')


        elif request.form['logInBtn'] == "Forget Password":
            return render_template('3_Forgot_Password.html')

@app.route("/Create_Account_Window", methods=['GET', 'POST'])
def Create_Account_Window():
    if request.method == 'POST':
        if request.form['createAccount'] == "Create Account":
            data={
            "username":request.form.get('username'),
            "password":request.form.get('password'),
            "email": request.form.get('email'),
            "id": request.form.get('id'),
            "age": request.form.get('age'),
            }

            if  data["email"].isnumeric():
                return render_template('2_1_Failed_Create_Account.html', message=[data["email"], data["id"],data["age"],data["password"],data["username"]])

            regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'  # Make a regular expression-for validating an Email
            if not (re.fullmatch(regex, data["email"])):
                return render_template('2_1_Failed_Create_Account.html', message=[data["email"], data["id"],data["age"],data["password"],data["username"]])

            if not data["id"].isnumeric():
                return render_template('2_1_Failed_Create_Account.html', message=[data["email"], data["id"],data["age"],data["password"],data["username"]])

            if not data["age"].isnumeric():
                return render_template('2_1_Failed_Create_Account.html',  message=[data["email"], data["id"],data["age"],data["password"],data["username"]])


            create_account=User_Registration(input_password=data["password"],input_username=data["username"],input_email=data["email"],input_id=data["id"],input_age=data["age"])
            if create_account.User_Registration_Main():
                return render_template('2_2_Successful_Create_New_Account.html')
            else:
                return render_template('2_1_Failed_Create_Account.html',  message=[data["email"], data["id"],data["age"],data["password"],data["username"]])

@app.route("/Forgot_Password", methods=['GET', 'POST'])
def Forgot_Password():
    if request.method == 'POST':
        if request.form['Forgot_Password'] == "Send Verification Code":
            data={"username": request.form.get('username')}
            forgot_password=Forget_Password(input_username=data["username"])

            if not forgot_password.Check_If_User_Exists_in_DB():
                return render_template('3_1_Failed_Forgot_Password.html',message=data["username"])

            random_password,receiver_address=forgot_password.Send_Email_With_Random_Password()
            session['random_password'] = random_password
            session['username'] = data["username"]

            return render_template('3_2_Check_Verification_Code.html', message=receiver_address)

@app.route("/Check_Verification_Code", methods=['GET', 'POST'])
def Check_Verification_Code():
    if request.method == 'POST':
        if request.form['Check_Code'] == "Check code":
            if session.get('random_password', None) ==request.form.get('random_code'):

                return render_template('3_3_Update_Password.html',message=session.get('username', None))
            else:
                return render_template('3_4_Incorrect_Verficication_Code.html')

@app.route("/Update_Password", methods=['GET', 'POST'])
def Update_Password():
    if request.method == 'POST':
        if request.form['Update_Password'] == "Update Password":
            new_password=request.form.get('newPassword')
            change_password=Change_Password_Current_User(input_username=session.get('username', None), input_password=new_password)
            if change_password.Main():
                return render_template('3_6_Successful_Change_Password.html')
            else:
                return render_template('3_5_Failed_Change_Password.html',message=new_password)

@app.route("/Add_Customer", methods=['GET', 'POST'])
def Add_Customer():
    if request.method == 'POST':
        if request.form['Add_Customer'] == "Add Customer":
            data = {
                "username": request.form.get('username'),
                "phone": request.form.get('phone'),
                "city": request.form.get('city'),
                "country": request.form.get('country')
            }
            Add_New_Customer(name=data["username"],country=data["country"],city=data["city"],phone=data["phone"])
            return render_template('1_1_Successful_Login.html')

@app.route("/Display_Customer", methods=['GET', 'POST'])
def Display_Customer():
    if request.method == 'POST':
        if request.form['Display_Customer'] == "Display customer":
            data=Get_All_Customer()
            return render_template('4_Display_All_Customers.html', data=data)




@app.route("/Change_Current_Password", methods=['GET', 'POST'])
def Change_Current_Password():
    if request.method == 'POST':
        if request.form['Change_Password'] == "Change Password":
            new_password=request.form.get('newPassword')
            username = request.form.get('username')
            currentPassword = request.form.get('currentPassword')
            user_password_from_db = Pull_User_Password_From_User_Details_Table(username)[0]
            if (is_correct_password(user_password_from_db,currentPassword)):change_password=Change_Password_Current_User(input_username=username, input_password=new_password)
            else:return render_template('3_5_Failed_Change_Password.html',message=new_password)

            if change_password.Main():return render_template('3_6_Successful_Change_Password.html')
            else:return render_template('3_5_Failed_Change_Password.html',message=new_password)


@app.route('/Go_Back_To_Homepage')
def Go_Back_To_Homepage():
    return render_template('1_Homepage.html')

if __name__=="__main__":
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(debug=False,host="127.0.0.1",port=300)

