def delete_book():
    with open("books_StudentID.txt", "r+") as f:
        lines = f.readlines()
        #prompt the user if they want to use the function
        user_prompt = input("Would you like to delete books? (y/n): ")
        while True:
            if user_prompt == "n":
                print("Exiting...")
                break
            elif user_prompt == "y":
                user_delete = int(input("Enter the ISBN code for the book you'd like to delete: "))
                #splitting the book and searching for book
                for line in lines:
                    data = line.strip().split(",")
                    isbn = data[0]
                    if user_delete == isbn:
                        #asking for confirmation
                        confirmation = input(f"Are you sure you want to delete {user_delete}?\n Enter (y) for yes (n) to stop: ").lower()
                        if confirmation == "yes":
                            lines.remove(line) #removed line from lists 
                            print("Book has been deleted")
                            #asking if user wants to delete another book
                            while True:
                                continuing = input("Would you like to delete another book?\n Type (y) for yes (n) to stop: ").lower()
                                if continuing == "n":
                                    break
                                elif continuing == "y":
                                    continue
                                else:
                                    input("Please only use (y/n): ").lower()
                            break
                         #if input is no
                        elif confirmation == "no":
                            print("Deletion has been cancelled")
                            break
                        else:
                            input("Invalid input, please only use (y/n): ").lower()
                        break
                else: #if book not found
                    input("There is no such book.\nPlease enter an existing book: ")
            else:
                input("Please use the appropriate input.\n Enter (y) for yes and (n) for no: ").lower()

delete_book()
                    