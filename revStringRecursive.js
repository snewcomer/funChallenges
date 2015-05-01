function reverse(str) {
  //if reverse("scott") - deepest call returns 't', next deepest call adds 't' and returns reverse('tt'), next deepest call adds 'o' and returns reverse('ott').....
  //alternatively if starting from more intuitive route, by the third recursive call:: (((reverse('tt')) + 'o') + 'c') + 's'
  return str.length == 1 ? str : reverse(str.substring(1)) + str.charAt(0)
}
