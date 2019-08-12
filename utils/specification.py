from dataclasses import dataclass
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class Specification:
    name: str
    pingUrl: str
    description: str = None
    interval: int = 10
    waitTime: int = 10

