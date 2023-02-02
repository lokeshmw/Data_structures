package main

import "fmt"

type node struct {
	Data int
	next *node
}
type singleList struct {
	len  int
	head *node
	tail *node
}

func (s *singleList) Add(data int) {

	newnode := new(node)
	newnode.Data = data
	newnode.next = nil

	if s.head == nil {
		s.head = newnode
		s.tail = newnode
	} else if s.tail == nil {
		s.tail = newnode
		s.head.next = s.tail
	} else {
		s.tail.next = newnode
		s.tail = newnode
	}

}
func (s *singleList) pop() {
	temp := s.head
	for {
		if temp.next == s.tail {
			break
		}
		temp = temp.next
	}
	temp.next = nil
	s.tail = temp
}
func (s *singleList) display() {

	for temp := s.head; temp != nil; temp = temp.next {

		fmt.Println(temp.Data)
	}
}
func main() {
	s := singleList{}
	s.Add(34)
	s.Add(314)
	s.Add(334)
	s.Add(76)
	s.pop()
	s.display()
	s.pop()
	s.display()
}
