function solution(skill, skill_trees) {
  let failure = 0;
  skill = skill.split("");
  for (const skill_tree of skill_trees) {
    let index = 0;
    for (const thisSkill of skill_tree) {
      if (
        skill.indexOf(thisSkill) !== -1 &&
        skill.indexOf(thisSkill) === index
      ) {
        index++;
      } else if (skill.indexOf(thisSkill) === -1) continue;
      else {
        failure++;
        break;
      }
    }
  }

  return skill_trees.length - failure;
}

console.log(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]));
