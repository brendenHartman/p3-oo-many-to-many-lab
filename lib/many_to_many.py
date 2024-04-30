class Author:

    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)
    
    def contracts(self):
        contracts = []
        for contract in Contract.all:
            if contract.author  == self:
                contracts.append(contract)
        return contracts

    def books(self):
        books = []
        contracts = []
        for contract in Contract.all:
            if contract.author  == self:
                contracts.append(contract)
        for contract in contracts:
            books.append(contract.book)
        return books
    
    def sign_contract(self, book, date, royalties):
        new_cont = Contract(self, book, date, royalties)
        return new_cont
    
    def total_royalties(self):
        total = 0
        for contract in Contract.all:
            if contract.author == self:
                total += contract.royalties
        return total
        
    
        
        


class Book:

    all = []

    def __init__(self, title):
        self.title = title
        Book.all.append(self)
    
    def contracts(self):
        contracts = []
        for contract in Contract.all:
            if contract.book  == self:
                contracts.append(contract)
        return contracts
    
    def authors(self):
        books = []
        contracts = []
        for contract in Contract.all:
            if contract.book  == self:
                contracts.append(contract)
        for contract in contracts:
            books.append(contract.author)
        return books


class Contract:

    all = []

    def __init__(self, author, book, date, royalties):
        if isinstance(author, Author):
            self.author = author
        else:
            raise Exception()
        
        if isinstance(book, Book):
            self.book = book
        else:
            raise Exception()
        
        if type(date) is str:
            self.date = date
        else:
            raise Exception()
        
        if type(royalties) is int:
            self.royalties = royalties
        else:
            raise Exception()
        Contract.all.append(self)

    def contracts_by_date(date):
        result = []
        for contract in Contract.all:
            if contract.date == date:
                result.append(contract)
        return result

