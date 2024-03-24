# Initialize empty lists for books and members
books = []
members = []

# Define functions to add books and members without using parameters
def add_book():
    book_id = int(input("Enter book ID: "))
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    status = input("Enter book status: ")
    
    books.append({
        "book_id": book_id,
        "title": title,
        "author": author,
        "status": status
    })
    print("Book added successfully.")

def add_member():
    member_id = int(input("Enter member ID: "))
    name = input("Enter member name: ")
    
    members.append({
        "member_id": member_id,
        "name": name,
        "borrowed_books": []
    })
    print("Member added successfully.")

# Add a book titled "Python Programming" and a member named "Anelisa Maleka"
add_book()
add_member()

# Print both lists
print("\nBooks after addition:")
print(books)
print("\nMembers after addition:")
print(members)
