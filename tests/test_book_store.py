from lib.book_store import Book


"""
Book constructs with an id, title and author_name
"""
def test_book_constructs():
    book = Book(1, "Test Book", "Test author_name")
    assert book.id == 1
    assert book.title == "Test Book"
    assert book.author_name == "Test author_name"

