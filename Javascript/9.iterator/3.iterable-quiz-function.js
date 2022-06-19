// [Symbol.iterator](): IterableIterator<T>;
// 0부터 10이하까지 숫자의 2배를 순회하는 이터레이터(반복자) 만들기!
function makeIterable(initialValue, maxValue, callback) {
  return {
    [Symbol.iterator]: () => {
      const max = maxValue;
      let num = initialValue;
      return {
        next() {
          return { value: callback(num++), done: num > max };
        },
      };
    },
  };
}

const multiple = makeIterable(0, 20, (num) => num * 2);
console.clear();
for (const num of multiple) {
  console.log(num);
}

const single = makeIterable(0, 20, (num) => num);
for (const num of single) {
  console.log(num);
}
