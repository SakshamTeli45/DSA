"""Library Book Registry — Singly Linked List."""


class Node:
    def __init__(self, book_id):
        self.book_id = book_id
        self.next = None


class BookLinkedList:
    def __init__(self):
        self.head = None

    def insert_beginning(self, book_id):
        node = Node(book_id)
        node.next = self.head
        self.head = node
        print(f"Book ID {book_id} inserted at the beginning.")

    def insert_end(self, book_id):
        node = Node(book_id)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node
        print(f"Book ID {book_id} inserted at the end.")

    def delete_beginning(self):
        if self.head is None:
            print("The book list is empty.")
            return None

        removed_id = self.head.book_id
        self.head = self.head.next
        print(f"Deleted book ID: {removed_id}")
        return removed_id

    def display(self):
        if self.head is None:
            print("The book list is empty.")
            return

        current = self.head
        print("Book IDs:", end=" ")
        while current is not None:
            print(current.book_id, end="")
            current = current.next
            if current is not None:
                print(" -> ", end="")
        print(" -> None")


def main():
    book_list = BookLinkedList()

    while True:
        print("\nLIBRARY BOOK REGISTRY")
        print("1. Insert at beginning")
        print("2. Insert at end")
        print("3. Delete from beginning")
        print("4. Display book IDs")
        print("0. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            book_id = input("Enter book ID: ").strip()
            if book_id:
                book_list.insert_beginning(book_id)
            else:
                print("Book ID cannot be empty.")
        elif choice == "2":
            book_id = input("Enter book ID: ").strip()
            if book_id:
                book_list.insert_end(book_id)
            else:
                print("Book ID cannot be empty.")
        elif choice == "3":
            book_list.delete_beginning()
        elif choice == "4":
            book_list.display()
        elif choice == "0":
            print("Library Book Registry closed.")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
