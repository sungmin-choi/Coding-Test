var addTwoNumbers = function (l1, l2) {
  return String(Number(l1.reverse().join("")) + Number(l2.reverse().join("")))
    .split("")
    .reverse()
    .map((ele) => Number(ele));
};
