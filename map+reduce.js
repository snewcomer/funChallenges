bind = function(list, func) {
  var thisList = list.map(function(a) {
    var item = func(a);
    //make sure objects property is array
    if (item instanceof Array) {
      return item
    } else {
      throw new Error("no list provided");
    }
  });
  //flatten list
  var newList = [].concat.apply([], thisList);
  return newList;
}
