const bracketOpen = ["(", "{", "["];
const bracketClose = [")", "}", "]"];
var isValid = function (s) {
  const stack = [];
  for (const b of s) {
    const openIndex = bracketOpen.indexOf(b);
    const closeIndex = bracketClose.indexOf(b);

    if (openIndex !== -1) {
      stack.push(bracketOpen[openIndex]);
    } else {
      const pb = stack.pop();
      if (bracketOpen[closeIndex] !== pb) {
        return false;
      }
    }
  }
  return stack.length === 0 ? true : false;
};

console.log(isValid("(){}{"));
