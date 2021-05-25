from dataclasses import dataclass
from itertools import takewhile
from typing import List

from ecl_data_io.errors import ParsingError

from .subparser import SubParser


@dataclass
class OneLineRecord:
    message: str


class OneLineSubParser(SubParser):
    def __init__(self, keyword):
        self._keyword = keyword

    @property
    def keyword(self):
        return self._keyword

    def parse(self, super_parser, lines):
        try:
            yield OneLineRecord(next(lines))
        except StopIteration as e:
            raise ParsingError(
                f"Reached end of file while parsing {self.keyword}"
            ) from e