import java.util.Scanner;

public class pattern25 {
    public static void main(String[] args) {
        Scanner inp = new Scanner(System.in);
        System.out.print("Enter number of rows: ");
        int n = inp.nextInt();

        for(int i = 0; i < n; i++) {
            for(int j = 0; j < (n-i); j++) {
                System.out.print(j+1);
            }
            for(int j = 0; j < (2*i); j++) {
                System.out.print("*");
            }
            for(int j = 0; j < (n-i); j++) {
                System.out.print(n-j-i);
            }
            System.out.println();
        }
    }
}
