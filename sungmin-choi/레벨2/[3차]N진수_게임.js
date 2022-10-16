function solution(n, t, m, p) {
  let answer = "";
  let str = "";
  let count = 0;
  let currTurn = p;
  let num = 0;
  while (count < t) {
    while (str.length < currTurn) {
      str += num.toString(n);
      num++;
    }
    answer += str[currTurn - 1].toLocaleUpperCase();
    currTurn += m;
    count++;
  }
  return answer;
}
console.log(solution(2, 4, 2, 1));
