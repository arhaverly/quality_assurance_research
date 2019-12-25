#CSCI-642: Secure Coding Term Paper and Code

This program is a game ("game.py") that communicates with a server ("server.py"). The purpose of this game is to get the highest score with the given inputs. The personal data for the user is stored in "personal_data.txt". The program to fuzz test the game is "fuzz.py". This fuzzer uses a random approach and a random-restart hill climbing technique.

To run the game, first run `python3 server.py`. In another terminal, run `python3 game.py`. The username is "user" and the password is "pass". The encryption key is "hard_to_guess_password".

To run the fuzzer, first run `python3 server.py`. In another terminal, run `python3 fuzz.py`. This will fuzz the program using the custom fuzz program.

To compile the game code into `.pyc` compiled code, run `python3 <enter> import py_compile; py_compile.compile("game.py")`.

There are quite a few vulnerabilities in this code. The paper discusses most of these.