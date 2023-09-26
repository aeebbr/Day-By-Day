# [BOJ] 1855. 영준이의 진짜 BFS
# 풀이 시간 : 00 분

import java.io.*;
import java.util.*;
 
public class Solution {
    private static int N;
    private static long result;
 
    private static int[] depths;
    private static int[][] parents;
    private static ArrayList<ArrayList<Integer>> adjList;
    private static List<Integer> searchList;
 
    private static final int MAX_DEPTH = 18;
 
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st;
 
        searchList = new ArrayList<>();
 
        int T = Integer.parseInt(br.readLine());
        for (int t = 1; t <= T; t++) {
            sb.append('#').append(t).append(' ');
 
            N = Integer.parseInt(br.readLine());
            init();
 
            st = new StringTokenizer(br.readLine());
            for (int i = 2; i <= N; i++) {
                int nodeNum = Integer.parseInt(st.nextToken());
                adjList.get(i).add(nodeNum);
                adjList.get(nodeNum).add(i);
            }
 
            BFS(1, 0);
            setParent();
 
            int size = searchList.size();
            for (int i = 0; i < size - 1; i++) {
                int node1 = searchList.get(i);
                int node2 = searchList.get(i + 1);
                int sameParent = LCA(node1, node2);
 
                result += depths[node1] - depths[sameParent];
                result += depths[node2] - depths[sameParent];
            }
 
            sb.append(result).append('\n');
        }
 
        bw.write(sb.toString());
        bw.close();
    } // End of main
 
    private static void BFS(int vertex, int depth) {
        Queue<Integer> que = new LinkedList<>();
        boolean[] isVisited = new boolean[N + 1];
        que.offer(vertex);
 
        while (!que.isEmpty()) {
            int pollNode = que.poll();
            isVisited[pollNode] = true;
            searchList.add(pollNode);
 
            int size = adjList.get(pollNode).size();
            for (int i = 0; i < size; i++) {
                int child = adjList.get(pollNode).get(i);
 
                if (isVisited[child]) continue;
 
                parents[child][0] = pollNode;
                depths[child] = depths[pollNode] + 1;
                que.offer(child);
            }
        }
    } // End of BFS
 
    private static int LCA(int node1, int node2) {
        if (depths[node1] < depths[node2]) {
            int temp = node1;
            node1 = node2;
            node2 = temp;
        }
 
        for (int i = MAX_DEPTH; i >= 0; i--) {
            long diff = depths[node1] - depths[node2];
            if (diff >= (1L << i)) {
                node1 = parents[node1][i];
            }
        }
 
        if (node1 == node2) {
            return node1;
        }
 
        for (int i = MAX_DEPTH; i >= 0; i--) {
            if (parents[node1][i] != parents[node2][i]) {
                node1 = parents[node1][i];
                node2 = parents[node2][i];
            }
        }
 
        return parents[node1][0];
    }
 
    private static void setParent() {
        for (int i = 1; i <= MAX_DEPTH; i++) {
            for (int j = 1; j <= N; j++) {
                int halfParent = parents[j][i - 1];
                parents[j][i] = parents[halfParent][i - 1];
            }
        }
    }
 
    private static void init() {
        parents = new int[N + 1][MAX_DEPTH + 1];
        depths = new int[N + 1];
        result = 0;
        adjList = new ArrayList<>();
        for (int i = 0; i <= N; i++) {
            adjList.add(new ArrayList<>());
        }
        searchList.clear();
    }
}