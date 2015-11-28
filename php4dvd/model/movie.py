class Movie(object):

#Using not really all the data for this project - just some of them
#For the real project - describe all movie fields
    def __init__(self, imbnum="", title="", year="", notes=""):
        self.imbnum = imbnum
        self.title = title
        self.year = year
        self.notes=notes

    @classmethod
    def CorrectData(cls):
        return cls(imbnum="12345", title="Happy Story", year="1990", notes="Notes")

    @classmethod
    def UncorrectData(cls):
        return cls(imbnum="123456",  year="1991", notes="Notes1")