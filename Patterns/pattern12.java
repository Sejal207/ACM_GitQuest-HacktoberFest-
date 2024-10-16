import java.util.Scanner;

public class pattern12 {
    public static void main(String[] args) {
        Scanner inp = new Scanner(System.in);
        System.out.print("Enter number of rows: ");
        int n = inp.nextInt();
        char c = 'A';

        for(int i = 0; i < n; i++) {
            for(int j = 0; j < n; j++) {
                System.out.print((char)(c+j+(n*i))+" ");
            }
            System.out.println();
        }
    }
}
