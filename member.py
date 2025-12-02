from db import get_connection
class member:
    def __init__(self):
        self.conn=get_connection()
        self.cursor=self.conn.cursor()
    def add_member(self,name):
        '''
        get the last id numbe from the members db
        '''
        self.cursor.execute("select max(id) from members")
        current_id=self.cursor.fetchone()[0]

        self.cursor.execute("insert into members(id,name) values(?,?)",(current_id+1,name,))
        self.conn.commit()
    

    