from lib.book_store import Book


"""
Book constructs with an id, title and author_name
"""
def test_book_constructs():
    book = Book(1, "Test Book", "Test author_name")
    assert book.id == 1
    assert book.title == "Test Book"
    assert book.author_name == "Test author_name"

"""
We can format books to strings nicely
"""
def test_books_format_nicely():
    book = Book(3, 'Emma', 'Jane Austen')
    assert str(book) == "Book(3, Emma, Jane Austen)"
    # Try commenting out the `__repr__` method in lib/book.py
    # And see what happens when you run this test again.

"""
We can compare two identical books
And have them be equal
"""
def test_books_are_equal():
    book1 = Book(4, 'Dracula', 'Bram Stoker')
    book2 = Book(4, 'Dracula', 'Bram Stoker')
    assert book1 == book2

"""
Constructs with 
id, title, author_name, 
"""
def test_construsts_with_fields():
    book = Book(4, 'Dracula', 'Bram Stoker')
    assert book.id == 4
    assert book.title == 'Dracula'
    assert book.author_name == 'Bram Stoker'
    