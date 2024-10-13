public class BinarySearch {
    public static int binarySearch(int[] arr, int NumberSearch) {
        int low = 0;
        int high = arr.length - 1;

        while (low <= high) {
            int mid = (low + high) / 2;

            
            if (arr[mid] == NumberSearch) {
                return mid; 
            }
            
            if (arr[mid] < NumberSearch) {
                low = mid + 1;
            }
            else {
                high = mid - 1;
            }
        }
        return -1; 
    }

    public static void main(String[] args) {

        int[] arr = {10, 3, 51, 7, 9, 11, 13, 15};

        // Element to search for
        int NumberSearch = 7;

        int result = binarySearch(arr, NumberSearch);


        if (result == -1) {
            System.out.println("Element not present in array");
        } else {
            System.out.println("Element found at index " + result);
        }
    }
}
