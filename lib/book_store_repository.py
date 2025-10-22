from lib.book_store import Book

class BookRepository:

    # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection

    # Retrieve all books
    def all(self):
        rows = self._connection.execute('SELECT * from books')
        books = []
        for row in rows:
            item = Book(row["id"], row["title"], row["author_name"])
            books.append(item)
        return books

    # Find a single artist by their id
    def find(self, id):
        rows = self._connection.execute(
            'SELECT * from books WHERE id = %s', [id])
        row = rows[0]
        return Book(row["id"], row["title"], row["author_name"])

    # # Create a new artist
    # # Do you want to get its id back? Look into RETURNING id;
    # def create(self, artist):
    #     self._connection.execute('INSERT INTO books (title, author_name) VALUES (%s, %s)', [
    #                              artist.title, artist.author_name])
    #     return None

    # # Delete an artist by their id
    # def delete(self, id):
    #     self._connection.execute(
    #         'DELETE FROM books WHERE id = %s', [id])
    #     return None
