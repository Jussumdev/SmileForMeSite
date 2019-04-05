   ___                        .___          .                 
 .'   `. \,___,   ___  , __   /   \   ___   |   , _ , _       
 |     | |    \ .'   ` |'  `. |,_-'  /   `  |   |' `|' `.     
 |     | |    | |----' |    | |     |    |  |   |   |   |     
  `.__.' |`---' `.___, /    | /     `.__/| /\__ /   '   /     
         \
—————————————————————————————————————————————————————————
	OpenPalm Password Generator
	     Gabriel Lane, 2017


	OpenPalm is the result of a challenge I gave myself: create a strong self-encrypted password generator that would NOT store my passwords locally. My solution was to create a program that could procedurally generate passwords on the fly, and would always return the same password given the same Personal Key and website input. This allows a user to input the name of a website, get a password for that site, and then find their password again by relaunching the program and entering the same website name. Instead of remembering a different password for every site, you can simply remember a single Personal Key, used to generate and regenerate any site password you desire. The program can also create and save text files containing your inputs (not your passwords, mind you) so that one can quickly check all of their website passwords at once. If someone with the wrong Personal Key opened your file, they would see the same inputs, but a set of completely different passwords. This is what makes OpenPalm so secure.

	OPPG.py now runs on Python 3. Open your terminal or command prompt, navigate to the OPPG folder, and enter “python OPPG.py”. All interactions with the program are performed using the command prompt.

	dictionary.txt is a file containing the words used by the program to generate passwords. The program can take dictionary files of any size, as long as they contain alternating words and linebreaks (Hello\nThis\nIs\nAn\nExample\n). The dictionary.txt that I have included contains ~8,000 common one or two syllable words, with expletives and proper names removed. The password generator will be stronger with a longer dictionary.txt, up to 10,000 words. After 10,000 words, additional words will not affect passwords strength
—————————————————————————————————————————————————————————
IMPORTANT: IF YOU MODIFY OR REPLACE DICTIONARY.TXT, DO IT ***BEFORE*** YOU START GENERATING PASSWORDS!!! 
—————————————————————————————————————————————————————————
Any inputs you use will no longer generate the same password once you change the dictionary file. Be prepared. Don’t modify dictionary.txt after you’ve changed your passwords. You may be unable to find your passwords again.

	Other than that, enjoy OpenPalm!