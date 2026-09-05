
filename = 'books.txt'
# books = [
#     {
#         "id": 1,
#         "title": "Python Programming",
#         "author": "John Zelle",
#         "genre": "Technical",
#         "price": 650.00,
#         "copies": 15
#     },
#     {
#         "id": 2,
#         "title": "Clean Code",
#         "author": "Robert Martin",
#         "genre": "Technical",
#         "price": 950.00,
#         "copies": 8
#     },
#     {
#         "id": 3,
#         "title": "The Great Gatsby",
#         "author": "F. Scott Fitzgerald",
#         "genre": "Fiction",
#         "price": 350.00,
#         "copies": 20
#     },
#     {
#         "id": 4,
#         "title": "Sapiens",
#         "author": "Yuval Noah Harari",
#         "genre": "History",
#         "price": 550.00,
#         "copies": 12
#     },
#     {
#         "id": 5,
#         "title": "Cosmos",
#         "author": "Carl Sagan",
#         "genre": "Science",
#         "price": 480.00,
#         "copies": 6
#     }
# ]
books = []

def welcome():
    menu = '''
    1. Add book
    2. View Catalog
    3. Search Books
    4. Update Details
    5. Delete Book
    6. Save to file
    7. Load from File
    8. Exit'''

    print('*'*70)
    print(f"{'Welcome To Libray Book Management':^70}")
    print('*'*70)
    print(menu)
    print('*'*70)

def load_catalog_from_file(filename,books):
    try:
        with open(filename , mode='r') as file:
            for line in file:
                line = line.strip()

                if line == '':
                    continue

                data = line.split('|')

                book = {
                    "id": int(data[0]),
                    "title": data[1],
                    "author":data[2],
                    "genre":data[3],
                    "price":float(data[4]),
                    "copies": int(data[5])
                }
                books.append(book)


        print("File Loaded Successfully ... ")
    except:
        print("Failed to load file. Please Try again Later..")

def sync_catalog_to_file(filename, books):
    try:
        with open(filename, "w") as file:

            for book in books:
                line = (
                    f"{book['id']}|"
                    f"{book['title']}|"
                    f"{book['author']}|"
                    f"{book['genre']}|"
                    f"{book['price']}|"
                    f"{book['copies']}\n"
                )

                file.write(line)

        print("Books saved successfully.")


    except OSError:
        print("Error writing to file.")

def render_catalog(books):
    if len(books) == 0:
        print("No books in database.")
        return
    elif len(books) == 1:
        print_one_book(books[0])
    else:
        print_all_books(books)

def print_one_book(b):
    pass
def print_all_books(book_dict):
    print('_'*85)
    print(f'{'ID':<5}{'Title':<20}{'Author':<25}{'Genre':<10}{'Price':>10}{'Copies':>15}')
    for b in book_dict:
        id,title,author,genre,price,copies = b.values()
        print(f'{id:<5}{title:<20}{author:<25}{genre:<10}{price:>10}{copies:>15}')
    print('_'*85)


def add_book_entry(books, next_id):
    title = input("Enter the title for book : ")
    author = input("Enter Author of the book : ")
    genre = input("Input Genre of the book : ")
    if title.strip() == '' or author.strip() == '' or genre.strip()== '':
        print("Title, Author, Genre cannot be empty...")
        return
    price = float(input("Enter Price of the book : "))
    copies = int(input("Enter Copies of the book : "))
    if price <= 0.0 or copies <= 0:
        print("Must be more than 0")
        return

    books.append(dict(id=next_id,title=title,author=author,genre=genre,price=price,copies=copies))
    print("Book Added Successfully ")


def main():
    global filename
    global books
    next_id = len(books) + 1
    while True:
        welcome()

        choice = int(input('Enter your choice : '))

        match(choice):
            case 1:
                add_book_entry(books,next_id)
            case 2:
                render_catalog(books)
            case 6:
                sync_catalog_to_file(filename,books)
            case 7:
                load_catalog_from_file(filename,books)
            case 8:
                break
            case _:
                print("Invalid Input")


if __name__ == '__main__':
    main()