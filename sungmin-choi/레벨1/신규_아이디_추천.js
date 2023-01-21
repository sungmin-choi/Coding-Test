const regx1 = /[a-z0-9-_.]/g;
const regx2 = /[.]+/g;
function solution(new_id) {
  let answer = new_id;
  answer = new_id.toLowerCase();
  answer = answer.match(regx1).join("");
  answer = answer.replace(regx2, ".");
  answer = answer.replace(/^[.]/, "");
  answer = answer.replace(/[.]$/, "");
  if (answer.length === 0) answer = "a";
  if (answer.length >= 16) answer = answer.slice(0, 15);
  answer = answer.replace(/[.]$/, "");
  if (answer.length <= 2) {
    const char = answer[answer.length - 1];
    while (answer.length <= 2) {
      answer = answer + char;
    }
  }
  return answer;
}

solution("...!@BaT#*..y.abcdefghijklm");
