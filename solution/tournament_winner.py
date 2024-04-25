def tournamentWinner(competitions, results):
    wins = {}

    for index in range(len(competitions)):
        result = results[index]
        team = competitions[index]
        winner = team[1] if result == 0 else team[0]
        if winner in wins:
            wins[winner] += 1
        else:
            wins[winner] = 1

    max_wins = float('-inf')
    max_winner = ''
    for winner in wins:
        if wins[winner] >= max_wins:
            max_winner = winner
            max_wins = wins[winner]
    # Write your code here.
    return max_winner
