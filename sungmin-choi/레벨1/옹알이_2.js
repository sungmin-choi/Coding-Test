function solution(babbling) {
  const r1 = /(aya|ye|woo|ma)\1/;
  const r2 = /^(aya|ye|woo|ma)+$/;
  let answer = 0;
  for (const b of babbling) {
    const m = r1.exec(b);
    console.log(m);
    if (m) continue;

    const m2 = r2.exec(b);
    if (!m2) continue;

    answer++;
  }

  return answer;
}

solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]);
