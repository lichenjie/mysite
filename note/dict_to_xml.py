from xml.etree.ElementTree import Element

def dict_to_xml(tag, d):
	'''
	Turn a simple dict of key/value pairs into XML
	'''
	elem = Element(tag)
	for key, val in d.items():
		child = Element(key)
		child.text = str(val)
		elem.append(child)
	return elem

def dict_to_xml_str(tag, d):
	'''
	Turn a simple dict of key/value pairs into XML
	'''

	parts = ['<{}>'.format(tag)]
	for key, value in d.items():
		parts.append('<{0}>{1}</{0}>'.format(key, value))
	parts.append('</{}>'.format(tag))
	return ''.join(parts)
