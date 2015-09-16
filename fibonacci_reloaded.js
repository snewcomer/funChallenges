function* gen_fib(n) {
  let a = 0
  let b = 1;
  yield a;
  while (n > 1) {
    let tmp = a;
    a = b;
    b += tmp;
    yield a;
    n--;
  }
}

function fib(n) {
  let arr = [];
  let gen = gen_fib(n);
  for (var i of gen) {
    arr.push(i);
  }
  return arr[n-1]
}
