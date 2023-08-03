#!/usr/bin/env python3

import sys
root_dir = f"{__file__.split('src')[0]}"
if root_dir not in sys.path:
    sys.path.append(root_dir)
from src.rl.abstraction import Policy, State, Action
from src.rl.proof_env import ProofEnv, ProofAction, ProofState, ProofEnvInfo


class GptGuidedDfsPolicy(Policy):
    def __init__(self):
        pass

    def __call__(self, env: ProofEnv) -> ProofAction:
        pass

    def update(self, state: ProofState, action: ProofAction, next_state: ProofState, reward: float, done: bool, info: ProofEnvInfo):
        pass

    def checkpoint(self):
        pass

    def clone(self):
        pass