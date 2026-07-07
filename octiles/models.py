import os
from dataclasses import dataclass
from typing import Self


COLORS = {
    "red": "\033[91m",
    "green": "\033[92m",
    "yellow": "\033[93m",
    "cyan": "\033[96m",
    "magenta": "\033[95m",
    "reset": "\033[0m",
}


def colored(text: str, color: str) -> str:
    return f"{COLORS.get(color, '')}{text}{COLORS['reset']}"


@dataclass
class DiffResult:
    removed: list
    new: list
    equals: dict
    unequals: dict

    @classmethod
    def create_empty(cls) -> Self:
        return cls(removed=[], new=[], equals={}, unequals={})

    def __str__(self) -> str:
        return self.pretty(color=True, verbose=False)

    def pretty(self, color: bool = True, verbose: bool = False, max_items: int = 10) -> str:
        def c(text: str, color_name: str) -> str:
            return colored(text, color_name) if color else text

        def shorten_path(path: str) -> str:
            if verbose:
                return path
            dirname, basename = os.path.split(path)
            parent = os.path.basename(dirname)
            return os.path.join(parent, basename) if parent else basename

        def format_list(lst: list, label: str, color_name: str, symbol: str) -> str:
            if not lst:
                return f"{c(symbol, color_name)} {c(label, color_name)} (0): {c('(пусто)', 'reset')}"
            lines = [f"{c(symbol, color_name)} {c(label, color_name)} ({len(lst)}):"]
            for idx, item in enumerate(lst):
                if idx >= max_items:
                    lines.append(f"  {c('... и ещё ' + str(len(lst) - max_items), 'reset')}")
                    break
                lines.append(f"  {shorten_path(item)}")
            return "\n".join(lines)

        def format_dict(dct: dict, label: str, color_name: str, symbol: str) -> str:
            if not dct:
                return f"{c(symbol, color_name)} {c(label, color_name)} (0): {c('(пусто)', 'reset')}"
            lines = [f"{c(symbol, color_name)} {c(label, color_name)} ({len(dct)}):"]
            for idx, (key, (path_a, path_b)) in enumerate(dct.items()):
                if idx >= max_items:
                    lines.append(f"  {c('... и ещё ' + str(len(dct) - max_items), 'reset')}")
                    break
                lines.append(f"  {key} ->")
                lines.append(f"    A: {shorten_path(path_a)}")
                lines.append(f"    B: {shorten_path(path_b)}")
            return "\n".join(lines)

        parts = [
            c("═══════════════════════════════════════════════════════════════════", "magenta"),
            format_list(sorted(self.removed), "Удалены", "red", "-"),
            format_list(sorted(self.new), "Новые", "green", "+"),
            format_dict(dict(sorted(self.equals.items())), "Равны", "cyan", "="),
            format_dict(dict(sorted(self.unequals.items())), "Различаются", "yellow", "≠"),
            c("═══════════════════════════════════════════════════════════════════", "magenta"),
        ]
        return "\n".join(parts)
