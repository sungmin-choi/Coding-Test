room_number = list(map(int, list(input())))


number_set = [ 0 for _ in range (10)] 



for i in room_number:
    if i==6 or i==9:
        if number_set[6] > number_set[9]:
            number_set[9] +=1
        else:
            number_set[6] +=1
    else:
        number_set[i] +=1

print(max(number_set))

