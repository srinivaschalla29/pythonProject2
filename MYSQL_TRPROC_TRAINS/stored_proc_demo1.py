from mysql.connector import Error
from hcl_datbase_connections import MysqlDatabaseConnection
class HclstoredProcedure(MysqlDatabaseConnection):
    def execute_str_procedur(self):
        try:
            self.cursor.callproc("get_cust")
            for r in self.cursor.stored_results():
                print(r.fetchall())
        except Exception as e:
            print(e)
        finally:
            if(self.connection.is_connected()):
                self.cursor.close()
                self.connection.close()
obj=HclstoredProcedure()
obj.connect("localhost","root","9849431709Sr@","srinu")
obj.execute_str_procedur()