import java.util.Arrays;

// Two reverse methods; both are O(n) however
// - reverseE() is practically slower requiring two iterations
// - reverseE() has a memory overhead of O(n) as it copies the array
// - reverseI() will be faster and has an O(1) memory overhead
//
// Integer is used rather than int to make printing easier in the
// main() method
public class ArrayReverse {

    public static void reverseE(Integer a[]){
        int n = a.length;
        Integer b[] = new Integer[n];
        for(int i=0; i<n; i++){
            b[i] = a[n-1-i];
        }
        for(int i=0; i<n; i++){
            a[i] = b[i];
        }
    }

    public static void reverseI(Integer a[]){
        int n = a.length;
        for(int i=0; i<n/2; i++){
            int tmp = a[i];
            a[i] = a[n-1-i];
            a[n-1-i] = tmp;
        }
        return;
    }

    // Demo uses
    public static void main(String args[]){
        Integer test1[] = {1,3,5,7,9,11,13};

        System.out.println(Arrays.asList(test1));
        reverseE(test1);
        System.out.println(Arrays.asList(test1));

        Integer test2[] = {1,3,5,7,9,11,13};
        System.out.println(Arrays.asList(test2));
        reverseI(test2);
        System.out.println(Arrays.asList(test2));
    }
}
