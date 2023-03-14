function solution(P) {
  const n = P.length;
  let cnt = 0; // 빠져나올 수 있는 출발점의 개수
  let left = 0; // 가장 왼쪽에서 시작하는 경우
  let right = 0; // 가장 오른쪽에서 시작하는 경우

  for (let i = 0; i < n; i++) {
    if (P[i] === "<") {
      left++; // 왼쪽으로 이동하는 경우 left 증가
    } else {
      right++; // 오른쪽으로 이동하는 경우 right 증가
    }
    // left와 right 중 최소값이 빠져나올 수 있는 출발점
    cnt = Math.min(left, right);
  }

  return cnt;
}

console.log(solution(">>><<<"));

function solution(P) {
  const n = P.length;
  let ans = 0;
  for (let i = 0; i < n; i++) {
    if (P[i] === ">") {
      let j = i + 1;
      while (j < n && P[j] === ">") {
        j++;
      }
      if (j === n) {
        ans++;
      }
    } else if (P[i] === "<") {
      let j = i - 1;
      while (j >= 0 && P[j] === "<") {
        j--;
      }
      if (j === -1) {
        ans++;
      }
    }
  }
  return ans;
}
