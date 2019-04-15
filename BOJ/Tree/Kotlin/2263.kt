import java.util.Scanner

fun inferPreorder(inorder: Array<Int>,
				  postorder: Array<Int>,
				  inorderRemember: Array<Int>,
				  inorderLeft: Int,
				  inorderRight: Int,
				  postorderLeft: Int,
				  postorderRight: Int,
				  size: Int) {
	if( size <= 0 )
		return 

	print(postorder[postorderRight])
	print(" ")

	val pivot = inorderRemember[postorder[postorderRight]]
	val leftTreeSize = pivot - inorderLeft
	val rightTreeSize = inorderRight - pivot
	inferPreorder(inorder, postorder, inorderRemember, 
				  inorderLeft, pivot - 1, postorderLeft, postorderLeft+leftTreeSize-1, leftTreeSize)
	inferPreorder(inorder, postorder, inorderRemember, 
				  pivot + 1, inorderRight, postorderLeft + leftTreeSize, postorderRight-1, rightTreeSize) 
}

fun main(args: Array<String>) = with(Scanner(System.`in`)) {
	val n = nextInt()

	var inorder = Array(n+2) { 0 }
	var postorder = Array(n+2) { 0 }

	var inorderRemember = Array(n+2) { 0 }

	for (i in 1..n) {
		inorder[i] = nextInt()
		inorderRemember[inorder[i]] = i
	}

	for (i in 1..n) {
		postorder[i] = nextInt()
	}

	inferPreorder(inorder, postorder, inorderRemember, 1, n, 1, n, n)
}
