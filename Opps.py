import mysql.connector
import logging

# Set up logging
logger = logging.getLogger(__name__)

class MySqlConnection:
    def __init__(self, config):
        # Initialize with config and a placeholder for the connection
        self.config = config
        self.connection = None

    def connect(self):
        try:
            # Create the connection using the passed config
            self.connection = mysql.connector.connect(**self.config)
            if self.connection.is_connected():
                logger.info("Connection Successful to MySQL")
        except Exception as e:
            logger.error(f"Error occurred during connection: {e}")
            raise e

    def close(self):
        # Method to safely close the connection
        if self.connection and self.connection.is_connected():
            self.connection.close()
            logger.info("MySQL Connection Closed")

class MySqlCrudOperation:
    def __init__(self, connection):
        # This class takes an existing connection object
        self.connection = connection

    def read_from_mysql(self, query):
        cursor = None
        try:
            # Create a cursor from the connection passed via self
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Exception as e:
            logger.error(f"Error occurred in MySQL query run: {e}")
        finally:
            if cursor:
                cursor.close()
                logger.info("Cursor Closed")
