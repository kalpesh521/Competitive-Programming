public class EvenDigits {
    public static void main(String[] args) {
        int[] num = { 23, 2, 1, 223, 13232, 2222,22 };
        int res = findnum(num);
        //Total number of even digits numbers in array
        System.out.println(res);
        //Total number of digits in n
        System.out.println(digits(33215));
    }

    static int findnum(int[] nums) {
        int count = 0;
        for (int num : nums) {
            if (even(num)) {
                count++;
            }
        }
        return count;

    }

    // Function to check number even or odd
    static boolean even(int num) {
        int numOfdigits = digits(num);
        return (numOfdigits % 2) == 0;
    }



    // Another Function to count number of digits
    static int digits2(int num) {
        int count = 0;
        if (num < 0) {
            num = num * -1;
        }
        if (num == 0) {
            return 1;
        }

        while (num > 0) {
            count++;
            num = num / 10;
        }
        return count;
    }

    // Optimize Function to count number of digits
    static int digits(int num) {
        if (num < 0) {
            num = num * -1;
        }
        if (num == 0) {
            return 1;
        }
        return (int) (Math.log10(num)) + 1;//Important Find number of digits
    }
}
