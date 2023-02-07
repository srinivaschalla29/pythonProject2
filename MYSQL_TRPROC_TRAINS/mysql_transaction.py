from mysql.connector import Error
from hcl_datbase_connections import MysqlDatabaseConnection
class HclPythonTransaction(MysqlDatabaseConnection):
    def execute_transaction_query(self):
        custid=2
        sql="delete from customer where cust_id=%s"
        try:
            self.cursur.execute(sql,(custid,))
            self.connection.commit()
        except:
            self.connection.rollback()
            print("something is goes wrong")
        finally:
            if(self.connection.is_connected()):
                self.cursur.close()
                self.connection.close()
obj=HclPythonTransaction()
obj.connect("localhost","root","9849431709Sr@","srinu")
obj.execute_transaction_query()