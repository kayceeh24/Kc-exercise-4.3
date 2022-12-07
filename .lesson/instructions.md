# Exercise 4.3 - Bank Machine

In this assignment, you will create a program that gets a list of deposits and withdrawals and reports on the net result.

## Requirements

Write a program that asks the user to enter a list of deposits to and withdrawals from a bank account (see samples below).
* For the first question, if the user doesn't input `"D"` or `"W"`, the program should print `Invalid choice! Try again.` and keep asking until a valid choice is entered.

The program should total the deposits and the withdrawals and print them at the end of the program with comma-separated thousands and rounded to 2 decimal places.

Finally, the program should calculate the net change (deposits minus withdrawals) and print that out with comma-separated thousands and rounded to 2 decimal places.

**Sample Execution #1**

```
How many transactions are there? 3
Is transaction 1 a deposit or withdrawal? [D/W] D
How much is being deposited? 500
Is transaction 2 a deposit or withdrawal? [D/W] W
How much is being withdrawn? 300
Is transaction 3 a deposit or withdrawal? [D/W] W
How much is being withdrawn? 400

Deposits: $500.00
Withdrawals: $700.00
Net Change: $-200.00
```

**Sample Execution #2**

```
How many transactions are there? 1
Is transaction 1 a deposit or withdrawal? [D/W] not
Is transaction 1 a deposit or withdrawal? [D/W] A
Is transaction 1 a deposit or withdrawal? [D/W] valid
Is transaction 1 a deposit or withdrawal? [D/W] choice
Is transaction 1 a deposit or withdrawal? [D/W] D
How much is being deposited? 12345.67

Deposits: $12345.67
Withdrawals: $0.00
Net Change: $12345.67
```

## Submitting

When you are finished, push your code to GitHub.  Submit it on [Gradescope](gradescope.com) where it will be graded:
* Correctness - 80% (automatic)
* Style - 20% (manual - see [Style Guide](https://mrdevet.github.io/ICS3C/assignments/Style-Guide/))

## Resources

The following lessons will be helpful with this exercise:

* **[Loops and Data](https://mrdevet.github.io/ICS3C/essentials/4-while-loops/2-Loops-and-Data/)**
  * [Augmented Assignment](https://mrdevet.github.io/ICS3C/essentials/4-while-loops/2a-Augmented-Assignment/)
  * [Looping Input](https://mrdevet.github.io/ICS3C/essentials/4-while-loops/2b-Looping-Input/)
  * [Tallying and Totaling](https://mrdevet.github.io/ICS3C/essentials/4-while-loops/2c-Tallying-and-Totaling/)
