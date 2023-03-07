class Book:
    def __init__(self, name, author, pages):
        self.name = name
        self.author = author
        self.pages = pages


book = Book("My Book", "Ivo Todorov", 200)
print(f"Book's name: {book.name}")
print(f"Book's author: {book.author}")
print(f"Number of pages: {book.pages}\n")

my_favourite_book = Book("The Green Mile", "Stephen King", 540)
print(f"Book's name: {my_favourite_book.name}")
print(f"Book's author: {my_favourite_book.author}")
print(f"Number of pages: {my_favourite_book.pages}\n")
