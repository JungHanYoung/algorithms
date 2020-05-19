def solution(heights):
    answer = []
    stack = []
    for index, height in enumerate(heights):
        # 스택에 데이터가 없다 >> 정답 배열에 들어가있는 값이 없다.
        if len(stack) == 0:
            answer.append(0)
            stack.append((index + 1, height))
            continue
        # 스택의 값을 비교하는데, 스택의 모든 값을 비교할 필요가 없다.
        # 왜냐하면 스택에 값을 넣기 전에 peek값과 넣을 데이터를 비교해서 넣을 데이터가 클시에만 넣으므로
        # 스택의 peek값은 왼쪽의 모든 탑 중에 제일 큰 값만을 넣기 때문이다.
        while stack:
            item = stack[-1]
            left_place = item[0]
            left_height = item[1]
            if left_height > height:
                answer.append(left_place)
                break
            else:
                stack.pop()
        # 비교되는 값이 스택의 값들보다 클때 ---> 오른쪽 제외하고 제일 큰 탑이므로 
        if len(stack) == 0:
            answer.append(0)
        stack.append((index+1, height))

    return answer



if __name__ == '__main__':
    answer = solution([6, 9, 5, 7, 4])
    print(answer)
    answer2 = solution([3, 9, 9, 3, 5, 7, 2])
    print(answer2)
    answer3 = solution([1, 5, 3, 6, 7, 6, 5])
    print(answer3)
    # print(answer)