var longestCommonPrefix = function (strs) {
  let answer = "";

  const str = strs.sort((a, b) => a.length - b.length)[0];
  for (let i = 0; i < str.length; i++) {
    let tempStr = str[i];
    for (const item of strs) {
      if (item[i] !== tempStr) {
        return answer;
      }
    }
    answer = answer + tempStr;
  }
  return answer;
};

console.log(longestCommonPrefix(["reflower", "flow", "flight"]));
