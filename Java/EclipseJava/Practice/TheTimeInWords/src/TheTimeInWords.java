import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;
import java.text.DecimalFormat;

public class TheTimeInWords {
	
	static final String[] singleDigits = new String[]{ "", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
	static final String[] twoDigits = new String[]{"ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"};

    // Complete the timeInWords function below.
    static String timeInWords(int h, int m)
    {
    	if (m == 0 || m == 15 || m == 30 || m == 45)
    	{
    		return getMultipleOf15MinutesWithHour(h, m);
    	}
    	 
    	return getFullTimeExpression(h, m);
    
    }
    
    private static String getFullTimeExpression(int h, int m)
    {	
    	int correctedHour = h;
    	int correctedMinute = m;
    	String timePosition = "past ";
    	String minuteCase = " minutes ";
    	
    	if (m > 30)
    	{
    		// Example: "3 hours 40 minutes" will have the value of "20 to 4", so the hour and minutes need to be corrected accordingly
    		correctedHour = h + 1; // The value of the next hour is h + 1
    		correctedMinute = 60 - m; // The minutes to the next hours are 60 (minutes) - m
    		timePosition = "to ";
    	}
    	
    	if (correctedMinute == 1)
		{
			minuteCase = " minute ";
		}
	
    	
    	String hour = getHourString(correctedHour);
    	String minute = getMinutesString(correctedMinute);
    	
    	return minute + minuteCase + timePosition + hour;
    }
    
    private static String getHourString(int h)
    {
    	String hourInWord;
    	
    	if (h <= 9)
    	{
    	    hourInWord = singleDigits[h];
    	}
    	else
    	{
    		hourInWord = twoDigits[h % 10];
    	}
    	
    	return hourInWord;
    }
    
    private static String getMinutesString(int m)
    {
    	String minuteInWord;
    	
    	if (m <= 9)
    	{
    		minuteInWord = singleDigits[m];
    	}
    	else
    	{
    		if (m < 20)
    		{
    			minuteInWord = twoDigits[m % 10];
    		}
    		else
    		{
    			int secondDigitInt = m % 20;
    			String secondDigitString = singleDigits[secondDigitInt];
    			minuteInWord = "twenty " + secondDigitString;
    		}
    	}
    	
    	return minuteInWord;
    }
    
    private static String getMultipleOf15MinutesWithHour(int h, int m)
    {
    	String minuteInWords = "";
    	int correctedHour = h;
    	
    	if (m == 0)
    	{
    		return getHourString(h) + " o' clock";
    	}
    	else if (m == 15)
    	{
    		minuteInWords = "quarter past ";
    	}
    	else if (m == 30)
    	{
    		minuteInWords = "half past ";
    	}
    	else if (m == 45)
    	{
    		minuteInWords = "quarter to ";
    		correctedHour += 1;
    	}
    	
    	return minuteInWords + getHourString(correctedHour);
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        int h = 1;
        int m = 00;

        String result = timeInWords(h, m);
        System.out.println(result);

        scanner.close();
    }
}
