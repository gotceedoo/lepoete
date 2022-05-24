func fallingSquares(positions [][]int) []int {

	X := make([]int, 0)

	for _, P := range positions {
		x1, h := P[0], P[1]
		X = append(X, x1)
		X = append(X, x1+h)
	}

	sort.Ints(X)

	res, N := make([]int, 0), len(positions)*2
	C, M := make([]bool, N*8), make([]int, N*8)

	for _, P := range positions {
		x1, h, x2 := P[0], P[1], P[0]+P[1]
		U, V, A := make([]int, 0), make([]int, 0), make([][3]int, 0)
		A = append(A, [3]int{1, 0, N - 1})

		for i := 0; i < len(A); {
			v, b, e := A[i][0], A[i][1], A[i][2]
			i++
			V = append(V, v)

			if x1 <= X[b] && X[e] <= x2 {
				U = append(U, M[v])
				C[v] = true
			} else {
				l, r, m := v*2, v*2+1, (b+e)/2
				if C[v] {
					M[l], M[r] = M[v], M[v]
					C[l], C[r] = true, true
					C[v] = false
				}
				if x1 < X[m] {
					A = append(A, [3]int{l, b, m})
				}
				if X[m] < x2 {
					A = append(A, [3]int{r, m, e})
				}
			}
		}

		H := 0

		for _, h := range U {
			if H < h {
				H = h
			}
		}

		H += h

		for _, v := range V {
			if M[v] < H {
				M[v] = H
			}
		}

		res = append(res, M[1])
	}

	return res
}
