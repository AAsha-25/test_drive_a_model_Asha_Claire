class Album:
    def __init__(self, id, title, release_year, artiest_id):
        self.id = id
        self.title = title
        self.release_year = release_year
        self.artist_id = artiest_id

    def __eq__(self, other):
        return self.__dict__ == other.__dict__


    def __repr__(self):
        return f"Album({self.id}, {self.title}, {self.release_year}, {self.artist_id})"
    