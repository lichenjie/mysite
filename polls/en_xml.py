#coding:utf-8
from polls.models import Trade  
from django.shortcuts import render
import time
from .dict_to_xml import dict_to_xml, dict_to_xml_str
from xml.etree.ElementTree import tostring
from collections import OrderedDict
from chardet import detect
import json
#from en_xml_detail import *
def makeup_xml2(request):
  TradeCode = ''
  json_data = request.POST.get('JSON')
  request_data = json.loads(json_data)
  request_data_list = request_data[0]['data']
  for tree_two in request_data_list:
    if 'Pub' == tree_two['key'] and 'data' in tree_two:
       pub_list = tree_two['data']
       for tree_three in pub_list:
         if ('TradeCode') == tree_three['key'] and 'value' in tree_three:
           TradeCode = tree_three['value']
    if (TradeCode == '11001'):
      en_xml_11001(tree_two)
    if (TradeCode == '11002'):
      en_xml_11001(tree_two)
    if (TradeCode == '31017'):
      en_xml_31017(tree_two)
    if (TradeCode == '11005'):
      en_xml_11005(tree_two)
    if (TradeCode == '21019'):
      en_xml_21019(tree_two)
    if (TradeCode == '21019'):
      en_xml_21019(tree_two)
    if (TradeCode == '21050'):
      en_xml_21050(tree_two)
