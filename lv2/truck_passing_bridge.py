from queue import Queue

def solution(bridge_length: int, weight: int, truck_weights: list):
    passed_trucks = []
    bridge_queue = Queue(bridge_length)  # Queue( )
    bridge_weight = 0   # 현재 다리가 견디고 있는 하중
    seconds = 0         # 지난 시간
    truck_index = 0     # 다리에 진입할 대기중인 트럭의 인덱스
    temp_truck_weights = [] 
    # for item in truck_weights:
    #     temp_truck_weights.append(item)

    while True:
        # 1. 1초가 지나고
        seconds += 1  # 반복문이 지날때마다 1초가 지난다.
        
        # 2. 다리에 진입한 트럭중 1초가 지남으로써 다리를 통과하는 트럭 처리
        # 3. 나머지 다리에 진입한 트럭의 1초 지남을 처리
        just_came_out_truck_weight = 0
        if bridge_queue.full():
            just_came_out_truck_weight = bridge_queue.get()
            if just_came_out_truck_weight != 0:
                bridge_weight -= just_came_out_truck_weight
                passed_trucks.append(just_came_out_truck_weight)

        # 다리에 트럭이 들어설려면
        # 다리가 버티고 있는 하중 + 다음 트럭 무게 < 버틸수있는 하중 AND 
        if truck_index < len(truck_weights) and bridge_weight + truck_weights[truck_index] <= weight:
            next_truck_weight = truck_weights[truck_index]
            bridge_queue.put(next_truck_weight)
            bridge_weight += next_truck_weight
            truck_index += 1
        else:
            # 트럭이 들어올 수 없다면 의미없는 값 0을 넣어 트럭이 다리를 지나는 중임을 표시
            if not bridge_queue.full(): #and just_came_out_truck_weight == 0:
                bridge_queue.put(0)

        
                
        # 모든 트럭이 다리를 지나왔다면 반복문을 그만한다.
        if len(passed_trucks) == len(truck_weights):
            break
    
    return seconds


if __name__ == '__main__':
    answer = solution(2, 10, [7, 4, 5, 6])
    print(answer)
    answer = solution(100, 100, [10])
    print(answer)
    answer = solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10])
    print(answer)