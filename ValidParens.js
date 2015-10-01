function validParentheses(parens){
  let arr = parens.split('');
  if (parens.length === 1 || arr[arr.length - 1] === '(') {
    return false;
  }
  let func = gen_func(arr);
  let cache = [];
  let count = 0;
  for (let i of func) {
    count = (i === '(') ? count += 1 : count -= 1;
    for (let y of cache) {
      let indx = cache.indexOf(i);
      if (indx === -1) {
        cache.splice(indx, 1);
        break;
      } else {
        cache.push(i)
      }
    }
  }
  return count === 0 && cache.length === 0;
}

function* gen_func(arr) {
  for (let x of arr) {
    yield x;
  }
}
validParentheses( "())(" )

//best sol'n
function validParentheses(parens){
  var indent = 0;
  
  for (var i = 0 ; i < parens.length && indent >= 0; i++) {
    indent += (parens[i] == '(') ? 1 : -1;    
  }
  
  return (indent == 0);
}
