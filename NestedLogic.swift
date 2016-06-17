var actualArr = readLine()!.characters.split(" ").map(String.init).map{ Int($0)! }
var expectedArr = readLine()!.characters.split(" ").map(String.init).map{ Int($0)! }

let withinMonthFine = 15
let afterMonthFine = 500
let afterYearFine = 10000
var fine = 0

for indx in 0..<3 {
    let act = actualArr[indx] 
    let expected = expectedArr[indx]
    if indx == 2 && act > expected {
        fine = afterYearFine
        break
    } else if indx == 1 && act > expected {
        fine = (act - expected) * afterMonthFine
    } else if indx == 0 && act > expected {
        fine = (act - expected) * withinMonthFine
    }
}
print(fine)
//https://www.hackerrank.com/challenges/30-nested-logic
