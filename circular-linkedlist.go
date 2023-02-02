package main

import "fmt"

type node struct {
	data int
	next *node
}
type circularLinkedList struct {
	head *node
	tail *node
}

func (c *circularLinkedList) AddFront(data int) {
	Newnode := &node{
		data: data,
		next: c.head,
	}
	if c.head == nil {
		Newnode.next = Newnode
		c.head = Newnode
		return
	}
	temp := c.head
	for temp.next != c.head {
		temp = temp.next
	}
	temp.next = Newnode
	c.head = Newnode
}
func (c *circularLinkedList) AddBack(data int) {
	Newnode := &node{
		data: data,
		next: c.head,
	}
	if c.head == nil {
		Newnode.next = Newnode
		c.head = Newnode
		return
	}
	temp := c.head
	for temp.next != c.head {
		temp = temp.next
	}
	temp.next = Newnode
}
func (c *circularLinkedList) DeleteFront() {
	if c.head == nil {
		fmt.Println("empty list")
	}
	temp := c.head
	for temp.next != c.head {
		temp = temp.next
	}
	if c.head == temp {
		c.head = nil
	} else {
		temp.next = c.head.next
		c.head = c.head.next
	}
}

func (c *circularLinkedList) DeleteBack() {
	if c.head == nil {
		fmt.Println("empty list")
	}
	temp := c.head
	for temp.next != c.head {
		temp = temp.next
	}
	if c.head == temp {
		c.head = nil
	} else {
		temp1 := c.head
		for temp1.next != temp {
			temp1 = temp1.next
		}
		temp1.next = c.head
		temp = temp1
	}
}
func (c *circularLinkedList) display() {
	if c.head == nil {
		fmt.Println("list is empty")
	}
	temp := c.head
	for temp.next != c.head {
		fmt.Println(temp.data)
		temp = temp.next
	}
	fmt.Println(temp.data)

}
func main() {
	c := circularLinkedList{}
	c.AddFront(2)
	c.AddFront(1)
	c.AddBack(3)
	c.display()
	c.DeleteBack()
	c.display()
}
