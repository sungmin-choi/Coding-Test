// function solution(order) {
//   let answer = 1;
//   const checkOrder = Array(order.length + 1).fill(false);
//   checkOrder[order[0]] = true;
//   let min = order[0] - 1;
//   let next = min;
//   for (let i = 1; i < order.length; i++) {
//     if (order[i] > order[i - 1]) {
//       checkOrder[order[i]] = true;
//       ++answer;
//       if (checkOrder[order[i] - 1]) {
//         if (checkOrder[next]) {
//           next = min;
//         }
//       } else {
//         next = order[i] - 1;
//       }
//     } else if (order[i] < order[i - 1]) {
//       if (order[i] !== next) break;
//       checkOrder[order[i]] = true;
//       ++answer;
//       if (order[i] - 1 < min) {
//         min = order[i] - 1;
//       }
//       if (checkOrder[order[i] - 1]) {
//         next = min;
//       } else {
//         next = order[i] - 1;
//       }
//     }
//   }
//   return answer;
// }

function solution(order) {
  var answer = 0;
  let stack = [];
  let now = 1;
  let index = 0;
  while (index < order.length) {
    while (now < order[index]) {
      stack.push(now);
      now++;
    }
    if (now > order[index]) {
      if (stack[stack.length - 1] !== order[index]) {
        break;
      } else {
        stack.pop();
      }
    }
    if (now === order[index]) {
      now++;
    }
    answer++;
    index++;
  }
  return answer;
}
console.log(solution([5, 4, 8, 7, 6, 11, 10, 9, 3, 2, 1]));
