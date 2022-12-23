package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	var h, x, c int

	_, _ = fmt.Fscanf(reader, "%d %d", &h, &x)

	m := 1
	mod := 1000000007
	res := 0

	for i := 0; i < h; i++ {
		m *= x
		m %= mod
		_, _ = fmt.Fscan(reader, &c)
		res += c * m
		res %= mod
	}

	fmt.Println(res)
}
