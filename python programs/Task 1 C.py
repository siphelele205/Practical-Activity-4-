# Initialize empty lists for books and members
books = []
members = []

# Add a book titled "Python Programming"
book_id = 2024001
title = "Python Programming"
author = "Jacob Zuma"
status = "Available"
books.append({
    "book_id": book_id,
    "title": title,
    "author": author,
    "status": status
})

# Add a member named "Anelisa Maleka"
member_id = 1
name = "Anelisa Maleka"
members.append({
    "member_id": member_id,
    "name": name,
    "borrowed_books": []
})

# Print both lists
print("Books after addition:")
print(books)
print("\nMembers after addition:")
print(members)
