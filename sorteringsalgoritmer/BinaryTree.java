

public class BinaryTree {
    Node root;
    
    private class Node {
        int n;
        Node left;
        Node right;

        private Node(int n) {
            this.n = n;
        }
    }

    public void insert(int data) {
        root = insertRecursive(root, new Node(data));
    }
    private Node insertRecursive(Node root, Node node) {
        if (root == null) {
            root = node;
            return node;
        } else if (node.n < root.n) {
            root.left = insertRecursive(root.left, node);
        } else {
            root.right = insertRecursive(root.right, node);
        }
        return root;
    }

    public void display() {
        displayRecursive(root);
    }
    private void displayRecursive(Node root) {
        if (root != null) {
            displayRecursive(root.left);
            System.out.println(root.n);
            displayRecursive(root.right);
        }
    }

    public boolean search(int data) {
        return searchRecursive(root, data);
    }
    private boolean searchRecursive(Node node, int data) {
        if (root == null) {
            return false;
        }
    }

    public static void main(String[] args) {
        BinaryTree tree = new BinaryTree();
        tree.insert(5);
        tree.insert(1);
        tree.insert(3);
        tree.insert(7);
        tree.insert(6);
        tree.insert(4);
        tree.display();
    }
}
