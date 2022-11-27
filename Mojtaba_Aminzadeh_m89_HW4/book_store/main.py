from people import Poet, Writer, Person
from asar import Poetry, Book, Asar

""" صورت سوال نخواسته بود که چیزی اجرا کنیم. من برای خودم تست کردم شما اینجا رو جدی نگیر"""
if __name__ == "__main__":
    hafez = Poet('hafez', 'hafez@gmail.com', 'male', 'ghazal')
    sadi = Poet('sadi', 'hafez@gmail.com', 'male', 'ghazal')
    sher = Poetry('sher', hafez, 'format')
    jafar = Writer('jafar', 'jafar@mail.com', 'male', 111, 'dram')
    akbar = Writer('akbar', 'jafar@mail.com', 'male', 111, 'dram')
    harry_potter = Book('harry', [jafar, akbar], 123, "2015")
    print(harry_potter.get_number_of_authors())
    print(harry_potter.authors[1].genre)
