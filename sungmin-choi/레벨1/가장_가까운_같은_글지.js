function solution(s) {
  var answer = [];
  const str = [];
  for (const a of s) {
    if (str.indexOf(a) !== -1) {
      answer.push(str.indexOf(a) + 1);
    } else {
      answer.push(-1);
    }
    str.unshift(a);
  }

  return answer;
}

solution("banana");
