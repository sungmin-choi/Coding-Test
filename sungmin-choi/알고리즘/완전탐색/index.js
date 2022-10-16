// 조합
const getCombinations = function (arr, selectNumber) {
  const results = [];
  if (selectNumber === 1) return arr.map((el) => [el]);
  // n개중에서 1개 선택할 때(nC1), 바로 모든 배열의 원소 return

  arr.forEach((fixed, index, origin) => {
    const rest = origin.slice(index + 1);
    // 해당하는 fixed를 제외한 나머지 뒤
    const combinations = getCombinations(rest, selectNumber - 1);
    // 나머지에 대해서 조합을 구한다.
    const attached = combinations.map((el) => [fixed, ...el]);
    //  돌아온 조합에 떼 놓은(fixed) 값 붙이기
    results.push(...attached);
    // 배열 spread syntax 로 모두다 push
  });

  return results; // 결과 담긴 results return
};
/*
Input: [1, 2, 3, 4]  4개중에 3개 고를때.
Output: [ [1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4] ]
*/

// 순열
const getPermutations = function (arr, selectNumber) {
  const results = [];
  if (selectNumber === 1) return arr.map((el) => [el]);
  // n개중에서 1개 선택할 때(nP1), 바로 모든 배열의 원소 return. 1개선택이므로 순서가 의미없음.

  arr.forEach((fixed, index, origin) => {
    const rest = [...origin.slice(0, index), ...origin.slice(index + 1)];
    // 해당하는 fixed를 제외한 나머지 배열
    const permutations = getPermutations(rest, selectNumber - 1);
    // 나머지에 대해서 순열을 구한다.
    const attached = permutations.map((el) => [fixed, ...el]);
    //  돌아온 순열에 떼 놓은(fixed) 값 붙이기
    results.push(...attached);
    // 배열 spread syntax 로 모두다 push
  });

  return results; // 결과 담긴 results return
};
/*
Input: [1, 2, 3, 4] 
Output: [
  [ 1, 2, 3 ], [ 1, 2, 4 ],
  [ 1, 3, 2 ], [ 1, 3, 4 ],
  [ 1, 4, 2 ], [ 1, 4, 3 ],
  [ 2, 1, 3 ], [ 2, 1, 4 ],
  [ 2, 3, 1 ], [ 2, 3, 4 ],
  [ 2, 4, 1 ], [ 2, 4, 3 ],
  [ 3, 1, 2 ], [ 3, 1, 4 ],
  [ 3, 2, 1 ], [ 3, 2, 4 ],
  [ 3, 4, 1 ], [ 3, 4, 2 ],
  [ 4, 1, 2 ], [ 4, 1, 3 ],
  [ 4, 2, 1 ], [ 4, 2, 3 ],
  [ 4, 3, 1 ], [ 4, 3, 2 ] 
  ]
*/
