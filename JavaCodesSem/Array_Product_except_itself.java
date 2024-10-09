import java.util.Scanner;
class Array_Product_except_itself
{

public static void product(int[] nums)
{
int product = 1;
for(int i = 0; i<nums.length; i++)
{
product*=nums[i];
nums[i] = product/nums[i];
}
}

public static void main(String args[])
{
Scanner sc = new Scanner(System.in);
System.out.print("Size of the array: ");
int n = sc.nextInt();
int[] arr = new int[n];

System.out.print("Elements of the array: ");
for(int i = 0; i<n; i++)
{
arr[i] = sc.nextInt();
}

product(arr);
System.out.print("Solution Array:");
for(int i = 0; i<n; i++)
{
System.out.print(arr[i] + " ");
}

}
}
class Array_Product_except_itself{
    
    public static int[] productExceptSelf(int[] nums) {
        int[] answer = new int[nums.length];
        for(int i = 0; i<nums.length; i++)
        {
            int product = 1;
            for(int j = 0; j<nums.length; j++)
            {
                if(i!=j)
                {
                    product*=nums[j];
                
                }
            }
           answer[i]=product;

        }
        return answer;
    }

 public static void main(String[] args) {
     int inp[] ={2,3,4,5};
     int ans[] = new int[inp.length];
        ans = productExceptSelf(inp);
        for(int i : ans )
        {
            System.out.println(i);
        }
    }}