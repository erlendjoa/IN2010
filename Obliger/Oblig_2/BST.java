import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

class BST {

    Node root;

    private class Node {
        int data;
        Node left;
        Node right;

        public Node(int data) {
            this.data = data;
            this.left = null;
            this.right = null;
        }
    }


    public BST() {
        this.root = null;
    }

    public void insert(int newData) {
        root = insertRec(root, new Node(newData));
    }

    private Node insertRec(Node node, Node newNode) {
        if (node == null) {
            node = newNode;
        } else if (newNode.data < node.data) {
            node.left = insertRec(node.left, newNode);
        } else if (newNode.data > node.data) {
            node.right = insertRec(node.right, newNode);
        }
        return node;
    }

    public boolean contains(int searchData) {
        return containRec(root, searchData);
    }

    private boolean containRec(Node node, int searchData) {
        if (node == null) {
            return false;
        }
        if (node.data == searchData) {
            return true;
        } else if (searchData < node.data) {
            return containRec(node.left, searchData);
        } else if (searchData > node.data) {
            return containRec(node.right, searchData);
        }
        return false;
    }

    public void remove(int data) {
        root = removeRec(root, data);
    }

    private Node removeRec(Node node, int data) {
        if (data < node.data) {
            node.left = removeRec(node.left, data);
        } else if (data > node.data) {
            node.right = removeRec(node.right, data);
        }

        if (node.data == data) {
            if (node.left == null) {
                return node.right;
            }
            if (node.right == null) {
                return node.left;
            }

            Node tempLeft = node.left;
            node = node.right;
            while (node.left != null) {
                node = node.left;
            }
            node.left = tempLeft;
        }
        return node;
    }
    

    public static void main(String[] args) {
        System.out.println(args[0]);
        try {
            FileReader fileReader = new FileReader(args[0]);
            BufferedReader bufferedReader = new BufferedReader(fileReader);

            String s = bufferedReader.readLine();
            String[] cmdArr = new String[Integer.parseInt(s)];
            bufferedReader.readLine();
            int i = -1;
            while (s != null) {
                cmdArr[i++] = s;
            }

        } catch (Exception e) {
            System.out.println("File not found.");
        }
        
    }
}