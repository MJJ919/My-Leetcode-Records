/*
https://leetcode.com/problems/serialize-and-deserialize-n-ary-tree/
Refer to 297
*/
/*
Time:O(n)
Space:O(n)
*/
class Codec {
    // Encodes a tree to a single string.
    public String serialize(Node root) {
        List<String> res = new LinkedList<>();
        dfs(res, root);
        return String.join(",", res);
    }
    public void dfs(List<String> res, Node root){
        if (root==null) return;
        res.add(String.valueOf(root.val));
        res.add(String.valueOf(root.children.size()));
        for (Node child:root.children)    dfs(res, child);
    }
	
    // Decodes your encoded data to tree.
    public Node deserialize(String data) {
        if (data.equals(""))    return null;
        LinkedList<String> l = new LinkedList<>(Arrays.asList(data.split(",")));
        return dfs(l);
    }
    
    public Node dfs(LinkedList<String> l){
        Node root = new Node(Integer.valueOf(l.poll()), new List<Node>());
        for (int i=0; i<Integer.valueOf(l.poll()); i++){
            root.children.add(dfs(l));
        }
        return root;
    }
}
