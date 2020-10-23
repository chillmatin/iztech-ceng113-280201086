#Given data
first_book_price = 1
first_books = 8
more_book_price = 19.99
#more_books = ? 
total_cost = 80.96

#Evaluation of given data
first_cost = first_book_price * first_books
more_cost = total_cost - first_cost

#Finding the number of extra books
more_books = more_cost / more_book_price

#output
print(more_books)