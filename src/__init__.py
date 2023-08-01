# -*- coding: utf-8 -*-

from .Encoder import Encoder
from .Decoder import Decoder

from Liquirizia.Serializer import SerializerHelper

__all__ = (
	'Encoder',
	'Decoder',
)

SerializerHelper.Set('application/json', Encoder, Decoder)
SerializerHelper.Set('json', Encoder, Decoder)
