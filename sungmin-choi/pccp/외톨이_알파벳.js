function solution(input_string) {
  var answer = [];
  const visited = {};
  for (let i = 0; i < input_string.length; i++) {
    if (visited[input_string[i]]) continue;
    const alpha = input_string[i];
    const alphaList = [i];

    visited[input_string[i]] = true;
    for (let j = i + 1; j < input_string.length; j++) {
      if (alpha === input_string[j]) {
        alphaList.push(j);
      }
    }
    if (alphaList.length >= 2) {
      let index = alphaList[0];
      for (let i = 1; i < alphaList.length; i++) {
        if (alphaList[i] - index > 1) {
          answer.push(alpha);
          break;
        }
        index = alphaList[i];
      }
    }
  }
  return answer.length === 0 ? "N" : answer.sort().join("");
}

console.log(solution("zbzbz"));
