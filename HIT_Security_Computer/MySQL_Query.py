import mysql.connector #pip install mysql-connector-python
import json

def Show_Colums_From_DB():
    mysql_server_username, mysql_server_password, mysql_server_ip, mysql_database, mysql_port_connection, mysql_login_method = Get_MySQL_Login_Details()
    conn = mysql.connector.connect(user=mysql_server_username, password=mysql_server_password, host=mysql_server_ip,
                                   database=mysql_database, port=int(mysql_port_connection),
                                   auth_plugin=mysql_login_method)
    # Creating a cursor object using the cursor() method
    cursor = conn.cursor()
    # cursor.execute("select * from hit_cyber_project_db.user_details")
    cursor.execute("SHOW COLUMNS FROM hit_cyber_project_db.user_details")

    myresult = cursor.fetchall()
    for x in myresult:
        print(x)
    # Closing the connection
    conn.close
def Print_User_Details_Table():
        mysql_server_username, mysql_server_password, mysql_server_ip, mysql_database, mysql_port_connection, mysql_login_method = Get_MySQL_Login_Details()
        conn = mysql.connector.connect(user=mysql_server_username, password=mysql_server_password, host=mysql_server_ip,
                                   database=mysql_database, port=int(mysql_port_connection),
                                   auth_plugin=mysql_login_method)

    # Creating a cursor object using the cursor() method
        cursor = conn.cursor()
        cursor.execute("select * from hit_cyber_project_db.user_details")
        myresult = cursor.fetchall()
        for x in myresult:
            print(x)
        conn.close
def Print_User_Details_Table_on_specific_col(username):
    mysql_server_username, mysql_server_password, mysql_server_ip, mysql_database, mysql_port_connection, mysql_login_method = Get_MySQL_Login_Details()
    conn = mysql.connector.connect(user=mysql_server_username, password=mysql_server_password, host=mysql_server_ip,
                                   database=mysql_database, port=int(mysql_port_connection),auth_plugin=mysql_login_method)
    cursor = conn.cursor()
    cursor.execute("select * from hit_cyber_project_db.user_details where Username = " + "'"+str(username) + "'")
    myresult = cursor.fetchall()
    for x in myresult:
        print(x)
    conn.close
def Get_MySQL_Login_Details():
    with open('System_Details.txt') as f:
        system_details = json.load(f)
    mysql_server_username=system_details["Username_MySQL"]
    mysql_server_password =system_details["Password_MySQL"]
    mysql_server_ip =system_details["MySQL_Server_IP"]
    mysql_database=system_details["DB_Name"]
    mysql_port_connection=int(system_details["MySQL_Port"])
    mysql_login_method=system_details["auth_plugin"]
    return mysql_server_username,mysql_server_password,mysql_server_ip,mysql_database,mysql_port_connection,mysql_login_method

def Check_IF_ID_Exists(username):
    mysql_server_username,mysql_server_password,mysql_server_ip,mysql_database,mysql_port_connection,mysql_login_method=Get_MySQL_Login_Details()
    conn = mysql.connector.connect(user=mysql_server_username, password=mysql_server_password, host=mysql_server_ip, database=mysql_database, port=int(mysql_port_connection),auth_plugin=mysql_login_method)
    cursor = conn.cursor()
    cursor.execute('SELECT ID FROM hit_cyber_project_db.user_details WHERE Username = %(Username)s', { 'Username' : username })
    conn.close
    checkUsername = cursor.fetchone()
    if isinstance(checkUsername,tuple):
        return True #User is exist
    else:
        return False #User is not exist
