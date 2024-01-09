def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = []
    w = weight
    time = 0
    
    while True: 
        time += 1
        
        if len(bridge) != 0 and time - bridge[0][0] == bridge_length:
            x = bridge.pop(0)
            w += x[1]
        
        if len(truck_weights) != 0 and truck_weights[0] <= w:
            x = truck_weights.pop(0)
            bridge.append([time, x])
            w -= x
        
        if len(truck_weights) == 0 and len(bridge) == 0:
            answer = time
            break