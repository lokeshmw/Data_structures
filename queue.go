package main

import "fmt"

type Queue []int

func (q *Queue) Enqueue(data int) {
	*q = append(*q, data)
}
func (q *Queue) Dequeue() int {
	front := (*q)[0]
	*q = (*q)[1:]
	return front
}
func (q *Queue) Empty() bool {
	return len(*q) == 0
}
func main() {
	q := Queue{}
	q.Enqueue(1)
	q.Enqueue(2)
	fmt.Println(q.Dequeue())
	q.Enqueue(2)

}
