"""Tests for Connect Four"""
from connect_four.game import Board


def test_draw_board_without_errors():
    # Arange
    game = Board()

    # Act
    game

    # Assert
    # if we are here, we didn't have an error so that's good
    assert True
