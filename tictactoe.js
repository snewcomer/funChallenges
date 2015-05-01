var a =     [[2,1,1],[0,1,1],[2,2,2]]    ;

function isSolved(board) {
    if (down(board) === 2 || diagonal(board) === 2 || across(board) === 2) {
    return 2;
  } else if (down(board) === 1 || diagonal(board) === 1 || across(board) === 1) {
    return 1;
  } else if (flatten(board) === -1) {
    return -1;
  } else {
    return 0;
  }
}

function down(a) {
  for (i=0; i < a.length; i++) {
    for(j=0; j < a[0].length; j++) {
      if((a[i][j] + a[i+1][j] + a[i+2][j]) === 3 ) {
        return 1;
      } else if((a[i][j] + a[i+1][j] + a[i+2][j]) === 6 ) {
        return 2;
      } else {
        return -1;
      }
    }
  }
}

function diagonal(n) {
  if((n[0][0] === 1 && n[1][1] === 1 && n[2][2]) === 1) {
    return 1;
  } else if(n[0][0] === 2 && n[1][1] === 2 && n[2][2] === 2) {
    return 2;
  } else if(n[0][2] ===1 && n[1][1] === 1 && n[2][0] === 1) {
    return 1;
  } else if(n[0][2] === 2 && n[1][1] === 2 && n[2][0] === 2) {
    return 2;
  } else {
    return -1;
  }
}

function across(n) {
  for(i=0; i < n.length; i++) {
    if (n[i][0] === 1 && n[i][1] === 1 && n[i][2] === 1) {
      return 1;
      break;
    } else if (n[i][0] === 2 && n[i][1] === 2 && n[i][2] === 2) {
      return 2;
      break;
    } 
  }
}

function flatten(n) {
  var flat_array = [].concat.apply([],n);
  var a = flat_array.indexOf(0);
  if ((a > -1) && (diagonal(n) != 2 || diagonal(n) != 1 || across(n) != 1 || across(n) != 2 || down(n) != 1 || down(n) != 2)) {
    return -1;
  } else {
    return 0;
  }
}

isSolved(a);
