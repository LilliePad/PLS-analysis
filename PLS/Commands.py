from User import User
from book import Book



class Commands:

    def AddBook(self):
        Author = input("Who is the author:> ")
        Country = input("What is the country:> ")
        ImageLink = input("What is the imagelink:> ")
        Language = input("What is the language:> ")
        Link = input("What is the link:> ")
        Pages = input("How many pages has the book:> ")
        Title = input("what's the name of the book:> ")
        Year = input("What is the year of realease of the book:> ")
        book = Book(Author, Country, ImageLink, Language, Link, Pages,  Title, Year)
        Book.SaveBook(book)

    def AddUser(self):
        Gender = input("Whats is your gender:> ")
        NameSet = input("Whats is your nameSet:> ")
        GivenName = input("Whats is your givenName:> ")
        Surname = input("Whats is your Surname:> ")
        StreetAdress = input("Whats is your streetAdress:> ")
        ZipCode = input("Whats is your zipCode:> ")
        City = input("Where do you live:> ")
        EmailAdress = input("Whats is your emailAdress:> ")
        Username = input("Whats is your userName:> ")
        TelephoneNumber = input("Whats is your telephoneNumber:> ")

        user = User(Gender, NameSet, GivenName, Surname, StreetAdress, ZipCode, City, EmailAdress, Username, TelephoneNumber)
        User.SaveUser(user)

    def BookReturn(self):
        Name = input("Input the name of the person who lend the book:> ")
        book = input("Input the name of the book that was lend:> ")
        Book.ReturnBook(0, book,Name)

    def BookLend(self):
        Name = input("Input the name of the person that wants to lend the book:> ")
        book = input("Input the name of the book that the person wants to lend:> ")
        Book.LendBook(0, book,Name)    

        
    def SearchBook(self):
        Book.LookupBook(0)
        


