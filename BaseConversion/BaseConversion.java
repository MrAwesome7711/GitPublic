import java.util.Scanner;

/**
 * Program to convert numbers of one base to another base
 * 
 * Author: Nathan Walker
 * Date: 1-24-23
 */

public class BaseConversion 
{
    public static void main(String[] args)
    {
        int inputBase = 0;
        int outputBase = 0;
        String inputNumber;
        String answer;
        Scanner in = new Scanner(System.in);
        
        System.out.printf("Enter an input base (between 2 and 36): ");
        inputBase = in.nextInt();
        System.out.printf("Enter an input number: ");
        inputNumber = in.next();
        System.out.printf("Enter an output base (between 2 and 36): ");
        outputBase = in.nextInt();
        in.close();
        
        if (inputBase == 10)
        {
            answer = tenToNot(outputBase, inputNumber);
        }
        else if (outputBase == 10)
        {
            answer = notToTen(inputBase, inputNumber);
        }
        else
        {
            answer = tenToNot(outputBase, notToTen(inputBase, inputNumber));
        }
        
        System.out.printf("Result: %s%n", answer);
        
        
    }
    

    public static String notToTen(int base, String input)
    {
        int result=0;
        int num = 0;
        String alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        
        for (int i=0; i<input.length(); i++)
        {
          if (input.charAt(i) == '0' || input.charAt(i) == '1' || input.charAt(i) == '2' || input.charAt(i) == '3' || input.charAt(i) == '4'
              || input.charAt(i) == '5' || input.charAt(i) == '6' || input.charAt(i) == '7' || input.charAt(i) == '8' || input.charAt(i) == '9')
          {
              num = Integer.parseInt(input.charAt(i)+"");
          }
          else
          {
              num = alpha.indexOf(input.charAt(i))+10;
          }
            
           result += (num*Math.pow(base, input.length()-i-1));
        }
        return result+"";
    }
    
    public static String tenToNot(int base, String input)
    {
        int num = Integer.parseInt(input);
        int remainder = 0;
        String result = "";
        String alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        
        while (num != 0)
        {
             remainder = num % base;
             num = (num-remainder)/base;
             
             if (remainder < 10)
             {
                result = remainder + result;
             }
             else
             {
                 result = alpha.charAt(remainder-10)+ result;
             }
        }
        
        return result;
    }
}
