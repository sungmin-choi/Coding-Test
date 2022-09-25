function Accumulator(startingValue) {
  this.startingValue = startingValue;
  this.value = startingValue;
  this.read = function () {
    const num = prompt("더할 값을 입력해주세요.", 0);
    this.value += num;
  };
}

let accumulator = new Accumulator(1); // 최초값: 1

accumulator.read(); // 사용자가 입력한 값을 더해줌
accumulator.read(); // 사용자가 입력한 값을 더해줌

alert(accumulator.value); // 최초값과 사용자가 입력한 모든 값을 더해 출력함
