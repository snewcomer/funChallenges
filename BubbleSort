let n = Int(readLine()!)!
var arr = readLine()!.characters.split(" ").map(String.init).map { Int($0)! }

var numberOfSwaps = 0;

var swapped = false

repeat{
    swapped = false
    for i in 1..<n {
        if arr[i-1] > arr[i] {
            let tmp = arr[i-1]
            arr [i-1] = arr[i]
            arr[i] = tmp
            swapped = true
            numberOfSwaps++
        }
    }
} while swapped


print("Array is sorted in \(numberOfSwaps) swaps.")
print("First Element: \(arr[0])")
print("Last Element: \(arr[arr.count-1])")
//https://www.hackerrank.com/challenges/30-sorting
