import java.io.*;
import java.math.*;
import java.util.*;

public class FibonacciModified
{
    static BigInteger fibonacciModified(int t1, int t2, int n) 
    {
        BigInteger firstNum = BigInteger.valueOf(t1);
        BigInteger secondNum = BigInteger.valueOf(t2);
        BigInteger fibNum = BigInteger.valueOf(0);
 
        for (int i = 0; i < n - 2; i++)
        {
            fibNum = firstNum.add(secondNum.multiply(secondNum));
            firstNum = secondNum;
            secondNum = fibNum;
        }

        return fibNum;
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        String[] t1T2n = scanner.nextLine().split(" ");

        int t1 = Integer.parseInt(t1T2n[0]);

        int t2 = Integer.parseInt(t1T2n[1]);

        int n = Integer.parseInt(t1T2n[2]);

        BigInteger result = fibonacciModified(t1, t2, n);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedWriter.close();

        scanner.close();
    }
}
