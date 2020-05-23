def solution(numbers: list):
    answer = ''
    number_str = []
    for i, e in enumerate(numbers):
        st = str(e)
        number_str.append([st * 3, i])
    
    number_str.sort(reverse=True)
    for i, e in enumerate(number_str):
        index = e[1]
        answer += str(numbers[index])
    return '0' if answer[0] == 0 else answer 


if __name__ == "__main__":
    answer = solution([6, 10, 2])
    print(answer)
    answer = solution([3, 30, 34, 5, 9])
    print(answer)
