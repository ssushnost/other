start_input = input().split()
vertex = int(start_input[0])
inp = []
visited = [False] * vertex
weight = [10 ** 10] * vertex
weight[int(start_input[1])-1] = 0
# инпут
for i in range(vertex):
    inp.append(list(map(int, input().split())))

# бесконечности
for i in range(vertex):
    for j in range(vertex):
        if int(inp[i][j]) == 0 or int(inp[i][j]) == -1:
            inp[i][j] = 1000

while False in visited:
    for i in range(vertex):
        if not visited[i]:
            min_weight = weight[i]
            min_weight_index = i
    for i in range(vertex):
        if weight[i] < min_weight and visited[i] == False:
            min_weight = weight[i]
            min_weight_index = i
    for i in range(vertex):
        if weight[i] > inp[min_weight_index][i] + weight[min_weight_index]:
            weight[i] = inp[min_weight_index][i] + weight[min_weight_index]
    visited[min_weight_index] = True
print(weight)
