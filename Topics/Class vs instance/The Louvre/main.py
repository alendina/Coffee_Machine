class Painting:
    museum = 'Louvre'

    def __init__(self, title, artist, year):
        self.title = title
        self.artist = artist
        self.year = year

    def __str__(self):
        return f'"{self.title}" by {self.artist} ({self.year}) hangs in the {self.museum}.'


p = Painting(input(), input(), input())
print(p)
