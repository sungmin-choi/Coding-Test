var lengthOfLongestSubstring = function (s) {
  let answer = [];
  let tempStr = "";
  for (const c of s) {
    if (tempStr.indexOf(c) === -1) {
      tempStr = tempStr + c;
    } else {
      const index = tempStr.indexOf(c);

      tempStr = tempStr + c;
      tempStr = tempStr.slice(index + 1);
    }
    answer.push(tempStr);
  }
  return answer.length > 0
    ? answer.sort((a, b) => b.length - a.length)[0].length
    : 0;
};

console.log(lengthOfLongestSubstring(" "));
