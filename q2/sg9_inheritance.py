#defines a parent class which is Publication
class Publication:
    def __init__(self, title: str, author: str): #init=initializes a publication object na may title at author
        self._title = title #stores title of publication
        self._author = author #stores author of publication

    @property #allows get_title to be accesssed easier like an attribute
    def get_title(self): #retrieves publication title
        return self._title #returns publication title

    @property #allows get_author to be accesssed easier like an attribute
    def get_author(self): #retrieves publication author
        return self._author #returns publication atuhor

    @property #allows show_attributes to be accesssed easier like an attribute
    def show_attributes(self): #used to print the publication information
        print("Publication Information") #for header
        print(f"Title: {self._title}") #retrieves and prints publication title
        print(f"Author: {self._author}") #retrieves and prints publication author

#defines Book class that inherits properties and methods from Publication
class Book(Publication): 
    def __init__(self, title: str, author: str, pageno: int): #init=initializes a book object na may tile, author, and number of pages
        super().__init__(title, author) #initialized title and author thru Publication class constructor
        self._pageno = pageno #stores the book's number of pages

    @property #allows pageno to be accesssed easier like an attribute
    def pageno(self): #retrieves pageno
        return self._pageno #returns pageno

    @pageno.setter #connects the setter method to pageno property
    def pageno(self, pages): #setter that allows pageno to be changed
        if pages <= 0: #checks if new pageno value is negative or 0
            print("The number of pages must be positive.") #prints a warning message for when the page number is negative or 0
        else:
            self._pageno = pages #sets pageno to the updated value
    
    @property #allows show_attributes to be accessed easier like an attribute
    def show_attributes(self): #print attributes of book
        print(f"Title: {self._title}") #retrieves and prints title
        print(f"Author: {self._author}") #retrieves and prints author
        print(f"Number of Pages: {self._pageno}") #retrieves and prints number of pages

#defines a Magazine class that inherits some of its attributes and methods from Publication parent class
class Magazine(Publication): 
    def __init__(self, title: str, author: str, issueno: int): #init=initializes a magazine with a title, author, and issue number
        super().__init__(title, author) #initializes title and author thru Publication class constructor
        self._issueno = issueno #stores the magazine's issue number
      
    @property #allows issueno to be accessed easier like an attribute
    def issueno(self): #retrieves issueno
        return self._issueno #returns issueno

    @issueno.setter #connects setter method to issueno
    def issueno(self, number): #setter that allows issueno to be changed
        if number <= 0: #checks whether the issueno is negative or 0
            print("The issue number must be positive.") #prints a warning message when the issue number is negative or 0 kasi dapat positive ang issue number
        else:
            self._issueno = number #sets issueno to the updated value
    
    @property #allows show_attributes to be accessed easier like an attribute
    def show_attributes(self): #prints the attributes of a magazine object
        print("\nMagazine Information") #for header
        print(f"Title: {self._title}") #prints title
        print(f"Author: {self._author}") #prints author
        print(f"Issue Number: {self._issueno}") #prints issue number

publication1 = Publication("Arab-Adab", "Lupon ng Patnugot") #creates a Publication object
book1 = Book("The Metamorphosis", "Franz Kafka", 67) #creates a Book object
magazine1 = Magazine("adobo Magazine", "Angel Guerrero", 61) #creates a Magazine object

def main(): #defines the main function, for organization of the code
    publication1.show_attributes #accesses show_attributes property for publication1
    
    print("\nBook Information") #for header of book information since the warning if the page number is negative must come first before printing other attributes
    book1.pageno = -67 #attempts to update the pageno to a negative value
    book1.show_attributes #accesses show_attributes property for book1
    
    magazine1.show_attributes #accesses show_attributes property for magazine1

#calls main function to execute program
main() 
