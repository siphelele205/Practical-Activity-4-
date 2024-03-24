import pandas as pd

# Initialize empty DataFrames for books and members
books_df = pd.DataFrame(columns=["book_id", "title", "author", "status"])
members_df = pd.DataFrame(columns=["member_id", "name", "borrowed_books"])

# Add a book titled "Python Programming"
book_id = 2024001
title = "Python Programming"
author = "Jacob Zuma"
status = "Available"
books_df = books_df.append({
    "book_id": book_id,
    "title": title,
    "author": author,
    "status": status
}, ignore_index=True)

# Add a member named "Anelisa Maleka"
member_id = 1
name = "Anelisa Maleka"
members_df = members_df.append({
    "member_id": member_id,
    "name": name,
    "borrowed_books": []
}, ignore_index=True)

# Print both DataFrames
print("Books after addition:")
print(books_df)
print("\nMembers after addition:")
print(members_df)
