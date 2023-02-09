function solution(book_time) {
  const answer = [];

  book_time
    .map((time) => {
      const [startTime, endTime] = time;
      const [st1, st2] = startTime.split(":");
      const [et1, et2] = endTime.split(":");
      const a = Number(st1) * 60 + Number(st2);
      const b = Number(et1) * 60 + Number(et2);
      return [a, b + 10];
    })
    .sort((a, b) => a[0] - b[0])
    .forEach((time, index) => {
      if (index === 0) answer.push(time);
      else {
        let flag = 0;
        const [startTime, endTime] = time;
        for (let i = 0; i < answer.length; i++) {
          const [curStartTime, curEndTime] = answer[i];
          if (startTime >= curEndTime) {
            answer[i] = [curStartTime, endTime];
            flag = 1;
            break;
          } else if (endTime <= curStartTime) {
            answer[i] = [startTime, curEndTime];
            flag = 1;
            break;
          }
        }
        if (!flag) {
          answer.push(time);
        }
      }
    });
}

solution([
  ["15:00", "17:00"],
  ["16:40", "18:20"],
  ["14:20", "15:20"],
  ["14:10", "19:20"],
  ["18:20", "21:20"],
]);
