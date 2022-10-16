function solution(records) {
  const answer = [];
  const recordsMap = new Map();
  for (const record of records) {
    const [behave, id, name] = record.split(" ");
    if (name) {
      recordsMap.set(id, name);
    }
  }
  for (const record of records) {
    const [behave, id, name] = record.split(" ");
    if (behave === "Enter") {
      answer.push(`${recordsMap.get(id)}님이 들어왔습니다.`);
    } else if (behave === "Leave") {
      answer.push(`${recordsMap.get(id)}님이 나갔습니다.`);
    }
  }

  return answer;
}

console.log(
  solution([
    "Enter uid1234 Muzi",
    "Enter uid4567 Prodo",
    "Leave uid1234",
    "Enter uid1234 Prodo",
    "Change uid4567 Ryan",
  ])
);
// const [behave, id, name] = "Leave uid1234".split(" ");

// console.log(behave, id, name);
