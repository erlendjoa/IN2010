public class UniquePaths  {
    int m;
    int n;

    public int uniquePaths(int m, int n) {
        this.m = m;
        this.n = n;
        return search(0, 0);
    }

    public int search(int x, int y) {
        if (x == m && y == n) {
            return 1;
        }
        int s = 0;
        if (!(x + 1 > m)) {
            s += search(x + 1, y);
        }
        if (!(y + 1 > n)) {
            s += search(x, y + 1);
        }
        System.out.println(s);
        return s;
    }

    public static void main(String[] args) {
        UniquePaths solution = new UniquePaths();
        int result = solution.uniquePaths(3, 7);
        System.out.println("Number of unique paths: " + result);
    }
}