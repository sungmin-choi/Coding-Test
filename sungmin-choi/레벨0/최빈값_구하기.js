function solution(array) {
  const nums = {};
  let max = 0;
  let answer = 0;
  for (const num of array) {
    if (nums[num]) nums[num] = nums[num] + 1;
    else {
      nums[num] = 1;
    }
  }

  for (const num in nums) {
    if (nums[num] > max) {
      max = nums[num];
      answer = Number(num);
    } else if (nums[num] === max) {
      answer = -1;
    }
  }
  return answer;
}

solution([1]);
