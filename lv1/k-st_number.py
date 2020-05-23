

def solution(array: list, commands):
    for command in commands:
        trimed_array = array[command[0] - 1 : command[1]]
        trimed_array.sort()
        print(trimed_array[command[2]-1])
    answer = []
    return answer


if __name__ == "__main__":
    solution([1,5,2,6,3,7,4], [[2,5,3], [4,4,1], [1,7,3]])