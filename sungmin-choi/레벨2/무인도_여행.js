function solution(maps) {
  const answers = [];
  const islands = [];

  const dirs = [
    [-1, 0],
    [1, 0],
    [0, 1],
    [0, -1],
  ];

  for (const row of maps) islands.push(row.split(""));

  for (let i = 0; i < islands.length; i++) {
    for (let j = 0; j < islands[0].length; j++) {
      if (islands[i][j] !== "X") {
        const queue = [[i, j]];
        let total = Number(islands[i][j]);
        islands[i][j] = "X";
        while (queue.length > 0) {
          const [y, x] = queue.shift();
          for (const dir of dirs) {
            const cx = dir[1] + x;
            const cy = dir[0] + y;
            if (
              cx >= 0 &&
              cx < islands[0].length &&
              cy >= 0 &&
              cy < islands.length
            ) {
              if (islands[cy][cx] !== "X") {
                queue.push([cy, cx]);
                total = total + Number(islands[cy][cx]);
                islands[cy][cx] = "X";
              }
            }
          }
        }
        answers.push(total);
      }
    }
  }
  if (answers.length === 0) return [-1];
  return answers.sort((a, b) => Number(a) - Number(b));
}
