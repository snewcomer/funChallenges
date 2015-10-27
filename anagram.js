var arr = ['abc'];

var allAnagrams = function(arr) {
    var anagrams = {};
    arr.forEach(function(str) {
        var recurse = function(ana, str) {
            console.log(ana)
            console.log(str)
            console.log('dddd')
            if (str === '') 
                anagrams[ana] = 1;
            for (var i = 0; i < str.length; i++)
                recurse(ana + str[i], str.slice(0, i) + str.slice(i + 1));
        };
        recurse('', str);
    });
    return Object.keys(anagrams);
}

console.log(allAnagrams(arr));


function generateAnagrams(word) {

    if (word.length < 2) {

        return [word];

    } else {

        // By declaring all variables outside of the loop,
        // we improve efficiency, avoiding the needless
        // declarations each time.

        var anagrams = [];
        var before, focus, after;
        var shortWord, subAnagrams, newEntry;

        for (var i = 0; i < word.length; i++) {

            before = word.slice(0, i);
            focus = word[i];
            after = word.slice(i + 1, word.length + 1);
            shortWord = before + after;
            subAnagrams = generateAnagrams(shortWord);
            for (var j = 0; j < subAnagrams.length; j++){

                newEntry = focus + subAnagrams[j];
                anagrams.push(newEntry);

            }

        }

        return anagrams;

    }

}

var word = 'abc';
var result = generateAnagrams(word);
console.log(result)
