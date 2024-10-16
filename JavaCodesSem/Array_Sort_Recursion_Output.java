import java.util.Scanner;
class Array_Sort_Recursion_Output
{

public static void Recursive_SortArray(int[] arr, int i) 
{
int n = arr.length;
if (i == arr.length - 1) 
{
return;
}
for (int j = 0; j < n - i - 1; j++) {
if (arr[j] > arr[j + 1]) {
int temp = arr[j];
arr[j] = arr[j + 1];
arr[j + 1] = temp;
}
}
Recursive_SortArray(arr, i + 1);
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

Recursive_SortArray(arr, 0);

System.out.print("Sorted Array:");
for(int i = 0; i<n; i++)
{
System.out.print(arr[i] + " ");
}

}

}