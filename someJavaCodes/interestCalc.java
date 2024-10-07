import java.util.Scanner;

public class interestCalc {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Enter amount deposited: ");
        double amt = input.nextDouble();
        System.out.print("Enter yearly interest rate: ");
        double i = input.nextDouble();
        System.out.print("Enter income tax rate: ");
        double t = input.nextDouble();

        double interest = ((amt*i) - (amt*t*i)/100)/100;
        System.out.println("Interest earned in the year = " + interest);
    }
}
