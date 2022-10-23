shelf_books = input()
shelf_books_list = shelf_books.split('&')

command = input()

while command != 'Done':
    command = command.split(' | ')

    if command[0] == 'Add Book':
        if command[1] not in shelf_books_list:
            shelf_books_list.insert(0, command[1])

    if command[0] == 'Take Book':
        if command[1] in shelf_books_list:
            shelf_books_list.remove(command[1])

    if command[0] == 'Swap Books':
        if command[1] in shelf_books_list and command[2] in shelf_books_list:
            book_one_index = shelf_books_list.index(command[1])
            book_two_index = shelf_books_list.index(command[2])

            shelf_books_list[book_one_index] = command[2]
            shelf_books_list[book_two_index] = command[1]

    if command[0] == 'Insert Book':
        shelf_books_list.append(command[1])

    if command[0] == 'Check Book':
        try:
            book_found = shelf_books_list[int(command[1])]
            print(book_found)
        except IndexError:
            pass

    command = input()

print(', '.join(shelf_books_list))
