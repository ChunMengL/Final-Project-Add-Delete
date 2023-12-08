def add_book():
    with open("books_StudentID.txt",'a+') as f:
        file = f.read()
        
    prompt = input("Would you like to add a new book? Use (Y) for yes and (N) for no: ").upper()
    while True:
        if prompt == "Y":
            new_book = [
                input("ISBN: "),
                input("Author: "),
                input("Title: "),
                input("Publisher: "),
                input("Genre: "),
                input("Year Published (YYYY): "),
                input("Date Purchased (YYYY/MM/DD): "),
                input("Status (read/to-read/missing): "),
            ]
            
            file_list = file.split('\n')  # Convert the string to a list
            file_list.append(','.join(new_book))  # Append the new book as a comma-separated string
            print("Book added successfully")

            while True:
                continuing = input("Would you like to add another book? Use (Y) for yes and (N) for no: " ).upper()
                if continuing == "Y":
                    new_book = [
                        input("ISBN: "),
                        input("Author: "),
                        input("Title: "),
                        input("Publisher: "),
                        input("Genre: "),
                        input("Year Published (YYYY): "),
                        input("Date Purchased (YYYY/MM/DD): "),
                        input("Status (read/to-read/missing): "),
                    ]
                    file_list.append(new_book)
                    print("Book added successfully")
                elif continuing == "N":
                    print("Thank you for adding new books")
                    break
                else:
                    input("Please use (Y/N) only: ")
            break
        elif prompt == "N":
            print("No books added")
            break
        else:
            input("Please use (Y/N) only: ").upper()
add_book()