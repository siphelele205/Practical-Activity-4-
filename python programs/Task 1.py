books = []
members = []

def add_book(book_id, title, author, status):
    books.append({
        "book_id": book_id,
        "title": title,
        "author": author,
        "status": status
    })

def add_member(member_id, name):
    members.append({
        "member_id": member_id,
        "name": name,
        "borrowed_books": []
    })

# Example usage:
add_book(1, "Python Programming", "John Smith", "Available")
add_book(2, "Data Structures and Algorithms", "Jane Doe", "Unavailable")
add_member(101, "Alice")
add_member(102, "Bob")

print("Books:", books)
print("Members:", members)
