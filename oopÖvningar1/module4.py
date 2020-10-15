#4. Biblioteket
#Vi ska skapa ett bibliotekssystem. För att hantera utlåningar. Tänk er att vi har ett library. Som har
#ett antal books
#1. Skapa en klass Library
#Denna kanske behöver en lista med böcker
#En funktion för att AddBookToLibrary
#(kolla om titel redan finns. Isåfall plussa på antal för den! - annars skapa ny)
#En funktion för att BorrowBook
#En funktion för att ReturnBook
#2. Skapa en klass Book
#Funktioner kanske
#Borrow – låna ut om den finns inne
#GetCountInLibrary – hur många ex som finns inne
#GetBorrowedCount – hur många ex som är utlånade
#Title
#TotalCount
#BorrowedCount
#3. Skapa en MENY som
#a. Skapa ny bok
#b. Lånar ut bok (på titel)
#c. Lämnar tillbaka bok (på titel)

class Library:
    def __init__ (self):
        self._books=[]

    def addBook(self,book):
        for i in self._books:
            if book.getTitle()==i.getTitle():
                i.addMoreCount(book.getTotalCount)
        else:
            self._books.append(book)

    def loanOutBook(self,book):
        for i in self._books:
            if book==i.getTitle():
                if i.getCountinLibrary()>0:
                    print ("Enjoy the book!")
                    i.borrowBook()
                else:
                    print("not enough book available")
            else:
                print("Book is not there in the Library")

    def returnBook(self,book):
        for i in self._books:
            if book==i.getTitle():
                i.returnBook()
                print("Book is successfully returned")
           
class Book:
    def __init__(self, Title, Count):
        self._Title=Title
        self._Count=Count
        self._borrowedCount=0

    def getTitle(self):
        return self._Title

    def getTotalCount(self):
        return self._Count

    def getBorrowedCount(self):
        return self._borrowedCount

    def borrowBook(self):
        self._borrowedCount+=1

    def addMoreCount(self, newCount):
        self._Count+=newCount

    def getCountinLibrary(self):
        return self._Count-self._borrowedCount

    def returnBook(self):
        self._borrowedCount-=1

mylibrary=Library() 
while True:
    print("1. Add new book")
    print("2. Loan out book")
    print("3. Return book")
    choice=int(input("What would you like to do: "))
    if choice==1:
        book=Book(input("Title: "),int(input("Count : ")))
        mylibrary.addBook(book)
    elif choice ==2:
        book=input("Title: ")
        mylibrary.loanOutBook(book)
    elif choice==3:
        book=input("Title: ")
        mylibrary.returnBook(book)
    print ()
