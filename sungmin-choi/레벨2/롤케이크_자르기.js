function solution(topping) {
  let answer = 0;
  const left = { length: 0 };
  const right = { length: 0 };
  for (const item of topping) {
    if (right[item]) {
      right[item] += 1;
    } else {
      right[item] = 1;
      right.length += 1;
    }
  }
  for (const item of topping) {
    if (left[item]) {
      left[item] += 1;
    } else {
      left[item] = 1;
      left.length += 1;
    }
    if (right[item] === 1) {
      delete right[item];
      right.length -= 1;
    } else {
      right[item] -= 1;
    }
    if (left.length === right.length) answer++;
  }
  return answer;
}

console.log(solution([1, 2, 1, 3, 1, 4, 1, 2]));
