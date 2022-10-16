function getRemoveBlock(m, n, board) {
  const result = [];
  for (let i = 0; i < m - 1; i++) {
    for (let j = 0; j < n - 1; j++) {
      if (board[i][j] === null) continue;
      if (
        board[i][j] === board[i][j + 1] &&
        board[i][j] === board[i + 1][j] &&
        board[i][j] === board[i + 1][j + 1]
      ) {
        result.push([i, j], [i, j + 1], [i + 1, j], [i + 1, j + 1]);
      }
    }
  }
  return result;
}

function removeBlockInBoard(rmBlocks, board, removeCount) {
  let result = 0;
  for (const [i, j] of rmBlocks) {
    if (board[i][j] === null) continue;
    board[i][j] = null;
    result++;
  }
  return result;
}

function moveBlockPrepareNextGame(m, n, board) {
  for (let i = 0; i < n; i++) {
    const nullArr = [];
    for (let j = m - 1; j >= 0; j--) {
      if (board[j][i] === null) {
        nullArr.push([j, i]);
      } else if (nullArr.length > 0) {
        const [x, y] = nullArr.shift();
        board[x][y] = board[j][i];
        board[j][i] = null;
        nullArr.push([j, i]);
      }
    }
  }
}

function solution(m, n, board) {
  let answer = 0;
  board = Array.from(board, (x) => x.split(""));
  while (true) {
    const rmBlocks = getRemoveBlock(m, n, board);
    if (rmBlocks.length > 0) {
      answer += removeBlockInBoard(rmBlocks, board);
      moveBlockPrepareNextGame(m, n, board);
    } else {
      break;
    }
  }
  return answer;
}

console.log(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]));
