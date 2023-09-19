public class AVLBinarySearchTree <E extends Comparable<E> > {
    private Node root;
    
    private class Node {
        private E data;
        private int height;
        private Node left, right;

        public Node(E d) {
            data = d;
            height = 0;
        }
    }

    private int getHeight(Node node) {
        if (node == null) return -1;
        return node.height;
    }

    private int balanceFactor(Node node) {
    return (getHeight(node.left) - getHeight(node.right));

    }

    private Node balance(Node node) {
        // get node balance
        int balance = balanceFactor(node);

        if (balance > 1) {
            if (balanceFactor(node.left) < 0) {
                node.left = leftRotate(node.left);
            }
            return rightRotate(node);

        } else if (balance < -1) {
            if (balanceFactor(node.right) > 0) {
                node.right = rightRotate(node.right);
            }
            return leftRotate(node);
        } 
        return node;
    }

    private Node rightRotate(Node node) {
        Node temp = node.left;
        node.left = temp.right;    
        temp.right = node;

        node.height = 1 + Math.max(getHeight(node.left), getHeight(node.right));
        temp.height = 1 + Math.max(getHeight(temp.left), getHeight(temp.right));

        return temp;
    }
    private Node leftRotate(Node node) {
        Node temp = node.right;
        node.right = temp.left;
        temp.left = node;

        node.height = 1 + Math.max(getHeight(node.left), getHeight(node.right));
        temp.height = 1 + Math.max(getHeight(temp.left), getHeight(temp.right));

        return temp;
    }


    public void insert(E e) {
        root = insertRec(root, e);
    }
    private Node insertRec(Node node, E e) {
        if (node == null) {
            System.out.println(e + " was inserted as the node was null");
            node = new Node(e);
        } else if (e.compareTo(node.data) < 0) {
            node.left = insertRec(node.left, e);
        } else if (e.compareTo(node.data) > 0) {
            node.right = insertRec(node.right, e);
        }
        // set node height
        node.height = 1 + Math.max(getHeight(node.left), getHeight(node.right));

        return balance(node);
    }

    public static void main(String[] args) {
        AVLBinarySearchTree<Integer> tree = new AVLBinarySearchTree<>();
        tree.insert(50);
        tree.insert(100);
        tree.insert(75);
        tree.insert(150);
        tree.insert(10);
        tree.insert(20);
        tree.insert(15);
        tree.insert(5);
        tree.insert(1);
        tree.insert(2);
        tree.insert(3);
        System.out.println(tree.root.data);
    }
}
