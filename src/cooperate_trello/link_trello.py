from trello import TrelloClient

# boards(ボード)の一覧を返す
def _return_board_list(boards):
    board_name_list = []
    for board in boards:
        board_name_list.append(board.name)
    return board_name_list


def trello_contents():
    client = TrelloClient(api_key='*********************', token='*********************************')
    boards = client.list_boards()
    boards_name_list = _return_board_list(boards)
    boards_string = 'と、'.join(str(x) for x in boards_name_list)
    return boards_string

#  print(trello_contents())
