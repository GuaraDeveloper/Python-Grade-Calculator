# Grade Calculator (Python)

[Leia em português](README.pt-br.md)

A terminal program that calculates the average of your grades and tells you whether you are approved, in recovery, or failed.

## How it works

- You choose how many grades to enter (for example, 3 quarterly grades or 4 tests).
- Each grade must be a number between 0 and 10. Commas are accepted (6,5). Invalid input is asked again.
- The program shows the average and the status:
  - average 7 or above: **Approved**
  - average from 5 to below 7: **Recovery**
  - average below 5: **Failed**

The 7 and 5 limits can be changed in the code to match your school's rules.

## How to run

You need Python 3 installed.

```
python calculadora_notas.py
```

You can also paste the code into [Google Colab](https://colab.research.google.com) and run it there.

## Concepts practiced

Functions, `while` loops, `try/except`, input validation, lists, `sum` and `len`, conditionals (`if/elif/else`), and string formatting.

## Notes

- College project developed at Anhanguera in 2025. It combines two earlier versions into one program.
- The program text is in Portuguese.
