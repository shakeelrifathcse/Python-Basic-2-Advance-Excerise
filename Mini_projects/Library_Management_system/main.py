books = ["atomic habits","wings","influence"]





class library():
    
    def __init__(self,books):
        self.books = books

    def list_books(self):
        print()
        print("Available books!")
        for i in self.books:
            print(i)

    def add_book(self,newbook):
        self.books.insert(0,newbook)
        print("New book added successfully")

    def borrow_book(self,needed_book):
        if needed_book in self.books:
            print("Available")
            self.books.remove(needed_book)
            print("Book borrowed successfully")
        else:
            print("Not Available")

    def returned_book(self,a):
        self.books.append(a)
        print("The returned book added successfully.")

    def delete_book(self,delete_book):
        if delete_book in self.books:
            print("you entered book is deleted...!")
            self.books.remove(delete_book)
        else :
            print("No books with such name")



    
obj = library(books)




msg = """\n
1. DISPLAY ALL BOOKS
2. ADD BOOKS
3. BORROW BOOK
4. RETURN BOOK
5. DELETE BOOK
6. EXIT
"""



while True:
    print(msg)
    choice = input("ENTER YOUR CHOICE: ")
    if choice == "1":
        obj.list_books()
    elif choice == "2":
        newbook = input("Add a book with its title name : ")
        obj.add_book(newbook)
    elif choice == "3" :
        needed_book = input("Which book you need? : ")
        obj.borrow_book(needed_book)
    elif choice == "4" :
        returning_book = input("Return book name : ")
        obj.returned_book(returning_book)
    elif choice == "5":
        deleted_book = input("Enter the book to delete : ")
        obj.delete_book(deleted_book)
    elif choice == "6":
        print("Thanks for using the system...!")
        quit()

    else:
        print("Enter the valid number mentioned...!")





