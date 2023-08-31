public class Teque<E> {

    Node first;
    Node last;
    Node middle;

    private class Node {
        Integer n;
        Node next;
        Node prev;
        public Node(Integer n) {
            this.n = n;
        }
    }

    public Teque() {
        
    }

    
}
