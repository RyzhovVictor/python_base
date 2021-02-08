import random


def get_all_answer():
    ans = []
    for i in range(10000):
        tmp = str(i).zfill(4)
        if len(set(map(int, tmp))) == 4:
            ans.append(list(map(int, tmp)))
    return ans


def get_one_answer(ans):
    num = random.choice(ans)
    return num


def check(nums, true_nums):
    bulls, cows = 0, 0
    for i, num in enumerate(nums):
        if num in true_nums:
            if nums[i] == true_nums[i]:
                bulls += 1
            else:
                cows += 1
    return bulls, cows
