from Salt_HMAC_Function import is_correct_password,hash_new_password
from MySQL_Query import *
import datetime
import random
import string
import hashlib
import smtplib
from email.mime.multipart import MIMEMultipart # pip install qick-mailer
from email.mime.text import MIMEText # This Module Support Gmail & Microsoft Accounts (hotmail, outlook etc..)
import json

class User_Registration():
    # default constructor
    def __init__(self,input_password,input_username,input_email,input_id,input_age):
        self._input_password=input_password
        self._input_username=input_username
        self._input_email = input_email
        self._input_id = input_id
        self._input_age = input_age
        with open('System_Details.txt') as f:
            system_details = json.load(f)
        self._min_pass_len=int(system_details["Password_Len"])
        self._complex_parameters =system_details["Complex_Password"]
        self._check_100_most_popular_password =system_details["Compare_Common_Password"]

    def User_Registration_Main(self):
        if self.Check_Password_Common() and  self.Check_Password_Len() and self.Check_Password_Parameters() and self.Create_User():
            return True # all the three function is good, the password not in the common pass and the parameters of the input password is good, and the user add to she DB and the len of the password is good
        else:
            return False

    def Check_Password_Common(self):

            if self._check_100_most_popular_password:
                with open("100_common_password.txt") as file:
                    lines = file.readlines()
                    lines = [line.rstrip() for line in lines]
                for line in lines:
                    if line == self._input_password:
                        print("class:User_Registration--Function:Check_Password_Common--The input password: {0} is on the 100_common_password,we dont accept your are password".format(self._input_password))
                        return False
                return True
            else:
                return True

    def Check_Password_Len(self):
         if len(self._input_password) >=self._min_pass_len:
             return True
         else:
             print("class:User_Registration--Function:Check_Password_Len--The input password len is :{0} , You need enter at lest len of {1}".format(len(self._input_password),(self._min_pass_len)))
             return False

    def Check_Password_Parameters(self):

        symbol = ['!', '@', '#', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=']

        if self._complex_parameters:
            count=0
            if any (char.isdigit() for char in self._input_password):
                count=count+1
            if any (char.isupper() for char in self._input_password):
                count=count+1
            if any (char.islower() for char in self._input_password):
                count=count+1
            for char in self._input_password:
                if char in symbol:
                    count = count + 1
                    break

            if count <3:
                print("class:User_Registration--Function:Check_Password_Parameters--The input password: {0} is must include 3 of the next 4 parameters :digit,upper_letter,lower_letter,special_symbol.----- You are password only include : {1} parameters".format(self._input_password,count))

                return False
            else:
                return True
        else:
            return True

    def Create_User(self):

        self._input_password_hash=hash_new_password(self._input_password) #convert the plain text to utf8/binary format (hasing)
        add_user=Add_Row_To_Table(username=self._input_username,id=self._input_id,email=self._input_email,age=self._input_age,input_password_hash=self._input_password_hash) #return true or false
        if add_user==False:
            print("class:User_Registration--Function:Create_User--The input username: {0} is already exist on our DB, please choose different username".format(self._input_username))
        return add_user

class Login():
    def __init__(self, input_password,input_username):
        self._input_password = input_password
        self._input_username= input_username
        with open('System_Details.txt') as f:
            system_details = json.load(f)
        self._reattempt=int(system_details["Reattempt"])

    def Check_If_User_Exists_in_DB(self):
        if Check_IF_ID_Exists(self._input_username):
            return True
        else:
            print("class:login--Function:User_Login--The input username {0} does not match to any username from the DB".format(self._input_username))
            return False

    def Check_IF_User_Lock_in_DB(self):
        check_user=Check_IF_User_Lock(username=self._input_username)
        if check_user == "User not lock":
            return True

        current_date_and_time = datetime.datetime.now()
        check_user_lock_until = datetime.datetime.strptime(check_user, '%Y-%m-%d %H:%M:%S.%f')
        delta = (current_date_and_time - check_user_lock_until)
        if delta > datetime.timedelta(minutes=1):
            Release_Lock_User(self._input_username)
            return True
        else:
            print("class:login--Function:Check_IF_User_Lock_in_DB--The input username {0} is lock you need to wait until 30 min will be pass".format(self._input_username))
            return False

    def User_Login(self):
        if self.Check_If_User_Exists_in_DB() and self.Check_IF_User_Lock_in_DB():
            user_password_from_db=Pull_User_Password_From_User_Details_Table(self._input_username)[0]
            if (is_correct_password(user_password_from_db,self._input_password)):
                    Add_Count_To_Attempt_Login_Failed(username=self._input_username, count_number=0)
                    return True
            else:
                    print("class:login--Function:User_Login--The input password {0} does not match to the password from the DB".format(self._input_password))
                    print("After 3 Times fail to login the User will be lock for 30 min")
                    count=int(Attempt_Login_Failed_Count(username=self._input_username)) #pull the current count times of failed login
                    Add_Count_To_Attempt_Login_Failed(username=self._input_username, count_number=count+1) # update the db and change the add +1 to the count of failed login attempt
                    if int(Attempt_Login_Failed_Count(self._input_username)) == self._reattempt:
                        current_date_and_time = datetime.datetime.now()
                        minutes = 29
                        minutes_added = datetime.timedelta(minutes=minutes)
                        future_date_and_time = current_date_and_time + minutes_added
                        Lock_User(username=self._input_username, lock_until=future_date_and_time)
                        print("class:login--Function:User_Login--The username: {0} will be lock for the next 30 min ".format(self._input_username))
                        Add_Count_To_Attempt_Login_Failed(username=self._input_username, count_number=0)

                    return False
        else:
            return False

class Forget_Password():
    # default constructor
    def __init__(self,input_username):
        self._input_username = input_username
        with open('System_Details.txt') as f:
            system_details = json.load(f)
        self.email_source =system_details["Email_Name"]
        self.email_source_password=system_details["Email_Password"]

    def Check_If_User_Exists_in_DB(self):
        if Check_IF_ID_Exists(username=self._input_username):return True
        else:
            print("class:login--Function:User_Login--The input username {0} does not match to any username from the DB".format(self._input_username))
            return False

    def Send_Email_With_Random_Password(self):
        #self._random_password = ''.join(random.choice(string.ascii_lowercase) for i in range(8))
        h= hashlib.sha1(''.join(random.choice(string.ascii_lowercase) for i in range(8)).encode('utf-8'))
        self._random_password=h.hexdigest()
        mail_content = "Hello we get request from your username.\nFor changing the password.We demand 2FA.\nPlsease Enter the next passwrod:\n" + self._random_password
        sender_address = self.email_source
        sender_pass = self.email_source_password
        self._receiver_address = Get_Username_Email(username=self._input_username)
        # Setup the MIME
        message = MIMEMultipart()
        message['From'] = sender_address
        message['To'] = self._receiver_address
        message['Subject'] = 'HIT-Cyber-Project-Change-Password'  # The subject line
        # The body and the attachments for the mail
        message.attach(MIMEText(mail_content, 'plain'))
        # Create SMTP session for sending the mail
        session = smtplib.SMTP('smtp.gmail.com', 587)  # use gmail with port
        session.starttls()  # enable security
        session.login(sender_address, sender_pass)  # login with mail_id and password
        text = message.as_string()
        session.sendmail(sender_address, self._receiver_address, text)
        session.quit()
        return self._random_password,self._receiver_address

class Change_Password_Current_User():
    # default constructor
    def __init__(self, input_username,input_password):
        self._input_username = input_username
        self._input_password = input_password
        with open('System_Details.txt') as f:
            system_details = json.load(f)
        self._check_history = int(system_details["History"])
        self._min_pass_len = int(system_details["Password_Len"])
        self._complex_parameters = system_details["Complex_Password"]
        self._check_100_most_popular_password = system_details["Compare_Common_Password"]

    def Check_Password_History_Using(self):
        all_user_current_password=Pull_User_Password_From_User_Details_Table(username=self._input_username)
        for _password in all_user_current_password:
            if _password==None:
                continue
            if is_correct_password(stored_password=_password,provided_password=self._input_password):
                print("class:Change_Password_Current_User--Function:Check_Password_History_Using--The input password len is :{0} allready one of the last 10 password ".format((self._input_password)))
                return False
        return True

    def Check_Password_Common(self):

            if self._check_100_most_popular_password:
                with open("100_common_password.txt") as file:
                    lines = file.readlines()
                    lines = [line.rstrip() for line in lines]
                for line in lines:
                    if line == self._input_password:
                        print("class:Change_Password_Current_User--Function:Check_Password_Common--The input password: {0} is on the 100_common_password,we dont accept your are password".format(self._input_password))
                        return False
                return True
            else:
                return True

    def Check_Password_Len(self):
         if len(self._input_password) >=self._min_pass_len:
             return True
         else:
             print("class:Change_Password_Current_User--Function:Check_Password_Len--The input password len is :{0} , You need enter at lest len of {1}".format(len(self._input_password),(self._min_pass_len)))
             return False

    def Check_Password_Parameters(self):

        symbol = ['!', '@', '#', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=']
        if self._complex_parameters:
            count=0
            if any (char.isdigit() for char in self._input_password):
                count=count+1
            if any (char.isupper() for char in self._input_password):
                count=count+1
            if any (char.islower() for char in self._input_password):
                count=count+1
            for char in self._input_password:
                if char in symbol:
                    count = count + 1
                    break

            if count <3:
                print("class:Change_Password_Current_User--Function:Check_Password_Parameters--The input password: {0} is must include 3 of the next 4 parameters :digit,upper_letter,lower_letter,special_symbol.----- You are password only include : {1} parameters".format(self._input_password,count))

                return False
            else:
                return True
        else:
            return True

    def Main(self):
        if self.Check_Password_History_Using() and self.Check_Password_Common() and self.Check_Password_Len() and self.Check_Password_Parameters():
            Change_Password(new_input_password_hash=hash_new_password(self._input_password),username=self._input_username)
            return True
        else:
            return False




