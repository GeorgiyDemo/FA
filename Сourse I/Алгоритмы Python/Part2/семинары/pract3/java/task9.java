public class Solution {
    public static int recursion() {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        // Базовый случай 
        if (n == 1) {
            int m = in.nextInt();
            // Базовый случай 
            if (m == 1) {
                // Шаг рекурсии / рекурсивное условие
                return recursion() + n + m;
            } else {
                int k = in.nextInt();
                // Базовый случай 
                if (k == 1) {
                    // Шаг рекурсии / рекурсивное условие
                    return recursion() + n + m + k;
                } else {
                    return n + m + k;
                }
            }
        } else {
            int m = in.nextInt();
            // Базовый случай 
            if (m == 1) {
                // Шаг рекурсии / рекурсивное условие
                return recursion() + n + m;
            } else {
                return n + m;
            }
        }
    }
    public static void main(String[] args) {
        System.out.println(recursion()); // вызов рекурсивной функции
    }
}