#1
def Add_Row_To_Table(username,id,email,age,input_password_hash):
    mysql_server_username, mysql_server_password, mysql_server_ip, mysql_database, mysql_port_connection, mysql_login_method = Get_MySQL_Login_Details()
    conn = mysql.connector.connect(user=mysql_server_username, password=mysql_server_password, host=mysql_server_ip,database=mysql_database, port=int(mysql_port_connection),auth_plugin=mysql_login_method)


    if Check_IF_ID_Exists(username): # if the id (the user) is allready exists ob the DB return False
        return False
    # Creating a cursor object using the cursor() method
    cursor = conn.cursor()
    sql = "INSERT INTO hit_cyber_project_db.user_details (Username,ID,Email,Age,Current_Password) VALUES (%s, %s,%s,%s,%s)"
    val = (username,id,email,age, input_password_hash)
    cursor.execute(sql,val)
    conn.commit()
    conn.close
    return True
#2
def Pull_User_Password_From_User_Details_Table(username):
    mysql_server_username, mysql_server_password, mysql_server_ip, mysql_database, mysql_port_connection, mysql_login_method = Get_MySQL_Login_Details()
    conn = mysql.connector.connect(user=mysql_server_username, password=mysql_server_password, host=mysql_server_ip,
                                   database=mysql_database, port=int(mysql_port_connection),
                                   auth_plugin=mysql_login_method)
    cursor = conn.cursor()

    #Current_Password
    cursor.execute("select Current_password from hit_cyber_project_db.user_details where Username=" + "'"+str(username) + "'")
    myresult = cursor.fetchall() #the type that return is -> tuple in list
    current_password_hash=''.join(myresult[0])


    #Old_Password_1
    cursor.execute("select Old_Password_1 from hit_cyber_project_db.user_details where Username="+"'"+str(username) + "'")
    myresult = cursor.fetchall() #the type that return is -> tuple in list
    tuple_password_hash=myresult[0] #right now the type of the password is -> tuple
    if isinstance(tuple_password_hash, tuple):
        try:
         old_password_1_hash=''.join(tuple_password_hash)
        except:old_password_1_hash = None
    else:
        old_password_1_hash=None

    #Old_Password_2
    cursor.execute("select Old_Password_2 from hit_cyber_project_db.user_details where Username=""'"+str(username) + "'")
    myresult = cursor.fetchall() #the type that return is -> tuple in list
    tuple_password_hash=myresult[0] #right now the type of the password is -> tuple
    if isinstance(tuple_password_hash, tuple):
        try:
            old_password_2_hash=''.join(tuple_password_hash)
        except:
            old_password_2_hash = None
    else:
        old_password_2_hash = None

    #Old_Password_3
    cursor.execute("select Old_Password_3 from hit_cyber_project_db.user_details where Username=""'"+str(username) + "'")
    myresult = cursor.fetchall() #the type that return is -> tuple in list
    tuple_password_hash=myresult[0] #right now the type of the password is -> tuple
    if isinstance(tuple_password_hash, tuple):
        try:
            old_password_3_hash=''.join(tuple_password_hash)
        except:old_password_3_hash = None
    else:
        old_password_3_hash = None

    #Old_Password_4
    cursor.execute("select Old_Password_4 from hit_cyber_project_db.user_details where Username=""'"+str(username) + "'")
    myresult = cursor.fetchall()  # the type that return is -> tuple in list
    tuple_password_hash = myresult[0]  # right now the type of the password is -> tuple
    if isinstance(tuple_password_hash, tuple):
        try:
            old_password_4_hash =''.join(tuple_password_hash)
        except:
            old_password_4_hash = None
    else:
        old_password_4_hash = None

    #Old_Password_5
    cursor.execute("select Old_Password_5 from hit_cyber_project_db.user_details where Username="+"'"+str(username) + "'")
    myresult = cursor.fetchall()  # the type that return is -> tuple in list
    tuple_password_hash = myresult[0]  # right now the type of the password is -> tuple
    if isinstance(tuple_password_hash, tuple):
        try:
            old_password_5_hash =''.join(tuple_password_hash)
        except:
            old_password_5_hash = None
    else:
        old_password_5_hash = None

    #Old_Password_6
    cursor.execute("select Old_Password_6 from hit_cyber_project_db.user_details where Username="+ "'"+str(username) + "'")
    myresult = cursor.fetchall()  # the type that return is -> tuple in list
    tuple_password_hash = myresult[0]  # right now the type of the password is -> tuple
    if isinstance(tuple_password_hash, tuple):
        try:
            old_password_6_hash = ''.join(tuple_password_hash)
        except:
            old_password_6_hash = None
    else:
        old_password_6_hash = None

    #Old_Password_7
    cursor.execute("select Old_Password_7 from hit_cyber_project_db.user_details where Username="+ "'"+str(username) + "'")
    myresult = cursor.fetchall()  # the type that return is -> tuple in list
    tuple_password_hash = myresult[0]  # right now the type of the password is -> tuple
    if isinstance(tuple_password_hash, tuple):
        try:
            old_password_7_hash =''.join(tuple_password_hash)
        except:
            old_password_7_hash = None
    else:
        old_password_7_hash = None

    #Old_Password_8
    cursor.execute("select Old_Password_8 from hit_cyber_project_db.user_details where Username=" "'"+str(username) + "'")
    myresult = cursor.fetchall()  # the type that return is -> tuple in list
    tuple_password_hash = myresult[0]  # right now the type of the password is -> tuple
    if isinstance(tuple_password_hash, tuple):
        try:
            old_password_8_hash = ''.join(tuple_password_hash)
        except:
            old_password_8_hash = None
    else:
        old_password_8_hash = None


    #Old_Password_9
    cursor.execute("select Old_Password_9 from hit_cyber_project_db.user_details where Username=" + "'"+str(username) + "'")
    myresult = cursor.fetchall()  # the type that return is -> tuple in list
    tuple_password_hash = myresult[0]  # right now the type of the password is -> tuple
    if isinstance(tuple_password_hash, tuple):
        try:
            old_password_9_hash =''.join(tuple_password_hash)
        except:
            old_password_9_hash = None
    else:
        old_password_9_hash = None

    #Old_Password_10
    cursor.execute("select Old_Password_10 from hit_cyber_project_db.user_details where Username="+ "'"+str(username) + "'")
    myresult = cursor.fetchall()  # the type that return is -> tuple in list
    tuple_password_hash = myresult[0]  # right now the type of the password is -> tuple
    if isinstance(tuple_password_hash, tuple):
        try:
            old_password_10_hash =''.join(tuple_password_hash)
        except:
            old_password_10_hash = None
    else:
        old_password_10_hash = None

    conn.close
    return [current_password_hash,old_password_1_hash,old_password_2_hash,old_password_3_hash,old_password_4_hash,old_password_5_hash,
            old_password_6_hash,old_password_7_hash,old_password_8_hash,old_password_9_hash,old_password_10_hash]
