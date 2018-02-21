"""Tests for Connect Four"""
from connect_four.game import Board, NUM_ROWS


def test_draw_board_without_errors():
    # Arange
    game = Board()

    # Act
    game

    # Assert
    # if we are here, we didn't have an error so that's good
    assert True


def test_fill_board_column():
    # Arange
    game = Board()

    # Act and Assert
    for _ in range(NUM_ROWS):
        assert game.drop_piece(1, 'x') is True

    # full, now we cannot
    assert game.drop_piece(1, 'x') is False
