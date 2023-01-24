var convert = function (s, numRows) {
  let curRow = 0;
  let answer = "";
  const strMap = Array.from(Array(numRows), () => []);
  let i = 0;

  if (numRows === 1) {
    return s;
  }

  while (i < s.length) {
    if (curRow === 0) {
      for (let j = 0; j < numRows; j++) {
        if (i < s.length) strMap[j].push(s[i]);
        else break;
        i++;
        curRow++;
      }
      curRow = curRow - 1;
    } else {
      for (let j = 0; j < numRows; j++) {
        if (j === curRow) {
          if (i < s.length) strMap[j].push(s[i]);
          i++;
        } else {
          strMap[j].push(" ");
        }
      }
    }
    curRow = curRow - 1;
  }
  for (const str of strMap) {
    answer = answer + str.filter((ele) => ele !== " ").join("");
  }
  return answer;
};

convert("AB", 1);
