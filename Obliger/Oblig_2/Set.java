import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

class Set {

    Node root;
    int size = 0;

    private class Node {
        int data;
        Node left, right;;
        int height;

        public Node(int data) {
            this.data = data;
            this.left = null;
            this.right = null;
        }
    }
    private Set() {
        this.root = null;
    }

    private void setHeight(Node node) {
        node.height = (1 + Math.max(getHeight(node.left), getHeight(node.right)));
    }
   private int getHeight(Node node) {
        if (node == null) return -1;
        return node.height;
    }  
    private int balanceFactor(Node node) {
        return (getHeight(node.left) - getHeight(node.right));
    }
    private Node balance(Node node) {
        int balance = balanceFactor(node);
        if (balance > 1) {
            if (balanceFactor(node.left) < 0) {
                node.left = leftRotate(node.left);
            }
            return rightRotate(node);
        }
        else if (balance < -1) {
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

        setHeight(node);
        setHeight(temp);

        return temp;
    }
    private Node leftRotate(Node node) {
        Node temp = node.right;
        node.right = temp.left;
        temp.left = node;

        setHeight(node);
        setHeight(temp);

        return temp;
    }

    public void insert(int newData) {
        root = insertRec(root, new Node(newData));
    }

    private Node insertRec(Node node, Node newNode) {
        if (node == null) {
            node = newNode;
            size++;
        } else if (newNode.data < node.data) {
            node.left = insertRec(node.left, newNode);
        } else if (newNode.data > node.data) {
            node.right = insertRec(node.right, newNode);
        }
        setHeight(node);
        return balance(node);
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
        if (node == null) return null;
        
        if (data < node.data) {
            node.left = removeRec(node.left, data);
        } else if (data > node.data) {
            node.right = removeRec(node.right, data);
        }
        if (node.data == data) {
            size--;
            if (node.left == null) {
                return node.right;
            }
            if (node.right == null) {
                return node.left;
            }
            // Find min to the right
            Node leftmost = node.right;
            while (leftmost.left != null) {
                leftmost = leftmost.left;
            }
            node.data = leftmost.data;
            size++;
            node.right = removeRec(node.right, leftmost.data);
            
        }
        return node;
    }

    public int size() {
        return size;
    }

    public static void main(String[] args) {
        if (args.length < 1) {
            System.out.println("Usage: java CommandFileReader <file_path>");
            return;
        }

        String filePath = args[0]; // Get the file path from command-line arguments

        try {
            FileReader fileReader = new FileReader(filePath);
            BufferedReader bufferedReader = new BufferedReader(fileReader);

            String s = bufferedReader.readLine();
            int arraySize = Integer.parseInt(s); // Parse the first line as the array size
            String[] cmdArr = new String[arraySize];

            int i = 0; // Initialize the array index to 0

            // Read lines from the file and store them in the array
            while ((s = bufferedReader.readLine()) != null && i < arraySize) {
                cmdArr[i] = s;
                i++;
            }

            // Close the BufferedReader and FileReader
            bufferedReader.close();
            fileReader.close();


            Set set = new Set();

            for (String cmd : cmdArr) {
                if (cmd.charAt(0) == 's') {
                    System.out.println(set.size());
                } else if (cmd.charAt(0) == 'c') {
                    System.out.println(set.contains(Integer.parseInt(cmd.split(" ")[1])));
                } else if (cmd.charAt(0) == 'i') {
                    set.insert(Integer.parseInt(cmd.split(" ")[1]));
                } else if (cmd.charAt(0) == 'r') {
                    set.remove(Integer.parseInt(cmd.split(" ")[1]));
                }
            }

        } catch (IOException e) {
            System.out.println("File not found or error reading the file.");
        } catch (NumberFormatException e) {
            System.out.println("Invalid array size in the file.");
        }
    }

}