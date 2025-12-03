let number = 10;
let a = 0;
let b = 1;
let nextTerm;

console.log('Fibonacci Series: ');
while(a<=number){
  process.stdout.write(a+" ");
  nextTerm = a+b;
  a = b;
  b = nextTerm;
}