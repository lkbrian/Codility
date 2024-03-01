function solution(Arr) {
  let occurrence = new Set();
  Arr.forEach((element) => {
    occurrence.has(element)
      ? occurrence.delete(element)
      : occurrence.add(element);
  });
  const [unpaired] = Array.from(occurrence);
  console.log(unpaired);
}
solution([9, 1, 7, 5, 9, 7, 5, 3, 11]);
