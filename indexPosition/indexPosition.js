function solution(arrayone) {
  let result = [];
  for (let i = 0; i < arrayone.length; i++) {
    for (let j = i + 1; j < arrayone.length; j++) {
      for (let value = 0; value < arrayone[i].length; value++) {
        if (arrayone[i][value] == arrayone[j][value]) {
          result.push(i, j, value);
        }
      }
    }
  }
  return result;
}
let arrayone = ["ab", "b", "fc", "bd"];
console.log(solution(arrayone));
