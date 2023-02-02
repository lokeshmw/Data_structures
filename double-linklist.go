package main

import "fmt"

type node struct {
	Data int
	next *node
	prev *node
}
type doublellinkList struct {
	len  int
	head *node
	tail *node
}

func (d *doublellinkList) Addfront(data int) {

	newnode := new(node)
	newnode.Data = data
	newnode.next = nil
	newnode.prev = nil

	if d.head == nil {
		d.head = newnode
		d.tail = newnode
	} else {
		newnode.next = d.head
		d.head.prev = newnode
		d.head = newnode
	}
}
func (d *doublellinkList) AddBack(data int) {

	newnode := new(node)
	newnode.Data = data
	newnode.next = nil
	newnode.prev = nil

	if d.head == nil {
		d.head = newnode
		d.tail = newnode
	} else {
		temp := d.head
		for temp.next != nil {
			temp = temp.next
		}
		newnode.prev = temp
		temp.next = newnode
		d.tail = newnode
	}
}

func (d *doublellinkList) pop() {
	temp := d.head
	for {
		if temp.next == d.tail {
			break
		}
		temp = temp.next
	}
	temp.next = nil
	d.tail = temp
}
func (d *doublellinkList) Removefront() {

	if d.head == nil {
		fmt.Println("list is empty")

	} else {
		temp := d.head
		d.head = temp.next
		temp.prev = nil
	}
}

func (d *doublellinkList) display() {
	if d.head == nil {
		fmt.Println("list is empty")
	}
	temp := d.head
	for temp != nil {
		fmt.Println(temp.Data)
		temp = temp.next
	}
}

func main() {
	d := doublellinkList{}
	d.Addfront(2)
	d.AddBack(3)
	d.Addfront(1)
	d.display()
	d.pop()
	d.display()
	d.Removefront()
	d.display()
}
