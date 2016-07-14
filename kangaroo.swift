let intArray = readLine()!.characters.split(" ").map(String.init).map { Int($0)!}

let dx = intArray[0] - intArray[2]
let dv = intArray[3] - intArray[1]

if(dv == 0) {
    //if not moving
    print("NO")
} else if((dx % dv == 0) && (dx / dv > 0)) {
    // (-2 to 2 dx % -2 to 2 dv)  && first behind but faster or first ahead but slower
    print("YES")
} else {
    print("NO")
}
