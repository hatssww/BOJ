N = int(input())
scores = list(map(int, input().split()))
max_score = max(scores)
new_scores = []

for i in range(N):
    new_score = scores[i] / max_score * 100
    new_scores.append(new_score)

average = sum(new_scores) / N
print(average)