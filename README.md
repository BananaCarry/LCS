Hello! 
I'm Bogdan Emilian,
this is a project made for Logic for Computer Science, which takes in a logical proposition, then determines and prints the truth table of it into an excel file.

To run this program, you have to import it into PyCharm. No other components needed, since everything you need is installed into this project.

After importing it into Pycharm, you have to Hit run, then compile the "Excel.py" file to get everything running.
Then, a Console will pop up on the bottom of the screen of PyCharm, where first, you will have to typa a name for the Excel file which is going to be created.
Then you will have to write down a valid logical proposition.
The only aspect you have to look for is that you will need paranthesis for every operation in the proposition, else it is going to give back an error which stops the excel from 
building, preventing a memory issue.
After compiling correctly, the Excel file will appear in the project folder, also can be seen in the left side of the PyCharm project. It can be opened just by double-clicking on it.



Some examples of valid inputs: 
((¬(P⇒Q))≡((P∨R)∧((¬P)⇒Q)))
((P≡Q)≡(¬(P⇒(¬Q))))
(((P⇒Q)∧(¬Q))∧(¬P))
((P⇒Q)⇒((Q⇒S)⇒((P∨Q)⇒R)))
(A∧B)



The valid operators are:
¬
∧
∨
≡
⇒


A downside would be that you have to enter with copy-paste each operator, but I am looking in a more efficient way to solve this in the near future.