#3
def Change_Password(new_input_password_hash,username):
    mysql_server_username, mysql_server_password, mysql_server_ip, mysql_database, mysql_port_connection, mysql_login_method = Get_MySQL_Login_Details()
    conn = mysql.connector.connect(user=mysql_server_username, password=mysql_server_password, host=mysql_server_ip,
                                   database=mysql_database, port=int(mysql_port_connection),
                                   auth_plugin=mysql_login_method)

    cursor = conn.cursor()
    cursor.execute("UPDATE hit_cyber_project_db.user_details set  Old_Password_10=Old_Password_9 where Username="+ "'"+str(username) + "'")
    cursor.execute("UPDATE hit_cyber_project_db.user_details set  Old_Password_9=Old_Password_8 where Username="+ "'"+str(username) + "'")
    cursor.execute("UPDATE hit_cyber_project_db.user_details set  Old_Password_8=Old_Password_7 where Username="+ "'"+str(username) + "'")
    cursor.execute("UPDATE hit_cyber_project_db.user_details set  Old_Password_7=Old_Password_6 where Username="+ "'"+str(username) + "'")
    cursor.execute("UPDATE hit_cyber_project_db.user_details set  Old_Password_6=Old_Password_5 where Username="+ "'"+str(username) + "'")
    cursor.execute("UPDATE hit_cyber_project_db.user_details set  Old_Password_5=Old_Password_4 where Username="+ "'"+str(username) + "'")
    cursor.execute("UPDATE hit_cyber_project_db.user_details set  Old_Password_4=Old_Password_3 where Username="+ "'"+str(username) + "'")
    cursor.execute("UPDATE hit_cyber_project_db.user_details set  Old_Password_3=Old_Password_2 where Username="+ "'"+str(username) + "'")
    cursor.execute("UPDATE hit_cyber_project_db.user_details set  Old_Password_2=Old_Password_1 where Username="+ "'"+str(username) + "'")
    cursor.execute("UPDATE hit_cyber_project_db.user_details set  Old_Password_1=Current_Password where Username="+ "'"+str(username) + "'")
    cursor.execute("""UPDATE hit_cyber_project_db.user_details SET Current_Password = %s Where Username = %s""",(new_input_password_hash, str(username)))
    conn.commit()
    conn.close
