// read the integer n
var n = Int(readLine()!)!

// spaces make the appearance of the tower.  Reverse loop starting with highest number, build string with line breaks by adding fake characters and replacing w/ spaces
var str = ""
for row in (0..<n).reverse() {
    for _ in 0..<row {
      str += "*"
    }
    var numHash = n - row
    for _ in 0..<numHash {
        str += "#"
    }
    str += "\n"
}
let replaced = str.characters.map {
    $0 == "*" ? " " : $0
}
print(String(replaced))
