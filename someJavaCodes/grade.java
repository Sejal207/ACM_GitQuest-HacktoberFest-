import java.util.Scanner;

public class grade {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter score: ");
        int grade = input.nextInt();

        if(grade > 100) {
            System.out.println("Invalid Input!");
        }
        else if(grade == 100) {
            System.out.println("Perfect Score");
        }
        else if(grade >= 90) {
            System.out.println("Excellent");
        }
        else if(grade >= 80) {
            System.out.println("Good");
        }
        else if(grade >= 70) {
            System.out.println("Above Average");
        }
        else if(grade >= 60) {
            System.out.println("Average");
        }
        else if(grade >= 50) {
            System.out.println("Below Average");
        }
        else if(grade >= 0) {
            System.out.println("Not Passing");
        }
        else{
            System.out.println("Invalid Output!");
        }
    }
}
