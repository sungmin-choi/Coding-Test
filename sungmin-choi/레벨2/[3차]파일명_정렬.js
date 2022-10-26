function solution(files) {
  let answer = [];
  for (let i = 0; i < files.length; i++) {
    const file = {};
    file.fullName = files[i];
    let numIndex = 0;
    let firstName = "";
    let number = "";
    for (numIndex; numIndex < files[i].length; numIndex++) {
      if (isNaN(files[i][numIndex]) || files[i][numIndex] === " ") {
        firstName += files[i][numIndex];
      } else {
        break;
      }
    }
    let count = 0;
    for (numIndex; numIndex < files[i].length; numIndex++) {
      if (!isNaN(files[i][numIndex]) && count < 5) {
        number += files[i][numIndex];
      } else {
        break;
      }
      count++;
    }
    file.firstName = firstName.toLocaleLowerCase();
    file.number = Number(number);
    file.index = i;
    answer.push(file);
  }
  console.log(answer);
  return answer.sort(sortFiles).map((item) => item.fullName);
}

function sortFiles(a, b) {
  //   if (a.firstName > b.firstName) {
  //     return 1;
  //   } else if (a.firstName < b.firstName) {
  //     return -1;
  //   } else {
  //     if (a.number > b.number) return 1;
  //     else if (a.number < b.number) return -1;
  //     else {
  //       if (a.index > b.index) return 1;
  //       else if (a.index < b.index) return -1;
  //     }
  //   }
  return a.firstName < b.firstName
    ? -1
    : a.firstName > b.firstName
    ? 1
    : a.number < b.number
    ? -1
    : a.number > b.number
    ? 1
    : 0;
}

// headA < headB ? -1 : headA > headB ? 1 : numberA < numberB ? -1 : numberA > numberB ? 1 : 0
console.log(
  solution([
    "F- gh5 Freedom Fighter",
    "B-50 Superfortress",
    "A-10 Thunderbolt II",
    "F-14 Tomcat",
  ])
);
// function solution(files) {
//     var answer = [];
//     const numberRegex = /[0-9]+/
//     answer = files.sort((a, b) => {
//         const [matchA, matchB] = [a.match(numberRegex), b.match(numberRegex)]
//         const [headA, headB] = [a.slice(0, matchA.index).toLowerCase(), b.slice(0, matchB.index).toLowerCase()]
//         const [numberA, numberB] = [parseInt(matchA[0]), parseInt(matchB[0])]
//         return headA < headB ? -1 : headA > headB ? 1 : numberA < numberB ? -1 : numberA > numberB ? 1 : 0
//     })
//     return answer;
// }
