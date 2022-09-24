function solution(s) {
  let answer = [0];
  for (const i of s) {
    const top = answer.length - 1;
    if (answer.length >= 2) {
      if (answer[top] === i) {
        answer.pop();
      } else {
        answer.push(i);
      }
    } else {
      answer.push(i);
    }
  }
  return answer.length > 2 ? 0 : 1;
}

console.log(solution("abccaeeaba"));
