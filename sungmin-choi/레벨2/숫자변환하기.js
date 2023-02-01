function inputValue(x, y, n, visited) {
  if (x + n <= y) {
    if (visited[x + n] > visited[x] + 1) {
      visited[x + n] = visited[x] + 1;
    }
  }
  if (x * 2 <= y) {
    if (visited[x * 2] > visited[x] + 1) {
      visited[x * 2] = visited[x] + 1;
    }
  }
  if (x * 3 <= y) {
    if (visited[x * 3] > visited[x] + 1) {
      visited[x * 3] = visited[x] + 1;
    }
  }
}

function solution(x, y, n) {
  const visited = Array.from({ length: y + 1 }, () => 1000000);
  visited[x] = 0;

  for (let i = x; i < y; i++) {
    inputValue(i, y, n, visited);
  }

  return visited[y] === 9999999 ? -1 : visited[y];
}
