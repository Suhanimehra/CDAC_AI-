filename='books.txt'
books=[
    {
        "id": 1,
        "title": "Python Programming",
        "author": "John Zelle",
        "genre":"Technical",
        "price": 650,
        "copy":15
    },
    {
        "id": 2,
        "title": "Clean Code",
        "author": "Robert Martin",
        "genre":"Technical",
        "price": 950,
        "copy":8
        }
]
id_counter=len(books)

def main():
    while True:
        
        menu()
        menu_choice=int(input("Enter Your Choice: "))
        
        match menu_choice:
            case 1:
                add_book()
            case 2:
                view_book()
            case 3:
                search_books()
            case 4:
                update_book()
            case 5:
                delete_book()
            case 6:
                save_to_file()
            case 7:
                load_to_file()
            case 8:
                break
            case _:
                print("Enter Valid Choice.")
        
        print("="*60)

def menu():
    
    print('='*60)
    print("-------Library Managment System-------")
    menu_text='''
    1. Add Book 
    2. View Catalog 
    3. Search Books 
    4. Update Details 
    5. Delete Book 
    6. Save to File 
    7. Load from File 
    8. Exit
    '''
    print(menu_text)
    print('='*60)
    
    
def add_book():
    global id_counter
    try:
        title=input("Enter the Title: ")
        if title.strip()=='':
            print("Title Cannot be an Empty String.")
            return
        author=input("Enter Author: ")
        if author.strip()=='':
            print("Author Cannot be an Empty String.")
            return
        genre=input("Enter Genre: ")
        if genre.strip()=='':
            print("Genre Cannot be an Empty String.")
            return
        price=float(input("Enter Price of Book: "))
        if price <=0 :
            print("Price Cannot be Negative.")
            return
        copies=int(input("Enter Copies of Book: "))
        if copies<0:
            print("Copy Cannot be Negative.")
            return
            
        books.append(dict(id=id_counter+1,title=title,author=author,genre=genre,price=price,copy=copies))
        id_counter+=1
        
        print("Book Added Successfully!")
    except ValueError:
        print("Enter Valid Input.")


def view_book():
    
    if len(books)==0:
        print("No Books in Record.")
    elif len(books)==1:
        print_one_record(books[0])
    else:
        print_many_record(books)
    
        
def print_one_record(b):
    
    id,title,author,genre,price,copies=b.values()
    print('-'*60)
    
    print("----Book Details----")
    print(f"ID         {id}")
    print(f"Title      {title}")
    print(f"Author     {author}")
    print(f"Genre      {genre}")
    print(f"Price      {price:.2f}")
    print(f"Copy       {copies}")
    
    print('-'*60)
    
    
def print_many_record(books):
    
    print('-'*80)
    print("---Books Details---")
    print(f"{'ID':<5}{'Title':<20}{'Author':<20}{'Genre':<15}{'Price':>10}{'Copy':>10}")
    print('-'*80)
    for b in books:
        id,title,author,genre,price,copy=b.values()
        print(f"{id:<5}{title:<20}{author:<20}{genre:<15}{price:>10.2f}{copy:>10}")
    print('-'*80)


def search_books():
    try:
        search_choice=int(input("Enter 1 to search by BookID.\n Enter 2 to search by Title.\n Enter 3 to search by Author."))

        if search_choice==1:
            search_by_id()
        elif search_choice==2:
            search_by_title()
        elif search_choice==3:
            search_by_author()
        else:
            print("Enter A Valid Integer")
    except:
        print("Retry Again")
        
def search_by_id():
    try:
        search_id_choice=int(input("Enter The Book ID: "))
        
        res=[b for b in books if b['id']==search_id_choice]
        
        if not res:
            print("No Book Found for Book ID.")
            return
        
        print("Book Found")
        print_one_record(res[0])
    except ValueError:
        print("Enter A Valid ID")

def search_by_title():
    try:
        search_title_choice=input("Enter The Book Title: ").strip()
        # here we have to find with substring concept
        res=[b for b in books if search_title_choice.lower() in b['title'].lower()]
        # This Matches the Values res=[b for b in books if b['title'].lower()==search_title_choice.lower()]
        
        if not res:
            print("No Book Found for Book Title.")
        
        print("Book Found")
        print_many_record(res)
    except:
        print("Enter A Valid Title")

def search_by_author():
    try:
        search_author_choice=input("Enter The Book Author: ").strip()
        
        res=[b for b in books if search_author_choice.lower() in b['author'].lower()]
        # res=[b for b in books if search_author_choice.lower() in b['author'].lower()]
        
        if not res:
            print("No Book Found for Book Author.")
        
        print("Book Found")
        print_many_record(res)
    except:
        print("Enter A Valid Author")

def update_book():
    try:
        update_id=int(input("Enter The Book ID to Update: "))
        
        res=[b for b in books if b['id']==update_id]
        
        if not res:
            print("No Book ID Found.")
            return
        else:
            price=float(input("Enter Price: "))
            if price <=0 :
                print("Price Cannot be Negative.")
                return
            copy=int(input("Enter Copy: "))
            if copy<0:
                print("Copy Cannot be Negative.")
                return
            
            res[0]['price']=price
            res[0]['copy']=copy
            print("Book Updated Successfully.")
            print_one_record(res[0])
        
        
    except ValueError:
        print("Enter a Valid Book ID to update")

def delete_book():
    try:
        delete_id=int(input("Enter The Book ID to Delete: "))
        
        res=[b for b in books if b['id']==delete_id]
        

        if not res :
            print("No ID found.")
        else:
            choice=input("Are You Sure You want to Delete[y/n]: ").lower().strip()
            if choice=='y':
                
                books.remove(res[0])
                print("Book Deleted Successfully")
                print_many_record(books)
            else:
                print("No Book Was Deleted")
                print_many_record(books)
                
    except ValueError :
        print("Enter a Valid ID to delete.")
        
def save_to_file():
    global filename
    
    with open(filename,mode='w') as file:
        pass
        
        

def load_to_file():
    pass
if __name__=='__main__':
    main()