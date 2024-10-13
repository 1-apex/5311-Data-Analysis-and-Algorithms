
import java.util.Scanner;

class Queue {

    private int[] queue = new int[10];  // Queue of fixed size 10
    private int front = -1;              // Points to the front of the queue
    private int rear = -1;               // Points to the rear of the queue

    // Enqueue operation: Add an element to the queue
    public void enqueue(int element) {
        if (rear == queue.length - 1) {
            System.out.println("Queue overflow! Unable to enqueue.");
        } else {
            if (front == -1) {
                front = 0;
            }
            queue[++rear] = element;
            System.out.println("Element enqueued: " + element);
        }
    }

    // Dequeue operation: Remove and return the front element of the queue
    public int dequeue() {
        if (isEmpty()) {
            System.out.println("Queue underflow! No element to dequeue.");
            return -1;  // Indicating queue is empty
        } else {
            int dequeuedElement = queue[front];
            if (front == rear) { 
                front = rear = -1; 
            } else {
                front++;
            }
            System.out.println("Element dequeued: " + dequeuedElement);
            return dequeuedElement;
        }
    }

    // Peek operation: Return the front element without removing it
    public int peek() {
        if (isEmpty()) {
            System.out.println("Queue is empty. No element to peek.");
            return -1; // Indicating queue is empty
        } else {
            return queue[front];
        }
    }

    // Check if the queue is empty
    public boolean isEmpty() {
        return front == -1;
    }

    // Get the size of the queue (number of elements)
    public int size() {
        if (isEmpty()) {
            return 0;
        } else {
            return rear - front + 1;
        }
    }

    // Main method to provide the menu and interact with the user
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        Queue queue = new Queue();  // Creating a queue object
        int choice;

        while (true) {
            System.out.println("\nFunctions on queue:");
            System.out.println("1. Enqueue");
            System.out.println("2. Dequeue");
            System.out.println("3. Peek");
            System.out.println("4. Is Empty?");
            System.out.println("5. Size");
            System.out.println("6. Exit");

            System.out.print("Enter your choice: ");
            choice = scan.nextInt();

            switch (choice) {
                case 1:
                    System.out.print("Enter element to enqueue: ");
                    int element = scan.nextInt();
                    queue.enqueue(element);
                    break;
                case 2:
                    queue.dequeue();
                    break;
                case 3:
                    int frontElement = queue.peek();
                    if (frontElement != -1) {
                        System.out.println("Front element is: " + frontElement);
                    }
                    break;
                case 4:
                    if (queue.isEmpty()) {
                        System.out.println("Queue is empty.");
                    } else {
                        System.out.println("Queue is not empty.");
                    }
                    break;
                case 5:
                    System.out.println("Queue size is: " + queue.size());
                    break;
                case 6:
                    System.out.println("Exiting...");
                    System.exit(0);
                    break;
                default:
                    System.out.println("Invalid choice! Please enter a valid option.");
            }
        }
    }
}
