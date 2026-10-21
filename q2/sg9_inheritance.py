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

    def show_attributes(self):
        print(f"Title: {self._title}")
        print(f"Author: {self._author}")

class Book(Publication):
    def __init__(self, title: str, author: str, pageno: int):
        super().__init__(title, author)
        self._pageno = pageno

    @property
    def get_pageno(self):
        return self._pageno

    @pageno.setter
    def set_pageno(self, pages):
        if pages <= 0:
            print("The number of pages must be positive.")
        else:
            self._pageno = pages

    def show_attributes(self):
        print(f"Title: {self._title}")
        print(f"Author: {self._author}")
        print(f"Number of Pages: {self._pageno}")

class Magazine(Publication):
    def __init__(self, title: str, author: str, issueno: int):
        super().__init__(title, author)
        self._issueno = issueno
      
    @property
    def get_issueno(self):
        return self._issueno

    @issueno.setter
    def set_issueno(self, number):
        if number <= 0:
            print("The issue number must be positive.")
        else:
            self._issueno = number

    def show_attributes(self):
        print(f"Title: {self._title}")
        print(f"Author: {self._author}")
        print(f"Issue Number: {self._issueno}")
