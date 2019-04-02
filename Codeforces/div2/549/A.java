import java.util.*;
import java.io.*;

public class A {
    private static int min(int a, int b) {
	return a > b ? b : a;
    }
    
    public static void main(String[] args) {
	Scanner s = new Scanner(System.in);
	int N = s.nextInt();

	Queue<Integer> left = new LinkedList<Integer>();
	Queue<Integer> right = new LinkedList<Integer>();
	
	for(int i=0; i<N; ++i) {
	    int door = s.nextInt();
	    if (door == 0)
		left.offer(i+1);
	    else
		right.offer(i+1);
	}

	boolean flag = false;
	int ans = 97653312;
	while(true) {
	    int left_idx = left.poll();
	    int right_idx = right.poll();

	    if (left.isEmpty()) {
		ans = min(left_idx, ans);
		flag = true;
	    }

	    if (right.isEmpty()) {
		ans = min(right_idx, ans);
		flag = true;
	    }

	    if (flag) {
		System.out.println(ans);
		return;
	    }
 	}
    }
}
