function digitize(n) {
  n = String(n);
  m = []
  for (i = 0; i < n.length; i++) {
    m.push( parseInt( n[i] ) );
  }
  return m;
}

/*
Given a non-negative integer, return an array / a list of the individual digits in order.

Examples:

123 => [1,2,3]

1 => [1]

*/
