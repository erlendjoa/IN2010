

class Set {
    private String[] set;

    Set(int size) {
        set = new String[size];
    }
    private int hash(String s, int N) {
        return s.length();
    }
    /*
    private int hash(String s, int N) {
        int h = 0;
        for (int i = 0; i < s.length(); i++) {
            h = 31*h + (int) s.charAt(i);
        }
        return h%N;
    }
    */
    public void insert(String s) {
        set[hash(s, set.length)] = s;
    }
    public boolean contains(String s) {
        return set[hash(s, set.length)] != null;
    }
    
    public static void main(String[] args) {
        Set s = new Set(10);
        s.insert("hei");
        System.out.println(s.contains("hei"));
    }
}