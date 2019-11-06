import torch
from collections import OrderedDict
from catalyst.dl.experiment.supervised import SupervisedExperiment
from catalyst.dl.callbacks import (
    CriterionCallback, ConsoleLogger, CheckpointCallback, OptimizerCallback,
    RaiseExceptionCallback, TensorboardLogger
)


DEFAULT_CALLBACKS = OrderedDict([
    ('_criterion', CriterionCallback),
    ('_optimizer', OptimizerCallback),
    ('_saver', CheckpointCallback),
    ('console', ConsoleLogger),
    ('tensorboard', TensorboardLogger),
    ('exception', RaiseExceptionCallback)])


def test_defaults():
    model = torch.nn.Module()
    dataset = torch.utils.data.Dataset()
    dataloader = torch.utils.data.DataLoader(dataset)
    loaders = OrderedDict()
    loaders['train'] = dataloader

    exp = SupervisedExperiment(model=model, loaders=loaders)

    assert exp.get_callbacks("train").keys() == DEFAULT_CALLBACKS.keys()
    cbs = zip(exp.get_callbacks("train").values(), DEFAULT_CALLBACKS.values())
    for cb, klass in cbs:
        assert isinstance(cb, klass)