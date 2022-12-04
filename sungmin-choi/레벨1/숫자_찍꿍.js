function solution(X, Y) {
  const xobj = {};
  const yobj = {};

  const unions = [];

  for (const num of X) {
    if (xobj[num]) xobj[num] = xobj[num] + 1;
    else xobj[num] = 1;
  }
  for (const num of Y) {
    if (yobj[num]) yobj[num] = yobj[num] + 1;
    else yobj[num] = 1;
  }

  for (const ele in xobj) {
    if (yobj[ele]) {
      const cnt = yobj[ele] > xobj[ele] ? xobj[ele] : yobj[ele];
      for (let i = 0; i < cnt; i++) {
        unions.push(Number(ele));
      }
    }
  }
  if (unions.length === 0) return "-1";
  const answer =
    unions.length > 0 ? unions.sort((a, b) => b - a).join("") : "-1";
  if (answer === "") return "-1";
  else if (Number(answer) === 0) return "0";

  return answer;
}

solution("5255", "1255");
