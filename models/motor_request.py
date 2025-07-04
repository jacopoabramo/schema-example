# generated by datamodel-codegen:
#   filename:  motor_request.json
#   timestamp: 2025-07-01T13:14:56+00:00

from __future__ import annotations

from typing import List

from pydantic import BaseModel


class Stepper(BaseModel):
    stepperid: int
    position: int
    speed: int
    isabs: int
    isaccel: int
    accel: int


class Motor(BaseModel):
    steppers: List[Stepper]


class Model(BaseModel):
    task: str
    qid: int
    motor: Motor
