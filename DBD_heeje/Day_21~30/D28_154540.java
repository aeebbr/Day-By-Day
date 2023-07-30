// [Programmers] 154540. 무인도 여행
// 풀이 시간: 90 분

import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedList;
import java.util.Queue;

class Solution {
	//	전역에서 사용하는 변수를 모아서 선언
	public static int[] dy = {-1, 0, 1, 0};
	public static int[] dx = {0, -1, 0, 1};
	public static int R;
	public static int C;
	public static boolean[][] visited;
	
	//	maps를 전역으로 쓰고 싶은데 방법을 몰라서 cMaps를 만들어넣음. 이래도 되나?
	public static String[] cMaps;
	
  public int[] solution(String[] maps) {
  	R = maps.length;
  	C = maps[0].length();
  	visited = new boolean[R][C];
  	ArrayList<Integer> answer = new ArrayList<>();
  	cMaps = maps;

		// 완전 탐색, BFS
  	for (int i = 0; i < R; i++) {
  		for (int j = 0; j < C; j++) {
  			if (cMaps[i].charAt(j) != 'X' && !visited[i][j]) {
  				answer.add(bfs(i, j));
  			}
  		}
  	}
    
		// 섬이 없으면 -1 출력
    if (answer.size() == 0) {
        answer.add(-1);
    }
    
		// 정렬
  	Collections.sort(answer);
  	
		// ArrayList -> int[] 로 변환
  	int[] sortedAnswer = new int[answer.size()];
  	for (int i = 0; i < answer.size(); i++) {
  		sortedAnswer[i] = answer.get(i).intValue();
  	}
      
    return sortedAnswer;
  }
  
  public static int bfs(int sy, int sx) {
  	Queue<int[]> q = new LinkedList<>();
  	q.add(new int[] {sy, sx});
  	visited[sy][sx] = true;
		
		// char -> int
  	int sum = cMaps[sy].charAt(sx) - '0';
  	
  	while (!q.isEmpty()) {
  		int[] arr = q.poll();
  		for (int d = 0; d < 4; d++) {
  			int ny = arr[0] + dy[d];
  			int nx = arr[1] + dx[d];

  			
  			// 유효성 검사
  			if (ny < 0 || ny >= R || nx < 0 || nx >= C) continue;

        int island = cMaps[ny].charAt(nx);
  			if (!visited[ny][nx] && island != 'X') {
  				sum += Character.getNumericValue(island);
  				visited[ny][nx] = true;
  				q.add(new int[] {ny, nx});
  			}
  		}
  	}
  	
  	return sum;
  }
}