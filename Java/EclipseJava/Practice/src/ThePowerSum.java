import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;


public class ThePowerSum {
     static int powerSum(int total, int power, int base) 
     {
        int baseToPower = (int)Math.pow(base, power);

        if (baseToPower == total)
        {
            return 1;
        }    
        else if (baseToPower > total)
        {
            return 0;
        }
        else
        {
            return powerSum(total, power, base + 1) + powerSum(total - baseToPower, power, base + 1);
        }
     }
      
    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int X = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        int N = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");
        
        int base = 1;

        int result = powerSum(X, N, base);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedWriter.close();

        scanner.close();
    }
}
