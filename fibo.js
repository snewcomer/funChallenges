function fib(n, undefined){
    if(fib.cache[n] === undefined){
        fib.cache[n] = fib(n-1) + fib(n-2);
    }
    return fib.cache[n];
}
fib.cache = [0, 1, 1];
fib(5)
//(n=5)4 + 3  --> 5 == 3 + 2
//(n=4)3 + 2  --> 4 == (2)+1 = 3 (we got +1 because we evaluated (n=4)(fib(2) which returns 1
//(n=3)2 + 1  --> 3 == 1+1 = 2 (goes up to parenthesized expression on line above)
//return 1 to n=3


//get last number in fib sequence for given length
var recursive = function(n) {
    if(n <= 2) {
        return 1;
    } else {
        return recursive(n - 1) + recursive(n - 2);
    }
};
