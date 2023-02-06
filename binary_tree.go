package main

import (
	"fmt"
)

type Node struct {
	element int
	left    *Node
	right   *Node
}

func insert(n *Node, element int) *Node {
	if n == nil {
		return &Node{element: element}
	}
	if element < n.element {
		n.left = insert(n.left, element)
	} else {
		n.right = insert(n.right, element)
	}
	return n
}
func InOrder(n *Node) {
	if n == nil {
		return
	}
	InOrder(n.left)
	fmt.Println(n.element)
	InOrder(n.right)

}
func preOrder(n *Node) {
	if n == nil {
		return
	}
	fmt.Println(n.element)
	preOrder(n.left)
	preOrder(n.right)
}
func postOrder(n *Node) {
	if n == nil {
		return
	}
	postOrder(n.left)
	postOrder(n.right)
	fmt.Println(n.element)
}
func count(n *Node) int {
	if n == nil {
		return 0
	}
	return 1 + count(n.left) + count(n.right)
}
func height(n *Node) int {
	if n == nil {
		return 0
	}
	return 1 + max(height(n.left), height(n.right))
}
func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func main() {
	root := &Node{element: 50}
	insert(root, 30)
	insert(root, 20)
	insert(root, 40)
	insert(root, 70)
	insert(root, 60)
	insert(root, 80)

	fmt.Println("In-order traversal:")
	InOrder(root)
	fmt.Println()

	fmt.Println("Pre-order traversal:")
	preOrder(root)
	fmt.Println()

	fmt.Println("Post-order traversal:")
	postOrder(root)
	fmt.Println()

	fmt.Println("Number of nodes:", count(root))
	fmt.Println("Height of the tree:", height(root))
}