#4
def Check_IF_User_Lock(username):
    mysql_server_username, mysql_server_password, mysql_server_ip, mysql_database, mysql_port_connection, mysql_login_method = Get_MySQL_Login_Details()
    conn = mysql.connector.connect(user=mysql_server_username, password=mysql_server_password, host=mysql_server_ip,database=mysql_database, port=int(mysql_port_connection),auth_plugin=mysql_login_method)

    # Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    cursor.execute("select User_Lock_Until from hit_cyber_project_db.user_details where Username =" + "'"+str(username) + "'")
    myresult = cursor.fetchall()  # the type that return is -> tuple in list
    conn.close
    user_lock_until_time_tuple= myresult[0]  # right now the type of the password is -> tuple
    user_lock_until_time_list=list(user_lock_until_time_tuple) #convert list to tuple
    if user_lock_until_time_list[0]==None:
        return "User not lock"
    else:
        return user_lock_until_time_list[0]
#5
def Lock_User(username,lock_until):
    mysql_server_username, mysql_server_password, mysql_server_ip, mysql_database, mysql_port_connection, mysql_login_method = Get_MySQL_Login_Details()
    conn = mysql.connector.connect(user=mysql_server_username, password=mysql_server_password, host=mysql_server_ip,database=mysql_database, port=int(mysql_port_connection),auth_plugin=mysql_login_method)

    # Creating a cursor object using the cursor() method
    cursor = conn.cursor()
    cursor.execute("""UPDATE hit_cyber_project_db.user_details SET User_Lock_Until = %s Where Username = %s""",(lock_until, str(username)))
    conn.commit()
    conn.close
#6
def Release_Lock_User(username):
    mysql_server_username, mysql_server_password, mysql_server_ip, mysql_database, mysql_port_connection, mysql_login_method = Get_MySQL_Login_Details()
    conn = mysql.connector.connect(user=mysql_server_username, password=mysql_server_password, host=mysql_server_ip,database=mysql_database, port=int(mysql_port_connection),auth_plugin=mysql_login_method)

    # Creating a cursor object using the cursor() method
    cursor = conn.cursor()
    cursor.execute("UPDATE hit_cyber_project_db.user_details SET User_Lock_Until = NULL Where Username = "+"'" + str(username) + "'")
    conn.commit()
    conn.close
#7
def Attempt_Login_Failed_Count(username):
    mysql_server_username, mysql_server_password, mysql_server_ip, mysql_database, mysql_port_connection, mysql_login_method = Get_MySQL_Login_Details()
    conn = mysql.connector.connect(user=mysql_server_username, password=mysql_server_password, host=mysql_server_ip,database=mysql_database, port=int(mysql_port_connection),auth_plugin=mysql_login_method)

    # Creating a cursor object using the cursor() method
    cursor = conn.cursor()
    cursor.execute("select Attempt_Login_Failed_Count from hit_cyber_project_db.user_details where Username =" + "'" + str(username) + "'")
    myresult = cursor.fetchall()  # the type that return is -> tuple in list
    conn.close

    user_attempt_login_tuple = myresult[0]  # right now the type of the password is -> tuple
    user_attempt_login_list = list(user_attempt_login_tuple)  # convert list to tuple

    if user_attempt_login_list[0] == None:
        return 0
    else:
        return int(user_attempt_login_list[0])
