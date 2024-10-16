import java.util.Scanner;

public class pattern3 {
    public static void main(String[] args) {
        Scanner inp = new Scanner(System.in);
        System.out.print("Enter number of rows: ");
        int n = inp.nextInt();

        for(int i = 0; i < n; i++) {
            for(int j = 1; j <= n; j++) {
                System.out.print(j+" ");
            }
            System.out.println();
        }
    }
}
