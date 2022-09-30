const a = "108,43";

console.log(
  a
    .split(",")
    .map((a) => Number(a))
    .join(",")
);
