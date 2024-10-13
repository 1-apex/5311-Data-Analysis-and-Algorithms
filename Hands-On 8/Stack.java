
import java.util.Scanner;

public class Stack {

    private final int[] stack = new int[10];  // Stack of fixed size 10
    private int top = -1;               // To track the top of the stack

    // Push operation: Add element to the stack
    public void push(int element) {
        if (top == stack.length - 1) {
            System.out.println("Stack overflow! Unable to push.");
        } else {
            stack[++top] = element;
            System.out.println("Element pushed: " + element);
        }
    }

    // Pop operation: Remove and return the top element of the stack
    public int pop() {
        if (isEmpty()) {
            System.out.println("Stack underflow! No element to pop.");
            return -1; // Indicating stack is empty
        } else {
            int poppedElement = stack[top--];
            System.out.println("Element popped: " + poppedElement);
            return poppedElement;
        }
    }

    // Peek operation: Return the top element without removing it
    public int peek() {
        if (isEmpty()) {
            System.out.println("Stack is empty. No element to peek.");
            return -1; // Indicating stack is empty
        } else {
            return stack[top];
        }
    }

    // Check if the stack is empty
    public boolean isEmpty() {
        return top == -1;
    }

    // Get the size of the stack (number of elements)
    public int size() {
        return top + 1;
    }

    // Main method to provide the menu and interact with the user
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        Stack stack = new Stack();  // Creating a stack object
        int choice;

        while (true) {
            System.out.println("\nFunctions on stack:");
            System.out.println("1. Push");
            System.out.println("2. Pop");
            System.out.println("3. Peek");
            System.out.println("4. Is Empty?");
            System.out.println("5. Size");
            System.out.println("6. Exit");

            System.out.print("Enter your choice: ");
            choice = scan.nextInt();

            switch (choice) {
                case 1:
                    System.out.print("Enter element to push: ");
                    int element = scan.nextInt();
                    stack.push(element);
                    break;
                case 2:
                    stack.pop();
                    break;
                case 3:
                    int topElement = stack.peek();
                    if (topElement != -1) {
                        System.out.println("Top element is: " + topElement);
                    }
                    break;
                case 4:
                    if (stack.isEmpty()) {
                        System.out.println("Stack is empty.");
                    } else {
                        System.out.println("Stack is not empty.");
                    }
                    break;
                case 5:
                    System.out.println("Stack size is: " + stack.size());
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
