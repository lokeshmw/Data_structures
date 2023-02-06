package main

import "fmt"

type Stack []int

func (s *Stack) Push(v int) {
	*s = append(*s, v)
}

func (s *Stack) Pop() int {
	l := len(*s)
	top := (*s)[l-1]
	*s = (*s)[:l-1]
	return top
}
func (s *Stack) Top() int {
	l := len(*s)
	return (*s)[l-1]
}
func (s *Stack) Empty() bool {
	return len(*s) == 0
}
func main() {
	s := Stack{}
	s.Push(1)
	s.Push(2)
	fmt.Println(s.Top())
	s.Pop()
	fmt.Println(s.Top())
}
