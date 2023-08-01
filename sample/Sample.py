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

	encoded = SerializerHelper.Encode([1,2,3], format='application/json', charset='utf-8')
	decoded = SerializerHelper.Decode(encoded, format='application/json', charset='utf-8')
	print(encoded, decoded)

	encoded = SerializerHelper.Encode((4,5,6), format='application/json', charset='utf-8')
	decoded = SerializerHelper.Decode(encoded, format='application/json', charset='utf-8')
	print(encoded, decoded)

	_ = {
		'a': True,
		'b': 0,
		'c': 0.0,
		'd': 'String',
		'e': [1,2,3],
		'f': (1,2,3),
		'g': {
			'a': True,
			'b': 0,
			'c': 0.0,
			'd': 'String',
			'e': [1,2,3],
			'f': (1,2,3),
			'g': {}
		}
	}
	encoded = SerializerHelper.Encode(_, format='application/json', charset='utf-8')
	decoded = SerializerHelper.Decode(encoded, format='application/json', charset='utf-8')
	print(encoded, decoded)

	# TODO : Support DataModelObject
