def check(player_name,list):
    if len(list)==3:
        if list[0]+list[1]+list[2]==15:
            print(player_name," is the winner\n the game is over.")
            exit()
    elif len(list)==4:
        if list[0]+list[1]+list[3]==15 or list[0]+list[2]+list[3]==15 or list[1]+list[2]+list[3]==15 :
            print(player_name," is the winner\n the game is over.")
            exit()
    else:
        if list[0]+list[1]+list[4]==15 or list[0]+list[2]+list[4]==15 or list[0]+list[3]+list[4]==15 or list[2]+list[3]+list[4]==15 or list[1]+list[3]+list[4]==15 or list[1]+list[2]+list[4]==15 :
            print(player_name," is the winner\nthe game is over.")
            exit()
numbers_list=[1,2,3,4,5,6,7,8,9]
player_number_1_list=[]
player_number_2_list=[]
player_number_1=input("please enter your name ")
player_number_2=input("please enter your name ")
while True:
    print("please ",player_number_1," pick up your number from this list ",numbers_list)
    a1=int(input())
    while a1 not in numbers_list:
        print("please ",player_number_1," try to pick up again ",numbers_list)
        a1=int(input())
    else:
        numbers_list.remove(a1)
        player_number_1_list.append(a1)
    if len(player_number_1_list)>=3:
        check(player_number_1,player_number_1_list)    
    print("please ",player_number_2," pick up your number from this list ",numbers_list)
    b1=int(input())
    while b1 not in numbers_list:
        print("please ",player_number_2," try to pick up again ",numbers_list)
        b1=int(input())
    else:
        numbers_list.remove(b1)
        player_number_2_list.append(b1)
    if len(player_number_2_list)>=3:
        check(player_number_2,player_number_2_list)

    





    

    