import ast
import operator as op
from .base import Bot

OPS = {ast.Add: op.add, ast.Sub: op.sub, ast.Mult: op.mul, ast.Div: op.truediv,
       ast.Pow: op.pow, ast.USub: op.neg, ast.Mod: op.mod}


def _eval(node):
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return node.value
    if isinstance(node, ast.BinOp) and type(node.op) in OPS:
        return OPS[type(node.op)](_eval(node.left), _eval(node.right))
    if isinstance(node, ast.UnaryOp) and type(node.op) in OPS:
        return OPS[type(node.op)](_eval(node.operand))
    raise ValueError("not arithmetic")


class MathBot(Bot):
    """Exact arithmetic: '2+3*4' -> 14. Same answer every time."""
    name = "math"

    def handle(self, text):
        try:
            return _eval(ast.parse(text.strip(), mode="eval").body)
        except Exception:
            return None
