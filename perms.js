function permutations(string) {
  function recursion(string, prefix) {
    if (string.length === 0) {
      return [prefix];
    } else {
      let out = [];
      for (let i = 0; i < string.length; i++) {
        var pre = string.substring(0, i); //
        var post = string.substring(i+1); //
        out = out.concat(recursion(pre+post, string[i]+prefix));
        //recursion string arg is the two letters that we want to prepend and swap
        //'ac' ==> 'ca' && 'ac'
        //index 0 just pass up as string last letter and as prefix the first letter + left out
        //index 1 just pass up as string first letter and as prefix last letter + left out letter
      }
      return out;
    }
  }
  let distinct = {};
  recursion(string, "").forEach((result) => {
    distinct[result] = true;
  });
  return Object.keys(distinct);
}
