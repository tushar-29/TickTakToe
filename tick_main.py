BOARD_STRUCT = [
    [" ", " ", "1", " ", "2", " ", "3"],
    [" ", "_", "_", "_", "_", "_", "_", "_"],
    ["1", "|", "", "|", "", "|", "", "|"],
    [" ", "|", "_", "|", "_", "|", "_", "|"],
    ["2", "|", "", "|", "", "|", "", "|"],
    [" ", "|", "_", "|", "_", "|", "_", "|"],
    ["3", "|", "", "|", "", "|", "", "|"],
    [" ", "|", "_", "|", "_", "|", "_", "|"]
]


def print_board_is():
    count = 0
    for row in BOARD_STRUCT:
        for cell in row:
            if cell == "":
                count += 1
            if not cell:
                print(" ", end="\t")
            else:
                print(cell, end="\t")
            if cell == "":
                count += 1
        print("\n", end="")
    print("\n")
    if count == 0:
        return True


def value_checker(str_numb):
    if not str_numb.isdigit():
        return False
    str_numb = int(str_numb)
    if (str_numb == 1) | (str_numb == 2) | (str_numb == 3):
        return str_numb
    return False


def get_index(dimension, ply_no):
    ind = input(f"Enter the {dimension} no.  for player {ply_no} : ").strip().strip(" ")
    index = value_checker(ind)
    if index:
        return index
    else:
        print(f"\n\nERROR: Incorrect {dimension} number by player {ply_no}, TRY AGAIN ")
        return get_index(dimension=dimension, ply_no=ply_no)


def is_blank(row_ind, col_ind):
    value = BOARD_STRUCT[row_ind][col_ind]
    if value == "":
        return True
    return False


def is_formed():
    all_list = []
    for i in range(2, 7, 2):
        for j in range(2, 7, 2):
            all_list.append(BOARD_STRUCT[i][j])
    if ((all_list[0] == all_list[1] == all_list[2]) | (all_list[0] == all_list[4] == all_list[8])) and (all_list[0] != ""):
        return True,
    elif (all_list[0] == all_list[3] == all_list[6]) | (all_list[3] == all_list[4] == all_list[5]) and (all_list[3] != ""):
        return True
    elif ((all_list[2] == all_list[5] == all_list[8]) | (all_list[2] == all_list[4] == all_list[6])) and (all_list[2] != ""):
        return True
    elif (all_list[1] == all_list[4] == all_list[7]) and (all_list[1] != ""):
        return True
    else:
        return False


def insert_value(ply_no):
    row_index = get_index(dimension="row", ply_no=ply_no) * 2
    col_index = get_index(dimension="column", ply_no=ply_no) * 2
    is_empty = is_blank(row_ind=row_index, col_ind=col_index)
    if is_empty:
        if ply_no == 1:
            BOARD_STRUCT[row_index][col_index] = "X"
        else:
            BOARD_STRUCT[row_index][col_index] = "O"
    else:
        print("\n\nERROR: Value has already been entered, TRY AGAIN")
        insert_value(ply_no)


def main_loop():
    print("WELCOME TO TIC TAC TOE GAME\n")
    ply = False
    while True:
        i = int(ply) + 1
        is_board_full = print_board_is()
        insert_value(i)
        game = is_formed()
        if game:
            print("_____________________________________________")
            print(f"\t\tGAME OVER\n\t Player {i} Won The Game")
            print_board_is()
            print("______________________________________________")
            break
        if is_board_full:
            print("______________________________________________")
            print("\nGAME IS DRAW\n")
            print_board_is()
            print("_____________________________________________")
            break
        ply = not ply
    input("\n\nPRESS ANY KEY TO PLAY AGAIN\n\n")
    main_loop()


if __name__ == "__main__":
    main_loop()
