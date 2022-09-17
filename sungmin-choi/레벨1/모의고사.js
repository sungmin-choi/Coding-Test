function solution(answers) {
  var answer = [];
  let a = [1, 2, 3, 4, 5];
  let b = [2, 1, 2, 3, 2, 4, 2, 5];
  let c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];
  let len = [];
  let j = 0;
  let max = 0;
  let as = 0;
  let bs = 0;
  let cs = 0;
  for (let i = 0; i < answers.length; i++) {
    if (answers[i] === a[i > 4 ? i % 5 : i]) as++;
    if (answers[i] === b[i > 7 ? i % 8 : i]) bs++;
    if (answers[i] === c[i > 9 ? i % 10 : i]) cs++;
  }
  len = [as, bs, cs];
  max = Math.max(as, bs, cs);
  for (let k = 0; k < 3; k++) {
    if (max === len[k]) {
      answer[j] = k + 1;
      j++;
    }
  }
  return answer;
}
