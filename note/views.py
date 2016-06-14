from django.shortcuts import render
import time
from dict_to_xml import dict_to_xml, dict_to_xml_str
from xml.etree.ElementTree import tostring
from collections import OrderedDict
from chardet import detect
# Create your views here.
cur_date = time.strftime("%Y%d")
cur_time = time.strftime("%H%M%S")
TradeCode = '11001'
MktCode = 'BJGD0000'
#ms_len = '00100'
BankId = 'A14000'
MarketSerial = time.strftime('%Y%d%H%M%S')
Summary1 = ''
Summary2 = ''
#xml 头
xml_head = '<?xml version="1.0" encoding="GBK"?>'

#xml Pub 字段
Pub = OrderedDict([('Version', 'V1.0'), ('TradeCode', TradeCode), ('Date', cur_date), ('Time', cur_time), ('EntWay', '我们'), ('BankId', BankId), ('TradeSrc', 'I'), ('MktCode', MktCode)])
#xml Serail 字段
Serial = {'MarketSerial': MarketSerial}
#xml MoneyKind字段
MoneyKind = {'MoneyKind': 'CNY'}
#xml SummaryInfo字段
SummaryInfo = OrderedDict([('Summary1', Summary1),('Summary2', Summary2)])


#组装成xml
xml_body = (dict_to_xml_str('Pub', Pub) + dict_to_xml_str('Serial', Serial) + dict_to_xml_str('MoneyKind', MoneyKind) + dict_to_xml_str('SummaryInfo', SummaryInfo))
#xml_serial = dict_to_xml_str('')
xml = ( xml_head + '<root>' + xml_body + '</root>').encode('gbk')
#print (xml)

#组装包头
#xml = xml.encode('gbk')
ms_len = '{:0>5}'.format(str(len(xml)))
msg_head = ('X1.0' + ms_len + 'R' + TradeCode + MktCode + '00' + ' '*8 + '00000000').encode('gbk')
#print (msg_head)

#组装成报文
message = msg_head + xml
print (message.decode('gbk'))
