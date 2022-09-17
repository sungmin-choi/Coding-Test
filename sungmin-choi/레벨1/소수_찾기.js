function solution(n) {
  var answer = 0;
  for (let i = 2; i <= n; i++) {
    let sqrtNum = Math.floor(Math.sqrt(i));
    let isDecimal = true;
    while (sqrtNum > 1) {
      if (i % sqrtNum === 0) {
        isDecimal = false;
        break;
      } else {
        sqrtNum--;
      }
    }
    if (isDecimal) {
      answer++;
    }
  }
  return answer;
}

console.log(solution(10));
