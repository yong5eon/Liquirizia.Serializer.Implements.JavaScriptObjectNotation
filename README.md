# Liquirizia.Serializer.Implements.JavaScriptObjectNotation
JSON 형식으로 통신하기 위한 직렬화 및 비직렬화 도구

## 사용법
```python
from Liquirizia.Serializer import SerializerHelper
import Liquirizia.Serializer.Implements.JavaScriptObjectNotation


if __name__ == '__main__':

  encoded = SerializerHelper.Encode(True, format='text/plain', charset='utf-8')
  decoded = SerializerHelper.Decode(encoded, format='text/plain', charset='utf-8')
  print(encoded, decoded)

  encoded = SerializerHelper.Encode(0, format='text/plain', charset='utf-8')
  decoded = SerializerHelper.Decode(encoded, format='text/plain', charset='utf-8')
  print(encoded, decoded)

  encoded = SerializerHelper.Encode(0.0, format='text/plain', charset='utf-8')
  decoded = SerializerHelper.Decode(encoded, format='text/plain', charset='utf-8')
  print(encoded, decoded)

  encoded = SerializerHelper.Encode('String', format='text/plain', charset='utf-8')
  decoded = SerializerHelper.Decode(encoded, format='text/plain', charset='utf-8')
  print(encoded, decoded)

  encoded = SerializerHelper.Encode([], format='text/plain', charset='utf-8')
  decoded = SerializerHelper.Decode(encoded, format='text/plain', charset='utf-8')
  print(encoded, decoded)

  encoded = SerializerHelper.Encode((), format='text/plain', charset='utf-8')
  decoded = SerializerHelper.Decode(encoded, format='text/plain', charset='utf-8')
  print(encoded, decoded)

  encoded = SerializerHelper.Encode({}, format='text/plain', charset='utf-8')
  decoded = SerializerHelper.Decode(encoded, format='text/plain', charset='utf-8')
  print(encoded, decoded)
```

## 개선사항
* [ ] DataModelObject 지원