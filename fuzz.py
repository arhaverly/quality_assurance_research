import pexpect
import random
import time

child = pexpect.spawn("python3 game.py")

inputs = [0, 0, 0, 0, 0, 0]
rand_low = 0
rand_high = 255
breaking_values = []



def get_score():
    global child
    child.sendline(str(inputs[0]) + " " + str(inputs[1]) + " " + str(inputs[2]) + " " + str(inputs[3]) + " " + str(inputs[4]) + " " + str(inputs[5]))
    child.expect([pexpect.TIMEOUT, "enter 6 numbers: ", pexpect.EOF])

    str_before = child.before.decode()
    str_before = str_before.replace('\r\n', ' ')
    before_split = str(str_before).split(' ')
    score = before_split[-2:][0]

    if len(before_split) > 8:
        print("Inputs that cause error: ", inputs)
        child.sendline("quit")
        child = pexpect.spawn("python3 game.py")
        login()
        return "zero"

    return score

def climb():
    global inputs

    for n in range(100):
        #find the best value to change
        change = 1
        best = get_score()
        climbed = False
        best_inputs = [inputs[0], inputs[1], inputs[2], inputs[3], inputs[4], inputs[5]]
        if(best == "zero"):
            return True

        for i in range(len(inputs)):
            for diff in [-1*change, change]:
                inputs[i] = inputs[i] + diff
                score = get_score()
                if score == "zero":
                    print("breaking values: ", inputs)
                    breaking_values.append(inputs)
                    return

                if float(score) > float(best):
                    best = score
                    best_inputs = [inputs[0], inputs[1], inputs[2], inputs[3], inputs[4], inputs[5]]
                    climbed = True

                inputs[i] = inputs[i] - diff

        if climbed is not True:
            return best

        inputs = best_inputs

    return best


def random_restart_hill_climb():
    print("climbing...")
    global inputs

    counter = 0
    while counter < 1000:
        for i in range(3):
            inputs[i] = random.randint(0, 255)
        for i in range(3, 6):
            inputs[i] = random.randint(0, 10000)

        climb()
        
        if len(breaking_values) > 3:
            return breaking_values

        counter += 1


def random_fuzz():
    print("random")
    global inputs
    starting_len = len(breaking_values)

    counter = 0
    while counter < 10000:
        for i in range(3):
            inputs[i] = random.randint(0, 255)
        for i in range(3, 6):
            inputs[i] = random.randint(0, 10000)

        get_score()
        
        if len(breaking_values) > starting_len + 3:
            return breaking_values

        counter += 1


def login():
    global child
    child.expect("username: ")

    child.sendline("user")
    child.expect("password: ")

    child.sendline("pass")
    child.expect("encryption key:")

    child.sendline("hard_to_guess_password")
    child.expect([pexpect.TIMEOUT, "enter 6 numbers: ", pexpect.EOF])


def main():
    login()
    print(random_restart_hill_climb())
    print(random_fuzz())




if __name__ == "__main__":
    main()