#8
def Add_Count_To_Attempt_Login_Failed(username,count_number):
    mysql_server_username, mysql_server_password, mysql_server_ip, mysql_database, mysql_port_connection, mysql_login_method = Get_MySQL_Login_Details()
    conn = mysql.connector.connect(user=mysql_server_username, password=mysql_server_password, host=mysql_server_ip,database=mysql_database, port=int(mysql_port_connection),auth_plugin=mysql_login_method)

    # Creating a cursor object using the cursor() method
    cursor = conn.cursor()
    cursor.execute("""UPDATE hit_cyber_project_db.user_details SET Attempt_Login_Failed_Count = %s Where Username = %s""",(str(count_number), str(username)))
    conn.commit()
    conn.close
#9
def Get_Username_Email(username):
    mysql_server_username, mysql_server_password, mysql_server_ip, mysql_database, mysql_port_connection, mysql_login_method = Get_MySQL_Login_Details()
    conn = mysql.connector.connect(user=mysql_server_username, password=mysql_server_password, host=mysql_server_ip,
                                   database=mysql_database, port=int(mysql_port_connection),
                                   auth_plugin=mysql_login_method)

    # Creating a cursor object using the cursor() method
    cursor = conn.cursor()
    cursor.execute("select Email from hit_cyber_project_db.user_details where Username =" + "'" + str(username) + "'")
    myresult = cursor.fetchall()  # the type that return is -> tuple in list
    conn.close

    user_attempt_login_tuple = myresult[0]  # right now the type of the password is -> tuple
    user_attempt_login_list = list(user_attempt_login_tuple)  # convert list to tuple

    return (user_attempt_login_list[0])
#10
def Enable_Login_With_SQL_Injection(username,password):
    mysql_server_username, mysql_server_password, mysql_server_ip, mysql_database, mysql_port_connection, mysql_login_method = Get_MySQL_Login_Details()
    conn = mysql.connector.connect(user=mysql_server_username, password=mysql_server_password, host=mysql_server_ip,
                                   database=mysql_database, port=int(mysql_port_connection),
                                   auth_plugin=mysql_login_method)
    cursor = conn.cursor()

    # Current_Password
    #sql injection=          ' or 1=1 #
    cursor.execute("select * from hit_cyber_project_db.user_details where Username=" + "'"+str(username)+"'" +"AND Current_Password=" +"'"+password+"'")
    myresult = cursor.fetchall()  # the type that return is -> tuple in list
    if len(myresult)==0:
        return False
    else:return True
#11
def Add_New_Customer(name,country,city,phone):
    mysql_server_username, mysql_server_password, mysql_server_ip, mysql_database, mysql_port_connection, mysql_login_method = Get_MySQL_Login_Details()
    conn = mysql.connector.connect(user=mysql_server_username, password=mysql_server_password, host=mysql_server_ip,database=mysql_database, port=int(mysql_port_connection),auth_plugin=mysql_login_method)

    # Creating a cursor object using the cursor() method
    cursor = conn.cursor()
    sql = "INSERT INTO hit_cyber_project_db.customer_details (Name,Country,City,Phone) VALUES (%s,%s,%s,%s)"
    val = (name,country,city,phone)
    cursor.execute(sql,val)
    conn.commit()
    conn.close
    return True
#12
def Get_All_Customer():
    mysql_server_username, mysql_server_password, mysql_server_ip, mysql_database, mysql_port_connection, mysql_login_method = Get_MySQL_Login_Details()
    conn = mysql.connector.connect(user=mysql_server_username, password=mysql_server_password, host=mysql_server_ip,
                                   database=mysql_database, port=int(mysql_port_connection),
                                   auth_plugin=mysql_login_method)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM hit_cyber_project_db.customer_details')
    data = cursor.fetchall()
    return data


