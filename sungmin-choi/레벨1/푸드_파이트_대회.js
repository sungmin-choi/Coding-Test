function solution(food) {
  let answer = [];
  for (let i = 1; i < food.length; i++) {
    const foodCnt = Math.floor(food[i] / 2);
    for (let j = 0; j < foodCnt; j++) {
      answer.push(i);
    }
  }
  console.log(answer.join(""));
  console.log(answer.reverse().join(""));
  return answer.join("") + "0" + answer.reverse().join("");
}

solution([1, 7, 1, 2]);
