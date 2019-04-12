import java.util.Scanner

typealias Data = Long
typealias Index = Int

fun initTree(source: Array<Data>,
			 tree: Array<Data>,
			 node: Index,
			 left: Index,
			 right: Index) {
	if (left == right) {
		tree[node] = source[left] 
		return
	} 

	val mid = (left + right) shr 1
	initTree(source, tree, node shl 1, left, mid)
	initTree(source, tree, (node shl 1) + 1, mid + 1, right)
	tree[node] = tree[node shl 1] + tree[(node shl 1) + 1]
}

fun updateTree(tree: Array<Data>, node: Index,
			   left: Index, right: Index, index: Index, value: Data) {
	if (left == right) {
		tree[node] = value
		return 
	}

	val mid = (left + right) shr 1
	if (index <= mid) {
		updateTree(tree, node shl 1, left, mid, index, value)
	} else {
		updateTree(tree, (node shl 1) + 1, mid + 1, right, index, value)
	}
	tree[node] = tree[node shl 1] + tree[(node shl 1) + 1]
}

fun query(tree: Array<Data>, node: Index,
		  leftRange: Index, rightRange: Index, left: Index, right: Index) : Data {
	if (leftRange > right || rightRange < left)
		return 0
	else if (leftRange >= left && rightRange <= right)
		return tree[node]
	
	val mid = (leftRange + rightRange) shr 1
	return query(tree, node shl 1, leftRange, mid, left, right) + 
			query(tree, (node shl 1) + 1, mid + 1, rightRange, left, right)
}

fun main(args: Array<String>) = with(Scanner(System.`in`)) {
	var tree = Array(4096) { 0 }
	var arr = Array(2048) { 0 }

	val n = nextInt()
	val q = nextInt()

	for (i in 1..n) {
		arr[i] = nextLong()
	}

	initTree(arr, tree, 1, 1, n)

	for (i in 1..q) {
		val c = nextInt()

		if (c == 1) {
			var a = nextInt()
			var b = nextInt()

			var tmpA = arr[a]
			var tmpB = arr[b]

			println(query(tree, 1, 1, n, a, b))
			updateTree(tree, 1, 1, n, a, tmpB)
			updateTree(tree, 1, 1, n, b, tmpA)

			arr[b] = tmpA
			arr[a] = tmpB
		} else {
			var a = nextInt()
			var b = nextInt()
			
			var d = nextInt()
			var e = nextInt()

			println(query(tree, 1, 1, n, a, b) - query(tree, 1, 1, n, d, e))
		}
	}
}
