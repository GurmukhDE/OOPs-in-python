config = configparser.ConfigParser()
config.read(
    r"C:\Users\manish\Documents\python_programming\src\resources\config_file.ini"
)

config.set(
    "mysql_database",
    "password",
    decrypt(config["mysql_database"]["password"])
)

mysql_db_conn_obj = MySQLConnection(config)
mysql_db_conn_obj.connect()

crud = MySQLCRUDOperation(mysql_db_conn_obj.connection)

manish_obj = Labour("manish", "kumar", 500)
manish_obj.save_to_database(crud)

print(manish_obj._Labour__wage)

# print(manish_obj._last)

ramesh_obj = Labour("Rajesh", "Singh", 400)

# print(Labour.total_count)
# first_name, last_name, wage
