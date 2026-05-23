

b = Book("Python Basics", "A. Example")

assert b.borrowed_by is None          # book starts as available

assert b.borrow("Mira") is True      # borrowing works
assert b.borrow("Noah") is False     # second borrow blocked

assert b.return_book() is True       # return works
assert b.return_book() is False      # can't return twice