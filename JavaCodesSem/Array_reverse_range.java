import java.util.Scanner;
class Array_reverse_range
{

static void reverse_range(int[] nums, int s, int e)
{
int start = s;
int end = e;

while(start<end)
{
int t = nums[start];
nums[start] = nums[end];
nums[end] = t;

start++;
end--;
}
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

int start = sc.nextInt();
int end = sc.nextInt();

reverse_range(arr,start,end);
System.out.println("Reverse array: ");
for(int i = 0; i<n; i++)
{
System.out.println(arr[i] + " ");
}
}

}

