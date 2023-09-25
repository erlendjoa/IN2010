import java.util.Set;
import java.util.HashSet;
import java.util.ArrayList;

public class DFS<E> {
    Set<E> V;
    Set<Set<E>> E;
    Set<E> visited;
    isFound = false;

    public DFS(Set<E> allu, Set<Set<E>> allv) {
        V = allu;
        E = allv;
    }

    public boolean DFSFull(E elem) {
        isFound = false;
        visited = new HashSet<>();

        for (E v : V) {
            if (!visited.contains(v)) {
                DFSVisit(v, elem);
            }
        }
        return isFound;
    }

    public boolean DFSVisit(E u, E elem) {
        if (u.equals(elem)) {
            isFound = true;
        }
        visited.add(u);
        for (Set<E> set : E) {
            ArrayList<E> arrSet = new ArrayList<>(set);
            E v = arrSet.get(1);
            if (!visited.contains(v)) {
                DFSVisit(v, elem);
            }
        }
    }


    public static void main(String[] args) {
        Set<String> V = new HashSet<>();
        Set<Set<String>> E = new HashSet<>();

        V.add("A");
        V.add("B");
        V.add("C");
        V.add("D");
        
        Set<String> e1 = new HashSet<>();
        e1.add("A");
        e1.add("B");

        Set<String> e2 = new HashSet<>();
        e2.add("B");
        e2.add("C");

        Set<String> e3 = new HashSet<>();
        e3.add("C");
        e3.add("D");


        E.add(e1);
        E.add(e2);
        E.add(e3);

        DFS<String> dfs = new DFS<>(V, E);
        System.out.println(dfs.DFSFull("A"));
    }
}
