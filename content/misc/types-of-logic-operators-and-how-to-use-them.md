---
title: Types of Logic Operators and How to Use Them
tags: [programming, logic]
---

## What are Logical Operators?

Say you are out grabbing lunch on behalf of a friend or a fellow student, and their lunch comes with a maximum of two sides for free. When you ask your friend about what sides they want, you may ask them one of the following 4 questions:

1.  Do you want an apple *and* bread?
2.  Do you want an apple *or* bread?
3.  Do you *not* want an apple *and* bread?
4.  Do you *not* want an apple *or* bread?

Reading these questions outload, you would know that each question has 2 immediate and unique responses your friend could give:

1.  Yes I want both, or no I do not want both.
2.  I want an apple, or I want a banana.
3.  I do, or do not want both the apple and bread.
4.  I do, or do not want an apple or bread.

In programming the logic of "and", "or", and "not" related questions is the same as in real conversation. In Python, you can type these exact words when asking your computer to run through some logical thinking. In programs like C and Java however, the equivalent is ```&&```, ```||```, and ```!``` respectively. The syntax is straightforward, but the complexity of using logic operators in code comes with you as the programmer not knowing what questions and answers you need to have i.e. not knowing which logic operators you need to use.

## When to Use OR ```||```

Let's say you designed a system with two buttons and one DC motor. You want to write a code so that if either one of the two buttons is pressed, and triggers a digital HIGH or 1, the motor will move. What we have here is the perfect example of an OR logic. If Button 1 **OR** Button 2 is HIGH, then the motor is HIGH. In pseudo code, we would have the following:

```c
int b1 = Pin 1
int b2 = Pin 2
int motor = Pin 3

main loop {
if ( B1 || B2 == 1){
		motor.HIGH;
}
}
```

Notice in the pseudo code the use of "==" versus "=". Remember from your previous programming class that these two symbols means two different things, when "==" is specific for logic operations, and "=" is equating a physical value to a data type.

## When to Use AND ```&&```

Let's say this time you want to write a code so that if both one of the two buttons are pressed, then the motor will move. What we have here is the perfect example of an AND logic. If Button 1 **AND** Button 2 is HIGH, then the motor is HIGH. In pseudo code, we would have the following:

```c
main loop {
if ( B1 && B2 == 1){
		motor.HIGH;
}
}
```

## When to Use NOT ```!```

Now let's say you want to write a code so that if both of the two buttons are left unpressed, then the motor will move continuously. What we have here is the perfect example of the "!" logic. If Button 1 **AND** Button 2 is ***not*** HIGH, then the motor is HIGH. In pseudo code, we would have the following:

```c
main loop {
if ( !(B1 && B2 == 1)){
		motor.HIGH;
}
}
```

What if you wanted to write a code so that if ***only one*** of the two buttons are left unpressed, then the motor will move continuously? Then we would have if Button 1 **OR** Button 2 is ***not*** HIGH, then the motor is HIGH. In pseudo code, we would have the following:

```c
main loop {
if ( ! (B1 || B2 == 1)){
		motor.HIGH;
}
}
```

Notice here how where the ```!``` symbol is placed. It's a typically adopted process in code to write a logic and then negate it as an easy what to tell the computer and other readers of your code that you are utilizing a NOT statement. Just know that if the NOT symbol was placed anywhere else, you would end up with a different output than you probably expected. With this said, be sure to write down your pseudo code and think very carefully about what you need.
