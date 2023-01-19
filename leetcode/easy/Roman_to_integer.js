const roman_symbols = {
  M: 1000,
  D: 500,
  C: 100,
  L: 50,
  X: 10,
  V: 5,
  I: 1,
};
var romanToInt = function (s) {
  let result = 0;
  let tempSymbol = undefined;
  for (let i of s.split("").reverse()) {
    if (tempSymbol === undefined) {
      tempSymbol = i;
      result = result + roman_symbols[i];
    } else if (roman_symbols[tempSymbol] > roman_symbols[i]) {
      result = result - roman_symbols[i];
      tempSymbol = i;
    } else {
      result = result + roman_symbols[i];
      tempSymbol = i;
    }
  }
  return result;
};

romanToInt("MCMXCIV");
