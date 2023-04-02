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
