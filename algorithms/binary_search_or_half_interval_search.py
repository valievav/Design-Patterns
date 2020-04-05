# Binary search algorithm OR half-interval search OR logarithmic search -
# search sorted array by repeatedly dividing the search interval in half.
# Time complexity - O(log N)

import random


def guess_secret_number(nums: list, secret_number: int)->None or int:
    min_ind = 0
    max_ind = len(nums) - 1
    try_cnt = 0
    result = None

    while min_ind <= max_ind:  # if min_ind gets > max_ind - value doesn't exist in a list
        mid_ind = (min_ind + max_ind) // 2  # floor to get mid index
        guess = nums[mid_ind]
        print(f"Computer guess is: {guess}")
        try_cnt += 1

        if guess > secret_number:
            print('>> Too high')
            max_ind = mid_ind - 1  # excluding guess from search range
        elif guess < secret_number:
            print('>> Too low')
            min_ind = mid_ind + 1  # excluding guess from search range
        elif guess == secret_number:
            print(">> You've got it! Congratulations :)")
            result = guess
            break
    else:
        print('Guess is not in a list')

    print(f'Finished in {try_cnt} tries')
    return result


def main():
    nums = [x for x in range(0, 101)]
    secret_number = random.choice(nums)
    print('~~ Secret number (shhhh...): ', secret_number)

    guess_secret_number(nums, secret_number)


if __name__ == "__main__":
    main()

