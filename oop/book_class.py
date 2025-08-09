class Book:
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        print(f"Deleting {self.title}")  # Destructor: called when object is deleted

    def __str__(self):
        return f"{self.title} by {self.author}, published in {self.year}"  # User-friendly string

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"  # Official string for debugging


book = Book("1984", "George Orwell", 1949)
print(book)            
print(repr(book))      
del book            