<?php 
// Fibonacci Series using Recursion 
function fib($n)
{
    if ($n <= 1) 
        return $n; 
    return fib($n - 1) + fib($n - 2); 
}
  
$n = 9;
echo fib($n); 
?>