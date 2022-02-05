function onesComplement(n) {
  let m = "";
  for (i=0; i < n.length; i++) {
    if (n[i] == "1") {m += "0"} else {m += "1"}
  }
  return m
};

/*
The Ones' Complement of a binary number is the number obtained by swapping all the 0s for 1s and all the 1s for 0s. For example:
  onesComplement(1001) = 0110
  onesComplement(1001) = 0110

*/
