"""Tests for Connect Four"""
from connect_four.game import Board, NUM_COLS, NUM_ROWS, find_empty_slot


def test_draw_board_without_errors():
    # Arange
    game = Board()

    # Act
    game

    # Assert
    # if we are here, we didn't have an error so that's good
    assert True


def test_dropping_piece_in_full_column():
    # Arange
    game = Board()

    # Act and Assert
    for _ in range(NUM_ROWS):
        assert game.drop_piece(1, 'x') is True

    # full, now we cannot
    assert game.drop_piece(1, 'x') is False


def test_board_full():
    # Arange
    game = Board()

    # Act and Assert
    for _ in range(NUM_ROWS):
        for col in range(NUM_COLS):
            game.drop_piece(col, 'x')

    # full, now we cannot
    assert game.is_full() is True


def test_find_empty_slot_empty_dict():
    my_dict = {}
    assert find_empty_slot(my_dict, None) == -1


def test_find_empty_slot_normal_dict():
    my_dict = {}
    my_dict['1'] = 'first_item'
    my_dict['2'] = 'second_item'
    my_dict['3'] = None
    my_dict['4'] = None

    assert find_empty_slot(my_dict, None) == '3'


def test_find_empty_slot_full_dict():
    my_dict = {}
    my_dict['1'] = 'first_item'
    my_dict['2'] = 'second_item'

    assert find_empty_slot(my_dict, None) == -1
