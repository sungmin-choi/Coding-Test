const getCombinations = function (arr, selectNumber) {
  const results = [];
  if (selectNumber === 1) return arr.map((el) => [el]);
  arr.forEach((fixed, index, origin) => {
    const rest = origin.slice(index + 1);
    const combinations = getCombinations(rest, selectNumber - 1);
    const attached = combinations.map((el) => [fixed, ...el]);
    results.push(...attached);
  });
  return results;
};

// [1,2,3], [1,3,4], [2,3,4], [1,2,4]
function solution(relation) {
  const combinationArr = [];
  const keys = [];
  const arr = Array.from({ length: relation[0].length }, (_, i) => i);
  for (let i = relation[0].length; i > 0; i--) {
    combinationArr.push(...getCombinations(arr, i));
  }

  for (const combination of combinationArr) {
    const set = new Set();
    for (let i = 0; i < relation.length; i++) {
      let key = "";
      for (const index of combination) {
        key = key + relation[i][index];
      }
      set.add(key);
    }
    if (set.size === relation.length) {
      keys.push(combination.join(""));
    }
  }
  const answer = [];
  for (let i = 0; i < keys.length; i++) {
    let isUnique = true;
    for (let j = i + 1; j < keys.length; j++) {
      const regx = new RegExp(`[${keys[j]}]`, "g");
      if (keys[i].match(regx)) {
        if (keys[i].match(regx).length === keys[j].length) {
          isUnique = false;
          break;
        }
      }
    }
    if (isUnique) {
      answer.push(keys[i]);
    }
  }
  return answer.length;
}

solution([
  ["a", "1", "aaa", "c", "ng"],
  ["a", "1", "bbb", "e", "g"],
  ["c", "1", "aaa", "d", "ng"],
  ["d", "2", "bbb", "d", "ng"],
]);

solution([
  ["100", "ryan", "music", "2"],
  ["200", "apeach", "math", "2"],
  ["300", "tube", "computer", "3"],
  ["400", "con", "computer", "4"],
  ["500", "muzi", "music", "3"],
  ["600", "apeach", "music", "2"],
]);
