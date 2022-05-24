func fallingSquares(positions [][]int) []int {

	X := make([]int, 0)

	for _, P := range positions {
	
		x1, x2 := P[0], P[0] + P[1]
		
		X = append(X, x1)
		X = append(X, x2)
	}

	sort.Ints(X)

	res, N := make([]int, 0), len(positions)*2
	C, M := make([]bool, N*8), make([]int, N*8)

	for _, P := range positions {
	
		x1, h, x2, H, U := P[0], P[1], P[0]+P[1], 0, 1
		V, A := make([]int, 0), make([][3]int, 0)
		
		A = append(A, [3]int{U, 0, N - 1})

		for i := 0; i < len(A); i++ {
		
			v, b, e := A[i][0], A[i][1], A[i][2]
			
			V = append(V, v)

			if x1 <= X[b] && X[e] <= x2 {	
                if H < M[v] { H = M[v] }
				C[v] = true
				
			} else {
			
				l, r, m := v*2, v*2+1, (b+e)/2
		
				if C[v] {
					M[l], M[r] = M[v], M[v]
					C[l], C[r] = true, true
					C[v] = false
				}
				if x1 < X[m] { A = append(A, [3]int{l, b, m}) }
				if X[m] < x2 { A = append(A, [3]int{r, m, e}) }
			}
		}

		H += h
		for _, v := range V { if M[v] < H { M[v] = H } }
		res = append(res, M[U])
	}

	return res
}
