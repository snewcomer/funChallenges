let t = Int(readLine()!)!

for _ in 0..<t {
    var bool = true
    let x2 = Int(readLine()!)!
    let o = readLine()!.characters.split(" ").map{Int(String($0))!}
    let sum = o.reduce(0, combine: +)
    var sumLeft = 0
    var equal = false
    for i in 1..<x2 {
        sumLeft += o[i - 1]
        let sumRight = sum - sumLeft - o[i]
        if sumRight == sumLeft {
            equal = true
            break
        }
    }

    if equal || x2 == 1 {
        print("YES")
    } else {
        print("NO")
    }   
}
