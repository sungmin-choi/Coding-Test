function fold(arr, index) {
  let result = [];
  let left = index - 1;
  let right = index;
  while (left >= 0 && right <= arr.length - 1) {
    const sum = arr[left] + arr[right];
    result.unshift(sum);
    left--;
    right++;
  }
  if (left < 0) {
    let concatArr = [];
    for (let i = arr.length - 1; i >= right; i--) {
      concatArr.push(arr[i]);
    }
    return [...concatArr, ...result];
  } else if (right >= arr.length) {
    let concatArr = [...arr].slice(0, left + 1);
    return [...concatArr, ...result];
  }
}

function solution(arr, n) {
  let foldCase = [[...arr]];
  let countFold = 0;
  let curCase = [[...arr]];
  let result = 0;
  while (countFold < n) {
    let thisCase = [...curCase];
    curCase = [];
    for (const thisArr of thisCase) {
      const arrLen = thisArr.length - 1;
      for (let i = 1; i <= arrLen; i++) {
        curCase.push(fold(thisArr, i));
      }
    }
    foldCase = [...foldCase, ...curCase];
    countFold++;
  }

  for (const list of foldCase) {
    result = result < Math.max(...list) ? Math.max(...list) : result;
  }
  return result;
}

solution([1, 2, 3, 4, 5], 2);
