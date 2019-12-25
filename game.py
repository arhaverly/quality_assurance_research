'''
game
asks for a password
    checks with server for high scores
    (fuzzing)

encryption key
    gets local files
    (pen testing)

objective: get highest score
    unlimited attempts
    (fuzzing)

'''
from cryptography.fernet import Fernet
import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import math
import sys
import socket
import time

def complicated_formula(x, y, z, a, b, c):
    '''
    valid ranges of values:
    1: (0, 255)
    2: (0, 255)
    3: (0, 255)
    4: (0, 10000)
    5: (0, 10000)
    6: (0, 10000)
    2556^3*10000^3 = 1.6581375E+019 possible combinations - intractable to try all combinations
    '''
    if x < 0 or x > 255 or y < 0 or y > 255 or z < 0 or z > 255 or a < 0 or a > 10000 or b < 0 or b > 10000 or c < 0 or c > 10000:
        return -1000000

    height_plus_height_diff = 87-x
    square_of_height_without_difference = x**2
    constant_height_small = 1
    byte_offset = 254-x
    z_factored_in_scaled = 0.00001*z
    standard_deviation_length = math.sqrt(constant_height_small**z_factored_in_scaled)
    power_of_five = 125
    weight_of_person_weighted = -1*0.000001*y
    weight_of_person_bias = 22
    height_and_weight = 0.00001*x*y
    volume_weighted = 0.00001*a
    divide_this_and_another = 1/byte_offset
    variable14 = 0.00001*b
    units_of_grain_scaled = x - 127
    variance_of_grain = units_of_grain_scaled**2
    offset_the_grain = -1
    standard_deviation_of_grain_from_variance = math.sqrt(variance_of_grain + offset_the_grain)
    mL_of_water_needed = 0.00001*c
    one_mL_to_new_units = 22*22
    velocity_of_sound_in_STP = math.sqrt(343)
    constant_height_small = 2
    division_of_heights = 1/height_plus_height_diff
    power_of_five = x*0.00000001 + 121
    standard_deviation_length = standard_deviation_length + constant_height_small
    square_of_height_without_difference = square_of_height_without_difference - 200
    weight_of_person_weighted = weight_of_person_weighted*-1
    weight_of_person_weighted = weight_of_person_weighted*-2
    var1 = division_of_heights + constant_height_small + z_factored_in_scaled + power_of_five
    var2 = weight_of_person_weighted + height_and_weight + volume_weighted + divide_this_and_another
    var3 = variable14 + standard_deviation_of_grain_from_variance + mL_of_water_needed
    return var1 + var2 + var3
       
        

#fuzzing
def play():
    highest = float('-inf')
    while True:
        valid_nums = []
        user_input = input("enter 6 numbers: ")
        for item in user_input.split(' '):
            try:
                current = int(item)
                valid_nums.append(current)
            except ValueError:
                if item == 'quit':
                    return highest

        if len(valid_nums) > 5:
            complicated_output = complicated_formula(valid_nums[0], valid_nums[1], valid_nums[2], valid_nums[3], valid_nums[4], valid_nums[5])
            print(complicated_output)
            if complicated_output > highest:
                highest = complicated_output
        else:
            print("invalid input")


#pen testing
# import py_compile
# py_compile.compile("game.py")
def get_personal_data():
    password = "hard_to_guess_password"
    encoded_password = password.encode()
    salt = b'salt_'
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )

    for p in range(3):
        user_input = input("encryption key: ")
        if user_input == password:
            key = base64.urlsafe_b64encode(kdf.derive(encoded_password))
            f = Fernet(key)
            file = open("data.txt", "rb")
            encrypted = file.readline()
            decrypted = f.decrypt(encrypted)
            print(decrypted.decode())

            return

        else:
            print("encryption key incorrect")

    print("invalid encryption key. exiting...")
    sys.exit(0)


def password_authentication():
    host = ''
    port = 20020
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))

        for p in range(3):
            username = input("username: ")
            password = input("password: ")
            print("\033[A", end="")
            print("password: ", end="")
            for c in password:
                sys.stdout.write(' ')
            print()
            total_string = username + " " + password
            s.sendall(total_string.encode())
            time.sleep(1)
            recieved = s.recv(1024).decode()

            if len(recieved) > 0:
                if recieved[0] == '1':
                    print("Welcome!")
                    return True

            print("password incorrect")

    print("You shall not pass[word]!")
    sys.exit(0)


def main():
    password_authentication()
    get_personal_data()
    highest = play()
    print("High score:", highest)

if __name__ == '__main__':
    main()