"""A compatibility layer for chemointeract."""

import sys
import types
import rdkit.Chem.Draw

if not hasattr(rdkit.Chem.Draw, "mplCanvas"):
    class DummyCanvas:
        pass
    dummy_mod = types.ModuleType("mplCanvas")
    dummy_mod.Canvas = DummyCanvas
    rdkit.Chem.Draw.mplCanvas = dummy_mod
    sys.modules["rdkit.Chem.Draw.mplCanvas"] = dummy_mod

import torch
import torchdrug.data
from torch.types import Device

__all__ = [
    "PackedGraph",
    "Graph",
]


class PackedGraph(torchdrug.data.PackedGraph):
    """A compatibility layer that implements a to() function and attribute fallbacks."""

    @property
    def data_dict(self):
        d = super().data_dict
        if "node_feature" not in d and "atom_feature" in d:
            d["node_feature"] = d["atom_feature"]
        return d

    @property
    def node_feature(self):
        if "node_feature" in self.data_dict:
            return self.data_dict["node_feature"]
        elif "atom_feature" in self.data_dict:
            return self.data_dict["atom_feature"]
        return self.atom_feature

    def to(self, device: Device):
        """Return a copy of this packed graph on the given device."""
        if isinstance(device, str):
            if device == "cpu":
                return self.cpu()
            elif device == "cuda":
                return self.cuda()
            else:
                raise NotImplementedError(f"{self.__class__.__name__}.to() is not implemented for string: {device}")
        elif isinstance(device, torch.device):
            if device.type == "cpu":
                return self.cpu()
            elif device.type == "cuda":
                return self.cuda()
            else:
                raise NotImplementedError
        else:
            raise TypeError


class Graph(torchdrug.data.Graph):
    """A compatibility layer that makes appropriate packed graphs."""

    packed_type = PackedGraph