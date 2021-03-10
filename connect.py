import psycopg2




# Create new DB sessioni and return connection object
connector = psycopg2.connect(dbname="DBNAME", 
                             user="USERNAME_TO_LOGIN_DB",
                             host="host of DB Server",
                             port="PORT_OF_DB_SERVER",
                             password="PASSWORD_OF_DB"
                             )


print('Connected to DB successful!')

query = "CREATE TABLE "