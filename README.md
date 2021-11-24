# Company_Website_With_DB_BY_Flask&MySQL&Html

# Our project
* A web system must be developed - And in its database you can find information about the company's customers.<br/>
* MySQL-DataBase<br/>
* Web based Python-Flask<br/>
* Register Window<br/>
  * Create new users<br/>
  * Config complex password
  * Password save on DB with HMAC+Salt Function
  * Configure email for user
* Change Password Window
  * Current Password
  * New Password (adjust the System_Details.txt file)
* Login Window -Welcom to Comunication_LTD
  * User input
  * Password input
  * Check if user exist on DB 
* System Window
  * Input new customer
  * Display all customers
* Forgot Password Window
  * Email authentication- via random verfication key by SHA-1
  * Note: If you are internet connection is via proxy the email authentication will be failed !
* SQL Injection -Enable/disable login with SQL Injection
* System_Details.txt -Password management configuration file
  * Len password
  * Complex password
  * History
  * 100 common password
  * Count Failed Attempt Login
  * Note:Please modify the file and you details like email account and email password...
  


# Folder:
* DataBase-Export = My DataBase (two tables:hit_cyber_project_db_customer_details,hit_cyber_project_db_user_details)<br/>
* Static = CSS & JS Files<br/>
* templates = html files<br/>
# Files:
* 100_common_password.txt=All the 100 common weak password that our website not allowed to register with them .<br/>
* System_Details.txt =Include the password settings and their requirements & Include the login access to our system email & Include connections fields to our DB.<br/>
* app.py=This file contain all Functions/Class for the FE (Using with Flask Lib).<br/>
* Main.py=This File contain all Functions/Class for the BE.<br/>
* MySQL_Query.py =This File contain all Functions that connect and query a DB.<br/>
* Salt_HMAC_Function.py=This File contain all Functions that convert our plain text password to hasing password with HMAC.<br/>
# Python:
* Using Python 3.7
* Import the next lib:
  * flask
  * re
  * MySQL_Query
  * datetime
  * random
  * string
  * hashlib
  * smtplib
  * from email.mime.multipart import MIMEMultipart # pip install qick-mailer
  * from email.mime.text import MIMEText # This Module Support Gmail & Microsoft Accounts (hotmail, outlook etc..)
  * json
  * mysql.connector #pip install mysql-connector-python
  * binascii
