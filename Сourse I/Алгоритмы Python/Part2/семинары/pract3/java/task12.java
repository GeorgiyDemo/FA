public class Solution {
    public static void recursion() {
        java.util.Scanner in = new java.util.Scanner(System.in);
        int n = in.nextInt();
        // Базовый случай 
        if (n > 0) {
            int m = in.nextInt();
            System.out.println(n);
            // Базовый случай 
            if (m > 0) {
                // Шаг рекурсии / рекурсивное условие
                recursion();
            }
        }
    }
    public static void main(String[] args) {
        recursion(); // вызов рекурсивной функции
    }
}