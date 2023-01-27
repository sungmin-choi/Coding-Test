// function getMusicTime(start, end) {
//   let result = 0;
//   let [shour, smin] = start.split(":");
//   let [ehour, emin] = end.split(":");
//   if (smin > emin) {
//     result = (ehour - shour - 1) * 60 + emin - smin + 60;
//   } else {
//     result = (ehour - shour) * 60 + emin - smin;
//   }
//   return result;
// }

function solution(m, musicinfos) {
  let answers = [];
  for (const musicinfo of musicinfos) {
    let [startTime, endTime, musicName, melodey] = musicinfo.split(",");
    const [fromHour, fromMin] = startTime.split(":").map((v) => parseInt(v));
    const [endHour, endMin] = endTime.split(":").map((v) => parseInt(v));
    const playTime = (endHour - fromHour) * 60 + (endMin - fromMin);

    m = m
      .replaceAll("C#", "c")
      .replaceAll("D#", "d")
      .replaceAll("F#", "f")
      .replaceAll("G#", "g")
      .replaceAll("A#", "a");
    melodey = melodey
      .replaceAll("C#", "c")
      .replaceAll("D#", "d")
      .replaceAll("F#", "f")
      .replaceAll("G#", "g")
      .replaceAll("A#", "a");
    if (playTime < melodey.length) {
      answers.push({
        name: musicName,
        time: playTime,
        sheet: melodey.slice(0, playTime),
      });
    } else if (playTime == melodey.length) {
      answers.push({
        name: musicName,
        time: playTime,
        sheet: melodey,
      });
    } else {
      const times = Math.floor(playTime / melodey.length);
      const spread = playTime % melodey.length;

      let sheet = "";
      for (let i = 0; i < times; i++) {
        sheet = sheet + melodey;
      }

      sheet = sheet + melodey.slice(0, spread);

      answers.push({
        name: musicName,
        time: playTime,
        sheet: sheet,
      });
    }
  }

  answers = answers.filter((ele) => ele.sheet.includes(m));
  if (answers.length === 0) {
    return "(None)";
  }
  if (answers.length > 1) {
    answers.sort((a, b) => b.time - a.time);
  }

  return answers[0].name;
}

console.log(
  solution("CDEF", ["12:00,12:04,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"])
);

console.log(
  solution("CC#BCC#BCC#BCC#B", [
    "03:00,03:30,FOO,CC#B",
    "04:00,04:08,BAR,CC#BCC#BCC#B",
  ])
);

console.log(
  solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"])
);

console.log(solution("ABC", ["12:00,12:06,HELLO,ABC#ABC#ABC"]));

console.log(solution("CDEFGAC", ["12:00,12:06,HELLO,CDEFGA"]));
