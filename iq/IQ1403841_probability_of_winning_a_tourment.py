def probability_of_winning_a_tourment(A):

    m = len(A)                                                            # number of teams
    n = int(math.log(m, 2))                                               # number of rounds
    rounds = [[0] * m for k in range(n + 1)]
    rounds[0] = [1] * m

    for k in range(n):                                                    # O(logN)

        members = 2 ** k                                                  # number of group members per round

        for i in range(m):                                                # O(N)

            group = i // members                                          # group index
            peer = [group + 1, group - 1][group % 2]                      # peer group index

            for j in range(peer * members, (peer + 1) * members):         # O(2^0), O(2^1) ... O(2^(logN-1))
                rounds[k + 1][i] += rounds[k][i] * A[i][j] * rounds[k][j]

    return rounds[n]
