const regx = /\d+S|\d+D|\d+T|[*#]/g;
function solution(dartResult) {
  var answer = [];
  const scoreList = dartResult.match(regx);
  for (const score of scoreList) {
    if (/\d+S|\d+D|\d+T/.test(score)) {
      const number = score.match(/\d+/g)[0];
      if (score[score.length - 1] === "S") answer.push(number);
      if (score[score.length - 1] === "D") answer.push(Math.pow(number, 2));
      if (score[score.length - 1] === "T") answer.push(Math.pow(number, 3));
    } else if (score === "*") {
      if (answer.length >= 2) {
        answer[answer.length - 1] = answer[answer.length - 1] * 2;
        answer[answer.length - 2] = answer[answer.length - 2] * 2;
      } else {
        answer[answer.length - 1] = answer[answer.length - 1] * 2;
      }
    } else if (score === "#")
      answer[answer.length - 1] = answer[answer.length - 1] * -1;
  }

  return answer.reduce((pre, cur) => pre + Number(cur), 0);
}

console.log(solution("1D2S#10S"));
