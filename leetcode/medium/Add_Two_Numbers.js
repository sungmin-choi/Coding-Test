var addTwoNumbers = function (l1, l2) {
  return String(Number(l1.reverse().join("")) + Number(l2.reverse().join("")))
    .split("")
    .reverse()
    .map((ele) => Number(ele));
};

console.log(
  String(Number([0].reverse().join("")) + Number([0].reverse().join("")))
    .split("")
    .reverse()
    .map((ele) => Number(ele))
);
