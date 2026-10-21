class Publication:
    def __init__(self, title: str, author: str):
        self._title = title
        self._author = author

    @property
    def get_title(self):
        return self._title

    @property
    def get_author(self):
        return self._author

    @property
    def show_attributes(self):
        print("Publication1")
        print(f"Title: {self._title}")
        print(f"Author: {self._author}")

class Book(Publication):
    def __init__(self, title: str, author: str, pageno: int):
        super().__init__(title, author)
        self._pageno = pageno

    @property
    def pageno(self):
        return self._pageno

    @pageno.setter
    def pageno(self, pages):
        if pages <= 0:
            print("The number of pages must be positive.")
        else:
            self._pageno = pages
    
    @property
    def show_attributes(self):
        print(f"Title: {self._title}")
        print(f"Author: {self._author}")
        print(f"Number of Pages: {self._pageno}")

class Magazine(Publication):
    def __init__(self, title: str, author: str, issueno: int):
        super().__init__(title, author)
        self._issueno = issueno
      
    @property
    def issueno(self):
        return self._issueno

    @issueno.setter
    def issueno(self, number):
        if number <= 0:
            print("The issue number must be positive.")
        else:
            self._issueno = number
    
    @property
    def show_attributes(self):
        print("\nMagazine Information")
        print(f"Title: {self._title}")
        print(f"Author: {self._author}")
        print(f"Issue Number: {self._issueno}")

publication1 = Publication("Arab-Adab", "Lupon ng Patnugot")
book1 = Book("The Metamorphosis", "Franz Kafka", 67)
magazine1 = Magazine("adobo Magazine", "Angel Guerrero", 61)

def main():
    publication1.show_attributes
    
    print("\nBook Information")
    book1.pageno = -67
    book1.show_attributes
    
    magazine1.show_attributes

main()
