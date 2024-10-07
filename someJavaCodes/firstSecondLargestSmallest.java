import java.util.Scanner;

public class firstSecondLargestSmallest {

    static int largestOf3(int a, int b, int c) {
        int largest;
        if (a >= b) {
            if (a >= c) {
                largest = a;
            }
            else {
                largest = c;
            }
        }
        else if (b >= c) {
            largest = b;
        }
        else{
            largest = c;
        }

        return largest;
    }

    static int smallestOf3(int a, int b, int c) {
        int smallest;
        if (a <= b) {
            if (a <= c) {
                smallest = a;
            }
            else {
                smallest = c;
            }
        }
        else if (b <= c) {
            smallest = b;
        }
        else{
            smallest = c;
        }

        return smallest;
    }

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter 4 numbers: ");
        int a = input.nextInt(), b = input.nextInt(), c = input.nextInt(), d = input.nextInt();

        int first, second, smallest;

        if (a >= b) {
            if (a >= c) {
                if (a >= d) {
                    first = a;
                    second = largestOf3(b, c, d);
                    smallest = smallestOf3(b, c, d);
                }
                else {
                    first = d;
                    second = largestOf3(b, c, a);
                    smallest = smallestOf3(b, c, a);
                }
            }
            else if(c >= d) {
                first = c;
                second = largestOf3(b, a, d);
                smallest = smallestOf3(b, a, d);
            }
            else{
                first = d;
                second = largestOf3(b, c, a);
                smallest = smallestOf3(b, c, a);
            }
        }
        else if(b >= c) {
            if (b >= d) {
                first = b;
                second = largestOf3(a, c, d);
                smallest = smallestOf3(a, c, d);
            }
            else {
                first = d;
                second = largestOf3(b, c, a);
                smallest = smallestOf3(b, c, a);
            }
        }

        else if(c >= d) {
            first = c;
            second = largestOf3(b, a, d);
            smallest = smallestOf3(b, a, d);
        }

        else {
            first = d;
            second = largestOf3(b, c, a);
            smallest = smallestOf3(b, c, a);
        }

        System.out.println("Largest: "+first);
        System.out.println("Second Largest: "+second);
        System.out.println("Smallest: "+smallest);
    }
}
