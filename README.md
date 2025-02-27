# Finance-Tracker
This financal tracker is a unser friendly way to keep track of your transactions, expenses, income, and your balance. It includes many features such as adding and removing transactions, updating transactions, viewing transactions, view balance, and view summary. In this file I will explain how all of the options work and what they do, as well as what some of the main functions, and the Libraries used as well as the documentation of any open-source or copyright materials used.


When you first run the program you will be brought to a menu that looks like this:

1. Add Transaction

2. Update Transaction

3. Delete Transaction

4. View Balance

5. View Transactions

6. View Summary

7. Exit

To use the option you wishing to use, its as simple as clicking the number that preceeds the function description.\

-In order to Add A Transaction type 1, it does exactly what it sounds like it would do, it allows you to add transactions. The first thing you will be asked to do when selecting the Add Transaction option will be a amount of money, once entered it will then ask for a description, then it will prompt you to add a date that must be a valid date in this format YYYY-MM-DD (year - month - date). If its something like 2025-25-45 it will give you a error becuase it did not follow the proper format. Finally, you will be asked whether its a income transaction or expese transaction, it is case sensitive so be sure the its all lowercase and spelled properly.

- In order to update a transaction type the number 2, it will show a list of all of the current transactions. You will be prompted to select the #/index of the transaction you want to edit, then edit the details you want to edit. If you dont want to edit a certian part of the transaction press enter to skip.

-  In order to delete a transaction type in the number 3, it will show a list of all of the current transactions. Then, all you have to do is enter the corresponding index or number of the transaction you wish to delete.

-  To view your balance you would type the number 4 in and it will show you remaining balance by calculating you income - expenses which would equal your balance. If you lost money or are in debt it will show your balance as a negitive number.

-  To view your transactions type in the nummber 5 and it will show you a list of all your current transactions. If you had preiviously updated or deleted a transaction those changes will show.

-  If your trying to view your summary simply type in the # 6. When you do that you will see something like this, "Total Income: $697.00 | Total Expenses: $0.00" it will show your total amount of income and your total amount of expenses on 2 seperate lines.

-  To exit the program all you have to do is type 7 and you will se something that says "Goodbye 👋" and the program will close.

  Libraries and Template used:
datetime - This is used to format dates adn times. For this specific program I used this module in order to allow users to input the dates of the transactions made.
   
