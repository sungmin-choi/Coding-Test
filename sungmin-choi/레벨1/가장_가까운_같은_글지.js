// function solution(s) {
//   var answer = [];
//   const str = [];
//   for (const a of s) {
//     if (str.indexOf(a) !== -1) {
//       answer.push(str.indexOf(a) + 1);
//     } else {
//       answer.push(-1);
//     }
//     str.unshift(a);
//   }

//   return answer;
// }

// function solution(s) {
//   var answer = [];
//   let str = "";
//   for (const c of s) {
//     const regex = new RegExp(`${c}`);
//     if (str.match(regex)) {
//       answer.push(str.match(regex).index + 1);
//     } else {
//       answer.push(-1);
//     }
//     str = c + str;
//   }
//   return answer;
// }
// solution("banana");

const regx = /19[2-9][0-9](0[1-9]|1[0-2])(0[1-9]|[1,2][0-9]|3[0,1])/;

console.log(regx.test("19911201"));
