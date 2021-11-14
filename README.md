# Company_Website_With_DB_BY_Flask-MySQL-Html

# Our project
* A web system must be developed - And in its database you can find information about the company's customers.<br/>
* MySQL-DataBase<br/>
* Web based Python-Flask<br/>
* Register Window<br/>
  * Create new users<br/>
  * Config complex password
  * Password save on DB with HMAC+Salt Function
  * Configure email for user
* Forgot Password Window
* Login Window -Welcom to Comunication_LTD
  * User input
  * Password input
  * Check if user exist on DB 


# Folder:
* DataBase-Export = My DataBase (2 tables:hit_cyber_project_db_customer_details,hit_cyber_project_db_user_details)<br/>
* Staic = CSS & JS Files<br/>
* templates = html files<br/>
# Files:
* 100_common_password.txt=All the 100 common weak password that our website not allowed to register with them .<br/>
* System_Details.txt =Include the password settings and their requirements & Include the login access to our system email & Include connections fields to our DB.<br/>
* app.py=This file contain all Functions/Class for the FE (Using with Flask Lib).<br/>
* Main.py=This File contain all Functions/Class for the BE.<br/>
* MySQL_Query.py =This File contain all Functions that connect and query a DB.<br/>
* Salt_HMAC_Function.py=This File contain all Functions that convert our plain text password to hasing password with HMAC.<br/>
