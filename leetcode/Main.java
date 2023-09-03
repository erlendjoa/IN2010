public class Main {
    public static void main(String[] args) {
        UniquePaths solution = new UniquePaths();
        int result = solution.uniquePaths(3, 7);
        System.out.println("Number of unique paths: " + result);
    }
}