def makeup_xml(request):
  json_data = request.POST.get('JSON')
  request_data = json.loads(json_data)
  #BankId, MktCode, other = argv
  cur_date = time.strftime("%Y%m%d")
  cur_time = time.strftime("%H%M%S")
  #ms_len = '00100'
  TradeCode = ''
  BankId = ''
  MktCode = ''
  BankAcc = ''
  CustName = '李晨杰'
  OrgCode = cur_time
  BankCode = '104100000004'
  CashType = '1'
  OpenBankName = '中国银行总行'
  BankAddr = '北京'
  IsSelf = '1'
  ClientName = 'cust'
  ClientKind = '1'
  CertType = 'G'
  CertId = cur_time
  BusyLics = cur_time
  Flag1 = ''
  Flag2 = ''
  MarketSerial = time.strftime('%Y%d%H%M%S')
  FirmId =  cur_time + '00'
  TransferLimit = '200000000'
  MobiNo = '18234157658'
  Email = '1194222721@qq.com'
  Summary1 = ''
  Summary2 = ''


  xml_body = ''
  #从表单中获取pub数据
  request_data_list = request_data[0]['data']
  for tree_two in request_data_list:
    if 'Pub' == tree_two['key'] and 'data' in tree_two:
       pub_list = tree_two['data']
       for tree_three in pub_list:
         if ('TradeCode') == tree_three['key'] and 'value' in tree_three:
           TradeCode = tree_three['value']
         elif ('BankId') == tree_three['key'] and 'value' in tree_three:
           BankId = tree_three['value']
         elif ('MktCode') == tree_three['key'] and 'value' in tree_three:
           MktCode = tree_three['value']
         else:
           pass
    #从表单获取BankAcc数据
    elif 'BankAcc' == tree_two['key'] and 'data' in tree_two:
        BankAcc_list = tree_two['data']
        for tree_three in BankAcc_list:
           if ('BankAcc') == tree_three['key'] and 'value' in tree_three:
             BankAcc = tree_three['value']
           elif ('CustName') == tree_three['key'] and 'value' in tree_three:
             CustName = tree_three['value']
           elif ('BankCode') == tree_three['key'] and 'value' in tree_three:
             BankCode = tree_three['value']
           elif ('CashType') == tree_three['key'] and 'value' in tree_three:
             CashType = tree_three['value']
           elif ('OpenBankName') == tree_three['key'] and 'value' in tree_three:
             OpenBankName = tree_three['value']
           elif ('IsSelf') == tree_three['key'] and 'value' in tree_three:
             IsSelf = tree_three['value']
    elif 'Client' == tree_two['key'] and 'data' in tree_two:
        Client_list = tree_two['data']
        for tree_three in Client_list:
          if ('ClientName') == tree_three['key'] and 'value' in tree_three:
            ClientName = tree_three['value']
          elif ('ClientKind') == tree_three['key'] and 'value' in tree_three:
            ClientKind = tree_three['value']
          elif ('CertType') == tree_three['key'] and 'value' in tree_three:
            CertType = tree_three['value']
          elif ('CertId') == tree_three['key'] and 'value' in tree_three:
            CertID = tree_three['value']
          elif ('MobiNo') == tree_three['key'] and 'value' in tree_three:
            MobiNo = tree_three['value']
          elif ('Email') == tree_three['Email'] and 'value' in tree_three:
            Email = tree_three['Email']
    elif 'FlagInfo' == tree_two['key'] and 'data' in tree_two:
        FlagInfo_list = tree_two['data']
        for tree_three in FlagInfo_list:
          if('Flag1') == tree_three['key'] and 'value' in tree_three:
            Flag1 = tree_three['Flag1']
          elif ('Flag2')== tree_three['key'] and 'value' in tree_three:
            Flag2 = tree_three['Flag2']
    elif 'SummaryInfo' in tree_two['key'] and 'data' in tree_two:
        Summary_list = tree_two['data']
        for tree_three in FlagInfo_list:
           if('Summary1') == tree_three['key'] and 'value' in tree_three:
             Summary1 = tree_three['value']
           elif('Summary2') == tree_three['key'] and 'value' in tree_three:
             Summary2 = tree_three['value']
  '''
  BankAcc = request.POST.get('BankAcc')
  CustName = request.POST.get('CustName')
  BankCode = request.POST.get('BankCode')
  CashType = request.POST.get('CashType')
  OpenBankName = request.POST.get('OPenBankName')
  IsSelf = request.POST.get('IsSelf')
  ClientKind = request.POST.get('ClientKind')
  OrgCode = request.POST.get('OrgCode')
  BusyLics = request.POST.get('BusyLics')
  CertType = request.POST.get('CertType')
  CertId = request.POST.get('CertId')
  BankAddr = request.POST.get('BankAddr')
  '''
  b = Trade(tradecode = TradeCode, mktcode = MktCode, bankid = BankId, marketserial = MarketSerial)
  b.save()
  #xml 头
  xml_head = '<?xml version="1.0" encoding="GBK"?>'
  #xml Pub 字段
  Pub = OrderedDict([('Version', 'V1.0'), ('TradeCode', TradeCode), ('Date', cur_date), ('Time', cur_time), ('EntWay', 'I'), ('BankId', BankId), ('TradeSrc', 'I'), ('MktCode', MktCode)])
  #xml Serail 字段
  Serial = {'MarketSerial': MarketSerial}
  #xml MoneyKind字段
  MoneyKind = {'MoneyKind': 'CNY'}
 
  Transfer = {'TransferLimit': TransferLimit}
  FlagInfo = {}
  #xml SummaryInfo字段
  SummaryInfo = OrderedDict([('Summary1', Summary1),('Summary2', Summary2)])
  BankAcc = OrderedDict([('BankAcc', BankAcc),('CustName', CustName), ('BankCode', BankCode), ('CashType', CashType), ('OpenBankName', OpenBankName), ('BankAddr', BankAddr), ('IsSelf', IsSelf)])
  FundAcc = OrderedDict([('FirmId', FirmId), ('CustName', CustName)])
  TransferLimit = {'TransferLimit': TransferLimit}
  Client = OrderedDict([('ClientName', CustName), ('ClientKind', ClientKind),  ('BusyLics', BusyLics), ('CertType', CertType), ('CertId', CertId), ('MobiNo', MobiNo), ('Email', Email)])
  base_body = dict_to_xml_str('Pub', Pub) + dict_to_xml_str('Serial', Serial) + dict_to_xml_str('MoneyKind', MoneyKind)
  acc_body =  dict_to_xml_str('BankAcc', BankAcc) + dict_to_xml_str('FundAcc', FundAcc) +  dict_to_xml_str('Transfer', Transfer) + dict_to_xml_str('Client', Client) + dict_to_xml_str('FlagInfo', FlagInfo)
  summary_body = dict_to_xml_str('SummaryInfo', SummaryInfo)
  #组装成xml
  if (TradeCode == '11001'):
    xml_body = base_body + summary_body
  elif (TradeCode == '11005'):
    xml_body = base_body + acc_body + summary_body
  elif (TradeCode == '11006'):
    pass
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
  return message
