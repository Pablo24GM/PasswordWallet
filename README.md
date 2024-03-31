# Password Wallet

I’ve always thought that people nowadays need to constantly have different types of accounts and passwords for everything in their lives, not just the main important things, like bank accounts, email addresses, health and car insurances, etc. But also, for streaming services, online shopping, social media, and so on and on. The project presented me with the opportunity to work on a program in which the user can store the many different accounts (by username or email) and their respective passwords, all in a separate text (.txt) file which content will be alphabetically sorted.

The original idea was to encrypt the text file make it only accessible through the program, and so it was like that for most of the time that took me to code my project, however, that had to change once I reached the Unit Tests part of the Final Project structure, since the libraries used (like Fernet library) and most part of the code was not build in accordance to go through the Unit Tests just like the assignment asked for.

## Characteristics

- This project presents a clean, friendly-user, main menu with 6 options in it.
- The main menu shows options such as, search for specific account and password, add a new account, edit and/or delete any existing entries, show a list just of the accounts already storage, and finally exit the program.
- This project also counts with its proper Pytest code file with specific Unit Tests for some Function defined inside project’s code.
- The programs store the accounts and passwords in a text file called “password_wallet.txt” that will be automatically created the first time the user runs the program.
- The code is structured with its “main” function as a start for the menu to shows up, then each option from that menu runs through specific functions of its own, in which within has other functions at the same time that helped me to structure the code better in accordance with the assignment’s requirements.
- For all the menu options individually, except “exit the program”, the program will search for the text file, read it and saved it as a list of dictionaries (each account and their respective password), search for what the user is looking for, show, edit or delete what the user wishes to, and finally rewrite the text file with the updated information.
- For edit and delete, the program will ask for verification from the user to ensure that this is what the user really wishes to do.
- For adding a new account & password, the program will first ask the “account” name (username or email address) to check if this one already exist, if it does, the user will be notified and instructed to search for the already existing account saved with the “Look for a password” option in the main menu.
- Contrary to the last point, if the user searches for any unsaved account, this one will be notified and instructed that such entry does not exist, and it first must be added with the “Add a new password” option in the main menu.
- Taking into consideration that this “Password Wallet” could store docents, maybe hundreds of Accounts & Passwords, the option number 5 in the menu “Show all accounts” will display a list of all accounts (only the accounts, not the passwords associated) in alphabetical order for the user to remember or check the existence of any particular account that could be looking for.

## Lessons & Thoughts throughout the process

As I first mentioned, the original idea was to make this Wallet not just a convenience to use but also a secure space to trust. I started using an original password authentication to access the program, but this would not have protected the information storage in the separated text file, so it was a futile try. Then the idea to add the Fernet library, that specializes in encrypt files and generate strong protected keys, came up. However, the addition of this library did change a lot of the code structure constructed at the very beginning.

Since Fernet was not something presented in the CS50P, the learning process was harder and more complex that I first expected, nonetheless, I believe I surpassed my own expectations, something that I am very proud of, and I also wish to credit it to CS50, since this course did settle the bases for me to understanding more about Python beyond the classroom.

Although the final result was a fully functional program, the code structure sure had a lot of room for improvement. Moreover, the deceive factor were the Unit Tests for the program’s function, that forced me to rewrite, for the third time, almost all the code, but helped me out to understand better the way of how I wanted to structure it and to see the logic of the same a lot better in my mind.
