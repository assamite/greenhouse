"""Plans for greenhouse scenario
"""
import numpy as np


class AppliedContext:
    """Single application context for a plan.
    """
    def __init__(self, tops, bulbs_height, fitness, ambient_lux):
        self.tops = tops
        self.bulbs_height = bulbs_height
        self.fitness = fitness
        self.ambient_lux = ambient_lux
        self.tops_mean = np.mean(self.tops)
        self.tops_std = np.std(self.tops)


class Plan:
    """Single plan (turned on bulbs) and its application contexts.
    """
    def __init__(self, bulbs_on, cost=0, applied_contexts=None):
        self.bulbs_on = bulbs_on
        self.cost = cost
        if applied_contexts is None:
            self.applied_contexts = []
        else:
            self.applied_contexts = applied_contexts

    def add_applied_context(self, tops, bulbs_height, fitness, ambient_lux=0):
        context = AppliedContext(tops, bulbs_height, fitness, ambient_lux)
        self.applied_contexts.append(context)

    def get_applied_contexts(self, min_fitness=0, ambient_lux=None, ambient_lux_range=0):
        contexts = []
        for ctx in self.applied_contexts:
            if ctx.fitness > min_fitness:
                if ambient_lux is not None:
                    if abs(ambient_lux - ctx.ambient_lux) <= ambient_lux_range:
                        contexts.append(ctx)
                else:
                    contexts.append(ctx)

        return contexts











