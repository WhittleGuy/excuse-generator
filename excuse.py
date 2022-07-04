#!bin/bash/python

################################################################################
# Programmer: Brandon Whittle
# File: excuse.py
# Purpose: Make fun of Allie
# Date: January 30, 2022
################################################################################

import random

REASONS = [
    'I have a terrible stomachache.',
    'my head is pounding.',
    'I did not get enough sleep last night.',
    'my dog ate my homework.',
    'I got too busy with EOM.',
    'I am playing ah-pex.',
    'I bullied myself too hard.',
    'no zero days.',
    'I was watching anime and the next episode started automatically.',
    'I have only eaten one piece of granola and a raisin.',
    'I have only eaten half a bagel and a protein bar.',
    'my car battery exploded.',
    'c\'est la vie.',
    'my bed looked a little *too* comfy.',
]


def main():
    print(
        f"I'm sorry, I won't be able to make it to <PRIOR OBLIGATION> because {random.choice(REASONS)}")


if __name__ == '__main__':
    main()
