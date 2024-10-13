import java.util.Scanner;

// Node class representing each element in the LinkedList
class Node {
    int data;
    Node next;

    Node(int data) {
        this.data = data;
        this.next = null;
    }
}

// LinkedList class implementing basic operations
class LinkedList {
    Node head;  // Head of the linked list

    // Insert a node at the beginning of the linked list
    public void insertAtBeginning(int data) {
        Node newNode = new Node(data);
        newNode.next = head;
        head = newNode;
        System.out.println("Inserted " + data + " at the beginning.");
    }

    // Insert a node at the end of the linked list
    public void insertAtEnd(int data) {
        Node newNode = new Node(data);
        if (head == null) {
            head = newNode;
        } else {
            Node temp = head;
            while (temp.next != null) {
                temp = temp.next;
            }
            temp.next = newNode;
        }
        System.out.println("Inserted " + data + " at the end.");
    }

    // Delete the first occurrence of a node with the given data
    public void deleteNode(int key) {
        Node temp = head, prev = null;

        // If the head node itself holds the key to be deleted
        if (temp != null && temp.data == key) {
            head = temp.next; // Changed head
            System.out.println("Deleted " + key + " from the linked list.");
            return;
        }

        // Search for the key to be deleted, keeping track of the previous node
        while (temp != null && temp.data != key) {
            prev = temp;
            temp = temp.next;
        }

        // If the key was not present in the linked list
        if (temp == null) {
            System.out.println(key + " not found in the list.");
            return;
        }

        // Unlink the node from the linked list
        prev.next = temp.next;
        System.out.println("Deleted " + key + " from the linked list.");
    }

    // Search for a node with the given data
    public boolean search(int key) {
        Node temp = head;
        while (temp != null) {
            if (temp.data == key) {
                return true;  // Node found
            }
            temp = temp.next;
        }
        return false;  // Node not found
    }

    // Display the linked list
    public void display() {
        if (head == null) {
            System.out.println("The list is empty.");
            return;
        }
        Node temp = head;
        System.out.print("Linked List: ");
        while (temp != null) {
            System.out.print(temp.data + " -> ");
            temp = temp.next;
        }
        System.out.println("null");
    }

    // Main method to interact with the user
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        LinkedList list = new LinkedList();
        int choice;

        while (true) {
            System.out.println("\nLinked List Operations:");
            System.out.println("1. Insert at beginning");
            System.out.println("2. Insert at end");
            System.out.println("3. Delete a node");
            System.out.println("4. Search for a node");
            System.out.println("5. Display the list");
            System.out.println("6. Exit");

            System.out.print("Enter your choice: ");
            choice = scan.nextInt();

            switch (choice) {
                case 1:
                    System.out.print("Enter element to insert at beginning: ");
                    int element1 = scan.nextInt();
                    list.insertAtBeginning(element1);
                    break;
                case 2:
                    System.out.print("Enter element to insert at end: ");
                    int element2 = scan.nextInt();
                    list.insertAtEnd(element2);
                    break;
                case 3:
                    System.out.print("Enter element to delete: ");
                    int key = scan.nextInt();
                    list.deleteNode(key);
                    break;
                case 4:
                    System.out.print("Enter element to search: ");
                    int searchKey = scan.nextInt();
                    if (list.search(searchKey)) {
                        System.out.println("Element " + searchKey + " found in the list.");
                    } else {
                        System.out.println("Element " + searchKey + " not found.");
                    }
                    break;
                case 5:
                    list.display();
                    break;
                case 6:
                    System.out.println("Exiting...");
                    System.exit(0);
                default:
                    System.out.println("Invalid choice! Please enter a valid option.");
            }
        }
    }
}
