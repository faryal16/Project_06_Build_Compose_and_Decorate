# 11. Class Methods Assignment:
# Create a class Book with a class variable total_books. 
# Add a class method increment_book_count() to increase the count when a new book is added.

def run():
    class Book():
        
        total_books = 0
        
        def __init__(self):
            Book.total_books += 1
            print(f"\n📔 Book \033[1;3;34m{Book.total_books}\033[0m added.")
            
        @classmethod
        def increment_book_count(cls):
            print(f"\n📚 You added Total \033[1;3;35m{cls.total_books}\033[0m books in list📃.")
            
    # create object
    book1 = Book()
    book2 = Book()
    book3 = Book()
    book4 = Book()


    # class method called
    Book.increment_book_count()



# call the main function
if __name__ == "__main__":
    run() 
        
    
        
        