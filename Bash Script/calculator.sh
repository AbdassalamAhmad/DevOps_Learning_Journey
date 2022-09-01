#!/bin/bash
function add {
echo $num1+$num2 = $[$num1+$num2]
}

function subtract {
echo $num1-$num2 = $[$num1-$num2]
}

function multiply {
echo $num1*$num2 = $[$num1*$num2]
}

function divide {
echo "$num1/$num2 =" "$[$num1/$num2]" "and the reminder is $[$num1%$num2]"
}

echo "This is a simple calculator that can add, minus, multiply and divide."

echo -n "enter two numbers: "
read num1 num2

echo choose one of these arithmetics: 
echo "1) add."
echo "2) minus."
echo "3) multiply."
echo "4) divide."
echo "5) all of them."

read case;
case $case in 
	1) add;;
	2) subtract;;
	3) multiply;;
	4) divide;;
	5) add; subtract; multiply; divide;
esac
