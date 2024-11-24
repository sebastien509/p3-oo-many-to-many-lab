class Author:

    all_authors = []

    def __init__(self, name):
        if not isinstance(name, str) or not name.strip():
            raise Exception("name must be a non-empty string.")
        self.name = name
        Book.all_books.append(self)

    def __repr__(self):
        return f" Author:{self.name}"

    def contracts(self):
        all_my_contracts =  [ contracts for contracts in Contract.all_contracts if contracts.author == self ]

        my_unique_contracts = set (all_my_contracts) 

        return list (my_unique_contracts)
        # return list( set( [ contract.doctor for contract in Contract.all_contracts if contract.patient == self ] ) )

    def books(self):
        return list( set( [ Contract.book for Contract in Contract.all_contracts if Contract.author == self ] ) )

    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties )

    def total_royalties(self):
        return sum(contract.royalties for contract in Contract.all_contracts if contract.author == self)




class Book:
    
    all_books = []

    def __init__(self, title):
        if not isinstance(title, str) or not title.strip():
            raise Exception("title must be a non-empty string.")
        self.title = title
        Author.all_authors.append(self)

    def __repr__(self):
        return f"Book Title: {self.title}"
    
    def contracts(self):
        return list(set ([ contract for contract in Contract.all_contracts if contract.book == self ] ))

    def authors(self):
        return [ Contract.author for Contract in Contract.all_contracts if Contract.book == self]




class Contract:

    all_contracts = []
 
    def __init__(self, author, book, date, royalties):
        # Validate author
        if not isinstance(author, Author):
            raise Exception("Author must be an instance of the Author class.")
        # Validate book
        if not isinstance(book, Book):
            raise Exception("Book must be an instance of the Book class.")
        # Validate date
        if not isinstance(date, str) or not date.strip():
            raise Exception("Date must be a non-empty string.")
        if not isinstance(royalties, int) or  (0 > royalties > 100):
            raise Exception("Royalties must be a number between 0 and 100.")


        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all_contracts.append(self)  # Add to the list of all contracts

    def __repr__(self):
        return (
            f"Contract(author={self.author}, book={self.book}, date='{self.date}', "
            f"royalties={self.royalties}%)"
        )


    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, new_value):
        if isinstance(new_value, Author):
             self._author = new_value
        else:   
            raise TypeError(" Author must be of type Author")

        
    @property
    def book(self):
        return self._book

    @book.setter
    def book(self, new_value):
        if isinstance(new_value, Book):
             self._book = new_value
        else:   
            raise Exception(" book must be of type book")

    @classmethod
    def contracts_by_date(cls, date):
        list_dates = [contract for contract in cls.all_contracts if contract.date == date]

        return sorted( list_dates, key=lambda  contract : contract.date)
