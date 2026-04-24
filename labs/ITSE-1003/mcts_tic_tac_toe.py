# ------------------------------------------------------------ #
# File: mcts_tic_tac_toe.py
# Date: 2026-04-19
# Author: Florentino Baez
# Professor: Mauricio Quiroga
# Description: Monte Carlo Tree Search (MCTS) with a Tic-Tac-Toe demo.
# Explanation: Pure-stdlib implementation of the four MCTS phases (Selection via UCB1, Expansion, Simulation/rollout, Backpropagation). The same Node class works for any game/state that implements get_legal_moves / make_move / is_terminal / get_result / current_player.
# ------------------------------------------------------------ #
# Requires: standard library only

from __future__ import annotations

import argparse
import math
import random
from collections.abc import Sequence
from dataclasses import dataclass, field
from typing import Generic, Optional, Protocol, TypeVar

Move = TypeVar("Move")

# ---------------------------------------------------------------------------
# Generic game interface MCTS expects
# ---------------------------------------------------------------------------


class GameState(Protocol[Move]):
    """Minimal interface a game must expose for MCTS, parameterized by move type."""

    current_player: int  # 1 or -1 in this demo

    def get_legal_moves(self) -> Sequence[Move]: ...

    def make_move(self, move: Move) -> "GameState[Move]": ...

    def is_terminal(self) -> bool: ...

    def get_result(self, player: int) -> float:
        """Return 1.0 win, 0.5 draw, 0.0 loss from ``player``'s perspective."""
        ...


# ---------------------------------------------------------------------------
# MCTS node
# ---------------------------------------------------------------------------


@dataclass
class MCTSNode(Generic[Move]):
    state: GameState[Move]
    parent: Optional["MCTSNode[Move]"] = None
    move: Move | None = None  # move that led here from parent
    children: list["MCTSNode[Move]"] = field(default_factory=list)
    untried_moves: list[Move] = field(default_factory=list)
    visits: int = 0
    wins: float = 0.0  # accumulated reward from the perspective of state-to-move's parent

    def __post_init__(self) -> None:
        self.untried_moves = list(self.state.get_legal_moves())

    @property
    def is_fully_expanded(self) -> bool:
        return not self.untried_moves

    def best_child(self, exploration: float = math.sqrt(2)) -> "MCTSNode[Move]":
        """Pick the child with the highest UCB1 score."""
        log_n = math.log(self.visits)
        return max(
            self.children,
            key=lambda c: (c.wins / c.visits)
            + exploration * math.sqrt(log_n / c.visits),
        )

    def expand(self) -> "MCTSNode[Move]":
        """Take one untried move and create the corresponding child node."""
        move = self.untried_moves.pop()
        next_state = self.state.make_move(move)
        child: MCTSNode[Move] = MCTSNode(state=next_state, parent=self, move=move)
        self.children.append(child)
        return child

    def update(self, reward: float) -> None:
        self.visits += 1
        self.wins += reward


# ---------------------------------------------------------------------------
# MCTS search loop
# ---------------------------------------------------------------------------


def mcts_search(
    root_state: GameState[Move],
    iterations: int = 1000,
    exploration: float = math.sqrt(2),
    rng: random.Random | None = None,
) -> Move:
    """Run MCTS from ``root_state`` and return the best move."""
    rng = rng or random.Random()
    root: MCTSNode[Move] = MCTSNode(state=root_state)
    root_player = root_state.current_player

    for _ in range(iterations):
        node = root

        # 1) Selection: descend with UCB1 while fully expanded and non-terminal
        while node.is_fully_expanded and not node.state.is_terminal():
            node = node.best_child(exploration)

        # 2) Expansion: if non-terminal and has untried moves, expand one
        if not node.state.is_terminal() and node.untried_moves:
            node = node.expand()

        # 3) Simulation: random playout from this node's state
        sim_state = node.state
        while not sim_state.is_terminal():
            move = rng.choice(sim_state.get_legal_moves())
            sim_state = sim_state.make_move(move)

        reward = sim_state.get_result(root_player)

        # 4) Backpropagation. By convention each node's `wins` is the cumulative
        # reward for the player who *just moved* to reach that node — that is the
        # opponent of the player about to move at the node. The root has no
        # parent, so only its visit count matters there.
        current: MCTSNode[Move] | None = node
        while current is not None:
            current.visits += 1
            if current.parent is not None:
                if current.state.current_player != root_player:
                    current.wins += reward
                else:
                    current.wins += 1.0 - reward
            current = current.parent

    # Choose the most-visited child (robust standard choice for MCTS)
    best = max(root.children, key=lambda c: c.visits)
    assert best.move is not None
    return best.move


# ---------------------------------------------------------------------------
# Tic-Tac-Toe game implementation
# ---------------------------------------------------------------------------


@dataclass
class TicTacToe:
    board: tuple[int, ...] = (0,) * 9  # 0 empty, 1 = X, -1 = O
    current_player: int = 1  # X starts

    _LINES: tuple[tuple[int, int, int], ...] = (
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6),
    )

    def get_legal_moves(self) -> list[int]:
        if self._winner() != 0:
            return []
        return [i for i, v in enumerate(self.board) if v == 0]

    def make_move(self, move: int) -> "TicTacToe":
        if self.board[move] != 0:
            raise ValueError(f"Cell {move} is not empty")
        new_board = list(self.board)
        new_board[move] = self.current_player
        return TicTacToe(board=tuple(new_board), current_player=-self.current_player)

    def _winner(self) -> int:
        for a, b, c in self._LINES:
            s = self.board[a] + self.board[b] + self.board[c]
            if s == 3:
                return 1
            if s == -3:
                return -1
        return 0

    def is_terminal(self) -> bool:
        return self._winner() != 0 or all(v != 0 for v in self.board)

    def get_result(self, player: int) -> float:
        winner = self._winner()
        if winner == 0:
            return 0.5  # draw
        return 1.0 if winner == player else 0.0

    def render(self) -> str:
        glyphs = {0: ".", 1: "X", -1: "O"}
        cells = [glyphs[v] for v in self.board]
        rows = [" ".join(cells[i : i + 3]) for i in range(0, 9, 3)]
        return "\n".join(rows)


# ---------------------------------------------------------------------------
# Demo
# ---------------------------------------------------------------------------


def play_self_game(iterations: int = 1000, seed: int | None = None) -> None:
    """MCTS plays both sides; print the board after every move."""
    rng = random.Random(seed)
    state: TicTacToe = TicTacToe()
    move_no = 0
    print("Starting MCTS self-play (X vs O), iterations per move:", iterations)
    print(state.render())
    print()

    while not state.is_terminal():
        move = mcts_search(state, iterations=iterations, rng=rng)
        state = state.make_move(move)
        move_no += 1
        glyph = "O" if state.current_player == 1 else "X"  # the one who just moved
        print(f"Move {move_no} by {glyph} -> cell {move}")
        print(state.render())
        print()

    winner = state._winner()
    if winner == 1:
        print("Result: X wins")
    elif winner == -1:
        print("Result: O wins")
    else:
        print("Result: draw")


def _parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description=play_self_game.__doc__)
    p.add_argument(
        "--iterations",
        type=int,
        default=1000,
        help="MCTS iterations per move (default: 1000)",
    )
    p.add_argument(
        "--seed",
        type=int,
        default=None,
        help="Random seed for reproducibility (default: random)",
    )
    return p.parse_args()


if __name__ == "__main__":
    args = _parse_args()
    play_self_game(iterations=args.iterations, seed=args.seed)
