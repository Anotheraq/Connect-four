import unittest
from GameLogic.ConnectFourLogic import ConnectFourClassic
from Exceptions.ImpossibleMoveException import ImpossibleMoveException


class ConnectFourTest(unittest.TestCase):

    def setUp(self):
        self.game = ConnectFourClassic()

    def test_should_CheckIfBoardContainTwoCoins_when_TwoCoinsDropped(self):
        # given

        # when
        self.game.drop_move(0)
        self.game.change_turns()
        self.game.drop_move(1)
        expected_board = [[0 for i in range(7)] for i in range(6)]
        expected_board[0][0] = 1
        expected_board[0][1] = 2

        # then
        self.assertEqual(self.game.board, expected_board)

    def test_should_ReturnTrue_when_PlayerOneWonByVerticalLine(self):
        # given
        self.game.board = [[1, 2, 0, 0, 0, 0, 0],
                           [1, 2, 0, 0, 0, 0, 0],
                           [1, 2, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0]]

        # when
        self.game.drop_move(0)
        is_player_one_winning = self.game.kto_wygral(1)

        # then
        self.assertTrue(is_player_one_winning)

    def test_should_ReturnTrue_when_PlayerOneWonByHorizontalLine(self):
        # given
        self.game.board = [[1, 1, 1, 0, 0, 0, 0],
                           [2, 2, 2, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0]]

        # when
        self.game.drop_move(3)
        is_player_one_winning = self.game.kto_wygral(1)

        # then
        self.assertTrue(is_player_one_winning)

    def test_should_ReturnTrue_when_PlayerOneWonByDiagonalLine(self):
        # given
        self.game.board = [[1, 2, 1, 2, 0, 0, 0],
                           [0, 1, 2, 2, 0, 0, 0],
                           [0, 0, 1, 1, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0]]

        # when
        self.game.drop_move(3)
        is_player_one_winning = self.game.kto_wygral(1)

        # then
        self.assertTrue(is_player_one_winning)

    def test_should_ReturnTrue_when_Draw(self):
        # given
        self.game.board = [[2, 2, 2, 1, 2, 2, 2],
                           [1, 1, 1, 2, 1, 1, 1],
                           [2, 2, 2, 1, 2, 2, 2],
                           [1, 1, 1, 2, 1, 1, 1],
                           [2, 2, 2, 1, 2, 2, 2],
                           [1, 1, 1, 2, 1, 1, 1]]

        # when
        is_game_tied = self.game.is_board_full()

        # then
        self.assertTrue(is_game_tied)

    def test_should_ReturnTrue_when_PlayerOneWonByLineThatLongerThanFour(self):
        # given
        self.game.board = [[1, 1, 1, 0, 1, 1, 1],
                           [2, 2, 2, 0, 2, 2, 2],
                           [0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0]]

        # when
        self.game.drop_move(3)
        is_player_one_winning = self.game.kto_wygral(1)

        # then
        self.assertTrue(is_player_one_winning)

    def test_should_ThrowImpossibleMoveException_when_DropIsImpossible(self):
        # given
        self.game.board = [[2, 0, 0, 0, 0, 0, 0],
                           [1, 0, 0, 0, 0, 0, 0],
                           [2, 0, 0, 0, 0, 0, 0],
                           [1, 0, 0, 0, 0, 0, 0],
                           [2, 0, 0, 0, 0, 0, 0],
                           [1, 0, 0, 0, 0, 0, 0]]

        # when

        # then
        self.assertRaises(ImpossibleMoveException, self.game.drop_move, 0)


if __name__ == "__main__":
    unittest.main()
