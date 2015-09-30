//correct sol'n
function scramble(str1, str2) {
  let dict = {};
  let dicty = {};
  let memo = true;
  let count = 0;
  for (let y=0; y < str1.length; y++) {
    dicty[str1[y]] = dicty[str1[y]] + 1 || 1;
  }
  for (let x=0; x < str2.length; x++) {
    if (str2[x] in dicty && dicty[str2[x]] > 0) {
      dict[str2[x]] = dict[str2[x]] + 1 || 1;
      dicty[str2[x]] -= 1;
      memo = true && memo;
    }
    if (dict[str2[x]] < 0) {
      memo = false;
    }
  }
  Object.keys(dict).forEach((key, indx) => {
    count += dict[key];
  });
  return memo && count === str2.length;
}


function scramble(str1, str2) {
  let str2Array = str2.split('');
  return bool = str2Array.reduce((memo, letter) => {
    let str2RegExp = new RegExp('[' + letter + ']');
    return memo && str2RegExp.test(str1);  
  }, true);
}

function scramble(str1, str2) {
  let str2Array = str2.split('');
  let dict = {};
  return bool = str2Array.reduce((memo, letter) => {
    let indx = dict[letter] || str1.indexOf(letter);
    dict[letter] = indx
    return memo && indx > -1;  
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
