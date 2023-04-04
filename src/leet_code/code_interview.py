# Define the Story class
class Story:
    def __init__(self, title, author, content):
        self.title = title
        self.author = author
        self.content = content
        self.current_page = 0

    def get_current_page_text(self):
        page_size = 1000
        start_index = self.current_page * page_size
        end_index = start_index + page_size
        if start_index >= len(self.content):
            return None  # Check if current page is out of range
        return self.content[start_index:end_index]

# Define the CloudReadingApp class
class CloudReadingApp:
    def __init__(self):
        self.library = []
        self.active_book_index = None

    def add_book(self, book):
        self.library.append(book)

    def remove_book(self, title):
        for index, book in enumerate(self.library):
            if book.title == title:
                del self.library[index]
                if self.active_book_index == index:
                    self.active_book_index = None

    def set_active_book(self, title):
        for index, book in enumerate(self.library):
            if book.title == title:
                self.active_book_index = index
                return

    def get_active_book(self):
        if self.active_book_index is not None:
            return self.library[self.active_book_index]

    def get_current_page_text(self):
        active_book = self.get_active_book()
        if active_book:
            return active_book.get_current_page_text()

    def next_page(self):
        active_book = self.get_active_book()
        if active_book:
            if active_book.current_page < len(active_book.content) // 1000:
                active_book.current_page += 1
                return active_book.get_current_page_text()

    def previous_page(self):
        active_book = self.get_active_book()
        if active_book:
            if active_book.current_page > 0:
                active_book.current_page -= 1
                return active_book.get_current_page_text()
            else:
                active_book.current_page = 0
                return active_book.get_current_page_text()


# Test the CloudReadingApp class
if __name__ == '__main__':
    app = CloudReadingApp()

    # Add some books
    book1 = Story("The Gift of the Magi", "O. Henry", "Once upon a time...")
    app.add_book(book1)
    book2 = Story("The Lottery", "Shirley Jackson", "The morning of June 27th was clear and sunny...")
    app.add_book(book2)

    app.set_active_book("The Gift of the Magi")
    active_book = app.get_active_book()
    active_book.current_page = 0  # Set the current page to 0
    current_page_text = app.get_current_page_text()
    print(current_page_text)

    # Move to the next page and display it
    next_page_text = app.next_page()
    print(next_page_text)

    # Move to the previous page and display it
    previous_page_text = app.previous_page()
    print(previous_page_text)

    # Remove a book and print the updated library
    app.remove_book("The Lottery")
    print([book.title for book in app.library])

    # Line 9 - 15: The get_current_page_text() method is defined inside the Story class , which represents a
    # book.This method is used to retrieve the current page of the book. The page_size variable is set to 1000,
    # which represents the maximum number of characters to be displayed on a page. The start_index variable is
    # calculated by multiplying the current page number (self.current_page) by the page_size, which gives the index
    # of the first character of the current page. The end_index variable is set to start_index + page_size,
    # which gives the index of the last character of the current page. The if statement checks whether the start
    # index of the current page is greater than or equal to the total number of characters in the book (len(
    # self.content)). If this is the case, it means that the current page is out of range, and None is returned.
    # Otherwise, the return statement returns a substring of the book's content that starts from the start_index and
    # ends at the end_index, representing the current page's text.

    # Line 18 - 21: This is a Python class definition for a CloudReadingApp. In the __init__ method, the class
    # initializes two instance variables library and active_book_index. library is a list that will hold all of the
    # books in the app's library, and active_book_index is a variable that keeps track of the index of the currently
    # active book in the library. library is initialized as an empty list with self.library = [],
    # while active_book_index is initialized to None with self.active_book_index = None.

    # line 26 - 31: This code defines a method called remove_book() that takes a title parameter. It first loops
    # through the list of books in the library using enumerate() to get both the index and the book object at the
    # same time. Then, for each book, it checks if the title matches the book's title attribute. If there is a match,
    # it uses the del statement to remove the book from the library list using the index.
    #
    # If the active_book_index equals the index of the book that was just removed, then self.active_book_index is set
    # to None to indicate that there is no active book selected.

    # Line 33-37: This function takes a book title as an argument and sets the active book index to the index of the
    # book with the corresponding title in the library list. It does this by iterating through the library list using
    # the enumerate() function, which allows it to get both the index and the book object at each iteration. If it
    # finds a book with a matching title, it sets the active book index to the current index and then returns, ending
    # the loop. If it doesn't find a matching book, the active book index remains unchanged.

    # Line 39-41: This function returns the active book in the library. It first checks if there is an active book by
    # checking if self.active_book_index is not None. If there is an active book, it returns the book object from the
    # self.library
    # list at the index self.active_book_index. If there is no active book, it returns None.

    # Line 48-53: This code is for the next_page method of the CloudReadingApp class. Here is what it does:
    # It first gets the active book by calling the get_active_book() method. This is done to check if there is an
    # active book or not.
    # If there is an active book, it checks if the current page is less than the total number of pages in the book.
    # This is done to ensure that we do not go beyond the last page of the book.
    # If the current page is less than the total number of pages, it increments the current_page attribute of the
    # active book by 1.
    # Finally, it returns the text of the current page of the active book by calling the get_current_page_text()
    # method of the active book.
    # So, in summary, this method helps to navigate to the next page of the active book, if there is one.

    # Line 55-63: This code defines a method called previous_page() which is used to navigate to the previous page of
    # the currently active book in the CloudReadingApp instance.
    # The method first gets the currently active book using the get_active_book() method. If there is an active book,
    # it checks if the current page number of the book is greater than zero. If it is, it decrements the current page
    # number by one, and returns the text of the new current page using the get_current_page_text() method of the book.
    # If the current page number is already 0, it sets the current page number to 0 again (as it cannot go below 0)
    # and returns the text of the first page of the book using get_current_page_text().
    # Essentially, this method allows the user to move back one page in the currently active book, or to stay on the
    # first page if they are already on it.