function scramble(str1, str2) {
  let str2Array = str2.split('');
  return bool = str2Array.reduce((memo, letter) => {
    let str2RegExp = new RegExp('[' + letter + ']');
    return memo && str2RegExp.test(str1);  
  }, true);
}

function scramble(str1, str2) {
 let bool = true;
 let str2Array = str2.split('');
 str2Array.forEach((letter) => {
   if (str1.indexOf(letter) === -1) {
     bool = false && bool;
   }
 });
 return bool;
}
