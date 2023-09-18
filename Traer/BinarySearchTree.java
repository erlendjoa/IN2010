

public class BinarySearchTree {
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
    private Node insertRecursive(Node cr, Node node) {
        if (cr == null) {
            cr = node;
        } else if (node.n < cr.n) {
            cr.left = insertRecursive(cr.left, node);
        } else {
            cr.right = insertRecursive(cr.right, node);
        }
        return cr;
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
        if (node == null) {
            return false;
        } else if (node.n == data) {
            return true;
        } else if (node.n > data) {
            return searchRecursive(node.left, data);
        } 
        return searchRecursive(node.right, data);
    }

    public void remove(int data) {
        if (search(data)) {
            root = removeRecursive(root, data, root);
        }
    }

    public Node removeRecursive(Node node, int data, Node parent) {
        if (node == null) {
            return node;
        } else if (data < node.n) {
            node.left = removeRecursive(node.left, data, node);
        } else if (data > node.n) {
            node.right = removeRecursive(node.right, data, node);
        } else {
            // if node has no children:
            if (node.left == null && node.right == null) {
                node = null;
            // if node has right or both child:
            } else if (node.right != null) {
                node.n = successor(node);
                node.left = removeRecursive(node.left, node.n, node);
            // if node has only left child
            } else {
                node.n = predecessor(node);
                node.left = removeRecursive(node.left, node.n, node);
            }
        }
        return node;
    }   

    public int successor(Node node) {
        node = node.right;
        // go as far left to find the most similar/smallest int
        while (node.left != null) {
            node = node.left;
        }
        return node.n;
    }

    public int predecessor(Node node) {
        node = node.left;
        // go as far right to find the most similar/biggest int
        while (node.right != null) {
            node = node.right;
        }
        return node.n;
    }

    public static void main(String[] args) {
        BinarySearchTree tree = new BinarySearchTree();
        tree.insert(5);
        tree.insert(1);
        tree.insert(3);
        tree.insert(7);
        tree.insert(6);
        tree.insert(4);
        tree.remove(1);
        tree.remove(6);
        tree.display();
        System.out.println(tree.search(1));
        System.out.println(tree.search(7));
        System.out.println(tree.search(8));
    }
}
