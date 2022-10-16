function permutation(arr, selectNum) {
  let result = [];
  if (selectNum === 1) return arr.map((ele) => [ele]);
  arr.forEach((ele, index, arr) => {
    const fixer = ele;
    const restArr = arr.filter((_, idx) => idx !== index);
    const combinArr = permutation(restArr, selectNum - 1);
    const combinFixer = combinArr.map((ele) => [fixer, ...ele]);
    result.push(...combinFixer);
  });
  return result;
}
function solution(k, dungeons) {
  let answer = 0;
  let permutationArr = permutation(dungeons, dungeons.length);
  for (const arr of permutationArr) {
    let count = 0;
    let energy = k;
    for (const item of arr) {
      if (energy >= item[0]) {
        energy -= item[1];
        count++;
      } else break;
    }
    answer = answer < count ? count : answer;
  }
  return answer;
}
