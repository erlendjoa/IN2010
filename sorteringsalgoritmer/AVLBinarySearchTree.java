public class AVLBinarySearchTree <E extends Comparable<E> > {
    private Node root;
    
    private class Node {
        private E data;
        private int height;
        private Node left, right;

        public Node(E d) {
            data = d;
            height = 1;
        }
    }
    private int getHeight(Node node) {
        if (node == null) return 0;
        return node.height;
    }
    private int getBalance(Node node) {
        if (node == null) return 0;
        return (getHeight(node.left) - getHeight(node.right));
    }
    private Node rightRotate(Node node) {
        Node temp = node.left;
        node.left = temp.right;    
        temp.right = node;
        return temp;
    }
    private Node leftRotate(Node node) {
        Node temp = node.right;
        node.right = temp.left;
        temp.left = node;
        return temp;
    }


    public void insert(E e) {
        root = insertRec(root, e);
    }
    private Node insertRec(Node node, E e) {
        if (node == null) {
            System.out.println(e + " was inserted as the node was null");
            return new Node(e);
        } else if (e.compareTo(node.data) < 0) {
            node.left = insertRec(node.left, e);
        } else if (e.compareTo(node.data) > 0) {
            node.right = insertRec(node.right, e);
        }
        node.height = 1 + Math.max(getHeight(node.left), getHeight(node.right));

        int balance = getBalance(node);
        if (balance > 1) {
            if (e.compareTo(node.left.data) < 0) {
                System.out.println("RR");
                return rightRotate(node);
  
            } else {
                System.out.println("LR");
                node.left = leftRotate(node.left);
                return rightRotate(node);
            }

        } else if (balance < -1) {
            System.out.println(balance);
            
            if (e.compareTo(node.right.data) > 0) {
                System.out.println("LL");
                return leftRotate(node);

            } else {
                System.out.println("RL");
                node.right = rightRotate(node.right);
                return leftRotate(node);
            }
            
        } 
        return node;
    }

    public static void main(String[] args) {
        AVLBinarySearchTree<Integer> tree = new AVLBinarySearchTree<>();
        tree.insert(10);
        System.out.println("ROOT: " + tree.root.data);
        tree.insert(20);
        System.out.println("ROOT: " + tree.root.data);
        tree.insert(15);
        System.out.println("ROOT: " + tree.root.data);
        tree.insert(3);
        System.out.println("ROOT: " + tree.root.data);
        tree.insert(5);
        System.out.println("ROOT: " + tree.root.data);
        tree.insert(1);
        System.out.println("ROOT: " + tree.root.data);
        tree.insert(30);
        System.out.println("ROOT: " + tree.root.data);
    }
}