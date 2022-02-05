function validateWord(word) {
  dictionary = {}
  
  for (i=0; i < word.length; i++) {
    letter = word[i].toUpperCase();
    dictionary[letter] = (dictionary[letter] || 0) + 1;
  }
  
  let last;
  for (const [key, value] of Object.entries(dictionary)) {
    if (last && last != value) { return false;}
    last = value;
  }
  return true;
  
}



/*
For this kata, capitals are considered the same as lowercase letters. Therefore: "A" == "a"
The input is a string (with no spaces) containing [a-z],[A-Z],[0-9] and common symbols. The length will be 0 < length < 100.

  Examples
    "abcabc" is a valid word because "a" appears twice, "b" appears twice, and"c" appears twice.
    "abcabcd" is NOT a valid word because "a" appears twice, "b" appears twice, "c" appears twice, but "d" only appears once!

*/
