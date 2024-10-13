public class LinearSearch {
    
    public static int LinearSearch(int[] arr, int NumToSearch) {
        // Traverse the array
        for (int i = 0; i < arr.length; i++) {
            
            if (arr[i] == NumToSearch) {
                return i;
            }
        }
        return -1;
    }

    public static void main(String[] args) {

        int[] arr = {10,5,1,4,90,35};
        
        // Element to search for
        int NumToSearch = 1;
        
        
        int result = LinearSearch(arr, NumToSearch);
        
        // Output
        if (result == -1) {
            System.out.println("Element not present!");
        } else {
            System.out.println("Element found at index " + result);
        }
    }
}
