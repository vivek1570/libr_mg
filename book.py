from db import get_connection


class Book:
    def __init__(self):
        self.conn = get_connection()
        self.cursor = self.conn.cursor()

    def add_book(self,title,author,year):
        '''
        title,author,year these data need to add a book
        so need to pass these all data
        '''
        # conn=sqlite3.connect("library.db")
        # cursor=conn.cursor()

        '''
        we need to know whether the book is currently exsting in there or not
        check the book with same name exsting in the db
        if throw and error
        take the last book number from the db

        '''
        self.cursor.execute("select * from books where title=?",(title,))

        result=self.cursor.fetchone()
        if result:
            raise ValueError("Book already exists!")
        else:
            '''
            take the highest value of the current book number
            if the id is null then we need to take care of that one also
            '''
            self.cursor.execute("select max(id) from books")
            max_id=self.cursor.fetchone()[0]
            if max_id is None:
                max_id=99
            max_id=max_id+1
            self.cursor.execute("insert into books(id,title,author,year,available) values(?,?,?,?,?)",
                           (max_id,title,author,year,1))
            self.conn.commit()
    def view_books(self):
        self.cursor.execute("select * from books")
        books=self.cursor.fetchall()
        for book in books:
            print(book)
        
    
    def update_book(self,id):
        '''
        first check the id is exsting or not?
        this mainly for updating the statud of the book
        '''
        self.cursor.execute("select title,author,year,available from books where id=?",(id,))
        book=self.cursor.fetchone()
        if not book:
            print("book not found")
            return
        old_title,old_author,old_year,=book

        new_title=input(f"Enter new title ({old_title}): ") or old_title
        new_author=input(f"Enter new authot ({old_author}): ") or old_author
        new_year=input(f"Enter new yer ({old_year}): ") or old_year

        
        self.cursor.execute("insert into books(id,title,author,year,available) values(?,?,?,?,?)",
                           (id,new_title,new_author,new_year,1))
        self.conn.commit()
        print("the book {id} updated successfully")
    def delete_book(self,id):
        self.cursor.execute("select title,author,year,available from books where id=?",(id,))
        book=self.cursor.fetchone()
        if not book:
            print("book not found")
            return
        self.cursor.execute("delete form books where id=?",(id,))
        self.conn.commit()
    
    def add_transaction(self,member_id,book_id,issue_date,return_date):
        "here we assume that no conflict occured means"
        "we need to take care of the book is aldready present"

        self.cursor.execute("insert into issued_books(member_id,book_id,issue_date,return_date) values(?,?,?,?)",
                            (member_id,book_id,issue_date,return_date))
        self.conn.commit()


        





        
                



            


