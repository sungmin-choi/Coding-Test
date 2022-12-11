function solution(k, m, score) {
  let answer = 0;
  let boxes = [];
  score.sort();
  for (i = score.length; i >= 0; i -= m) boxes.push(score.slice(i - m, i));
  boxes.forEach((ele) => {
    if (ele.length === m) {
      answer = answer + ele[0] * m;
    }
  });

  return answer;
}

solution(3, 4, [1, 2, 3, 1, 2, 3, 1]);
