import java.util.Scanner;
class Array_Sort_Recursion
{

public static boolean Recursive_Sort(int[] arr, int i) 
{
if (i == arr.length - 1) 
{
return true;
}
if (arr[i] > arr[i + 1]) 
{
return false;
}
return Recursive_Sort(arr, i + 1);
}

public static void main(String args[])
{
Scanner sc = new Scanner(System.in);
System.out.print("Size of the array: ");
int n = sc.nextInt();
int[] arr = new int[n];

for(int i = 0; i<n; i++)
{
arr[i] = sc.nextInt();
}
System.out.print("Array:");
for(int i = 0; i<n; i++)
{
System.out.print(arr[i] + " ");
}
System.out.print("\n");

System.out.println(Recursive_Sort(arr,0));

}

}