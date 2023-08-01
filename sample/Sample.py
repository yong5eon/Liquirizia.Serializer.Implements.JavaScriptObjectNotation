# -*- coding: utf-8 -*-

from Liquirizia.Serializer import SerializerHelper
import Liquirizia.Serializer.Implements.JavaScriptObjectNotation


if __name__ == '__main__':

  encoded = SerializerHelper.Encode(True, format='application/json', charset='utf-8')
  decoded = SerializerHelper.Decode(encoded, format='application/json', charset='utf-8')
  print(encoded, decoded)

  encoded = SerializerHelper.Encode(0, format='application/json', charset='utf-8')
  decoded = SerializerHelper.Decode(encoded, format='application/json', charset='utf-8')
  print(encoded, decoded)

  encoded = SerializerHelper.Encode(0.0, format='application/json', charset='utf-8')
  decoded = SerializerHelper.Decode(encoded, format='application/json', charset='utf-8')
  print(encoded, decoded)

  encoded = SerializerHelper.Encode('String', format='application/json', charset='utf-8')
  decoded = SerializerHelper.Decode(encoded, format='application/json', charset='utf-8')
  print(encoded, decoded)

  encoded = SerializerHelper.Encode([], format='application/json', charset='utf-8')
  decoded = SerializerHelper.Decode(encoded, format='application/json', charset='utf-8')
  print(encoded, decoded)

  encoded = SerializerHelper.Encode((), format='application/json', charset='utf-8')
  decoded = SerializerHelper.Decode(encoded, format='application/json', charset='utf-8')
  print(encoded, decoded)

  encoded = SerializerHelper.Encode({}, format='application/json', charset='utf-8')
  decoded = SerializerHelper.Decode(encoded, format='application/json', charset='utf-8')
  print(encoded, decoded)

  # TODO : Support DataModelObject
