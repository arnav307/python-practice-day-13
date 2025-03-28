list_of_tuples = [
    ("Jane Austen", "Pride and Prejudice"),
    ("Charles Dickens", "Great Expectations"),
    ("Mark Twain", "The Adventures of Huckleberry Finn"),
]

authors=[]
for book in list_of_tuples:
    authors.append(book[0])

sort_of_author=sorted(authors)

sorted_books=[]
for author in sort_of_author:
    for book in list_of_tuples:
        if book[0]==author:
            sorted_books.append(book)
            
for book in sorted_books:
    print(book)
            
