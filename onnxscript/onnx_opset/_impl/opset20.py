# --------------------------------------------------------------------------
# ⚠️ WARNING - AUTO-GENERATED CODE - DO NOT EDIT ⚠️
# ⚙️ Generated by 'python -m opgen'
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
# --------------------------------------------------------------------------
# flake8: noqa
# mypy: disable-error-code=override
# pylint: disable=W0221,W0222,W0237,W0246,R0901,W0611
# --------------------------------------------------------------------------

from onnx.defs import get_schema

from onnxscript.onnx_opset._impl.opset19 import Opset19
from onnxscript.values import Op, Opset


class Opset20(Opset19):
    def __new__(cls):
        return Opset.__new__(cls, "", 20)

    def __init__(self):
        super().__init__()
