import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class TheTimeInWords
{
    static final String[] numsInWordFormatUpToIncTwenty = new String[]{"one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "quarter", "sixteen", "seventeen", "eighteen", "nineteen", "twenty"};

    static String getTimeInWords(int hour, int min)
     {
        if (hour > 12 || min > 59)
        {
            throw new IllegalArgumentException("Hour should be <= 12 and minute should be <= 59");
        }

        if (min == 0)
        {
            return  getHourString(hour) + " o' clock";
        }

        return getFullTimeExpression(hour, min);
    }

    private static String getFullTimeExpression(int hour, int min)
    {
        String timePosition = "past ";
        String minuteCase = " minutes ";

        if (min == 15 || min == 45 || min == 30)
        {
            minuteCase = " ";  // Word "minutes" does not appear in expression "quarter to/past or half past"
        }

        if (min > 30)
        {
            // Example: "3 hours 40 minutes" will have the value of "20 to 4", so the hour and minutes need to be corrected
            hour += 1; // The value of the next hour is hour + 1
            min = 60 - min; // The minutes to the next hours are 60 (minutes) - min
            timePosition = "to ";
        }

        if (min == 1) // "min" can either be originally 1, or as a result of 59 subtracted from 60, that's why it is checked here
        {
            minuteCase = " minute ";
        }

        String hourWord = getHourString(hour);
        String minuteWord = getMinutesString(min);

        return minuteWord + minuteCase + timePosition + hourWord;
    }

    private static String getHourString(int hour)
    {
        return numsInWordFormatUpToIncTwenty[hour - 1]; // Correct the index, e.g., 3 is at index 2 in array numsInWordFormatUpToIncTwenty
    }

    private static String getMinutesString(int min)
    {
        if (min <= 20)
        {
            return numsInWordFormatUpToIncTwenty[min - 1];
        }

        if (min < 30)
        {
            int secondDigitInt = min % 20;
            String secondDigitString = numsInWordFormatUpToIncTwenty[secondDigitInt - 1];
            return "twenty " + secondDigitString;
        }
        else
        {
            return "half"; // If min is 30, the expression will be "half (past)"
        }
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int h = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        int m = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        String result = getTimeInWords(h, m);

        bufferedWriter.write(result);
        bufferedWriter.newLine();
        bufferedWriter.close();
        scanner.close();
    }
}
