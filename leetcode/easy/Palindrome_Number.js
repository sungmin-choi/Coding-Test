var isPalindrome = function (x) {
  const cx = String(x).split("");
  const rx = String(x).split("").reverse();

  for (let i = 0; i < cx.length; i++) {
    if (cx[i] !== rx[i]) {
      return false;
    }
  }

  return true;
};

console.log(isPalindrome(-121));
