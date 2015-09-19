function order(words){
  
  return words.split(' ').sort(function(a, b){
      return a.match(/\d/) - b.match(/\d/);
   }).join(' ');
} 

//15min
function order(words){
  if (!words) { return ''; }
  let sort_obj = {};
  let string_array = words.split(' ');
  string_array.forEach((str) => {
    let num = parseInt(str.match(/\d+/), 10);
    sort_obj[num] = str;
  });
  let new_obj = {};
  Object.keys(sort_obj).sort().forEach((key) => {
    new_obj[key] = sort_obj[key];
  });
  let new_str = '';
  for (str in new_obj) {
    new_str += new_obj[str] + ' ';
  }
  return new_str.trim();
}
