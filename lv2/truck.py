def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge_queue = []   # (<truck_second, truck_weight>)
    seconds = 0
    truck_index = 0
    temp_truck_weights = []
    for item in truck_weights:
        temp_truck_weights.append(item)

    while True:
        seconds += 1

        truck_weights

        front_waiting_truck_of_weight = truck_weights[truck_index]
        if verify_income_truck(weight, bridge_queue, front_waiting_truck_of_weight):
            bridge_queue.append((0, front_waiting_truck_of_weight))
            truck_index += 1

        seconds += 1

    for i in range(len(truck_weights)):

        print(truck_weights[i])
    return answer



def verify_income_truck(bridge_weight, bridge_queue, truck_weight):
    sum = 0
    for e in bridge_queue:
        sum += e
    return sum + truck_weight <= bridge_weight

if __name__ == '__main__':
    solution(2, 10, [7,4,5,6])