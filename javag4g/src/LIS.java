import java.util.Scanner;

/**
 * Created by sgu194 on 6/25/2017.
 */
public class LIS {

    public static void pain(String[] args) {
        Scanner sc = new Scanner(System.in);
        int cases = sc.nextInt();
        while (cases-- > 0){
            int size = sc.nextInt();
            int[] arr = new int[2*size];
            for (int i = 0; i < size; i++) {
                int value = sc.nextInt();
                arr[i] = value;
                arr[i+size] = value;
            }

           solution(arr);
        }
    }

    public static void main(String[] args) {
        int[] xrr = {87,78,16,94,36,87,93,50,22,63,28,91,60,64,27,41,27,73,37,12,69,68,30,83,31,63,24,68,36,30,3,23,59,70,68,94,57,12,43,30,74,22,20,85,38,99,25,16,71,14,27,92,81,57,74,63,71,97,82,6,26,85,28,37,6,47,30,14,58,25,96,83,46,15,68,35,65,44,51,88,9,77,79,89};
//        int[] xrr = {5, 6, 7, 1, 2, 3};
        int[] arr = new int[2*xrr.length];
        for (int i = 0; i < xrr.length; i++) {
            int value = xrr[i];
            arr[i] = value;
            arr[i+xrr.length] = value;
        }

        solution(xrr);

    }

    public static void solution(int[] brr) {
        int currSeq = 0;
        int maxSeq = 0;
//        System.out.println(Arrays.toString(brr));
        for (int i = 0; i < brr.length ; i++) {
            int index = i+1 < brr.length ? i+1 : 0;
            while(index != i) {
                if (brr[i] < brr[index]){
//                    System.out.println(brr[i] +" " +brr[index]);
                    currSeq++;
                }
                int next = index+1;
                index = next < brr.length ? next : next -brr.length;
            }

            maxSeq = currSeq > maxSeq ? currSeq : maxSeq;
            currSeq = 0;
        }

        System.out.println(maxSeq);

    }


}
