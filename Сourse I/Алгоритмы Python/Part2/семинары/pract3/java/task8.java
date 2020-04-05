public class Solution {
    public static void recursion(int max1, int max2) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        // Базовый случай
        if (n > 0) {
            // Шаг рекурсии / рекурсивное условие
            if (max1 < n) {
                recursion(n, max1);
            } // Шаг рекурсии / рекурсивное условие
            else if (max2 < n) {
                recursion(max1, n);
            } // Шаг рекурсии / рекурсивное условие
            else {
                recursion(max1, max2);
            }
        } else {
            System.out.println(max2);
        }
    }
    public static void main(String[] args) {
        recursion(0, 0); // вызов рекурсивной функции
    }
}