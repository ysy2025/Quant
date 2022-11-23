import kafka

import json, os, sys, time,datetime
import socket
import sys, base64, zlib
#import ErrorOperation
#from Crypto.Cipher import AES
from kafka import SimpleClient
from kafka.producer import KafkaProducer, KeyedProducer
from kafka.consumer import KafkaConsumer

sys.setdefaultencoding("utf-8")


"""

# Describe the sink
guangcai_gux.sinks.k1.type = org.apache.flume.sink.kafka.KafkaSink
guangcai_gux.sinks.k1.kafka.topic=zj_pc_log
guangcai_gux.sinks.k1.kafka.linger.ms = 1
guangcai_gux.sinks.k1.kafka.flumeBatchSize = 1000
guangcai_gux.sinks.k1.kafka.bootstrap.servers = 10.125.7.105:9092,10.125.7.118:9092,10.125.7.16:9092
guangcai_gux.sinks.k1.kafka.producer.acks=1
guangcai_gux.sinks.k1.kafka.producer.max.request.size=5242880
guangcai_gux.sinks.k1.custom.encoding=UTF-8


"""

consumer = KafkaConsumer(
'zj_pc_log',
group_id='tc-yangsy-text',
auto_offset_reset="latest",
# bootstrap_servers=['{kafka_host}:{kafka_port}'.format(kafka_host=kafka_host, kafka_port=kafka_port)]
bootstrap_servers=["10.125.7.105:9092","10.125.7.118:9092","10.125.7.16:9092"],
heartbeat_interval_ms=5000, max_partition_fetch_bytes=10485760)

"""

ConsumerRecord(topic=u'zj_pc_log', partition=2, offset=9220206411, timestamp=-1, timestamp_type=0, key=None, value='{"country":"\xe4\xb8\xad\xe5\x9b\xbd","province":"\xe5\xb9\xbf\xe4\xb8\x9c","city":"\xe5\xb9\xbf\xe5\xb7\x9e","timestamp":"2022-11-22 11:02:48.264","ssid":"{94180721-774E-4FE1-AD9E-EFB739687A93}","env":"prod","count":"1","name":"OPERATION","data":"{\\"city\\":\\"\\",\\"country\\":\\"\\",\\"debug\\":\\"false\\",\\"dognum\\":\\"A321069012\\",\\"duration\\":\\"\\",\\"fncode\\":\\"700373\\",\\"fngroup\\":\\"\xe6\x9e\x84\xe4\xbb\xb6\xe5\x88\x97\xe8\xa1\xa8\\",\\"fnname\\":\\"\xe6\x9e\x84\xe4\xbb\xb6\xe5\x88\x97\xe8\xa1\xa8|\xe5\xa4\x8d\xe5\x88\xb6\\",\\"gid\\":\\"\\",\\"licensetype\\":\\"0\\",\\"pcode\\":\\"13025\\",\\"prjname\\":\\"P1f0gSSax0rpWTmaDIQYvg==\\",\\"projectid\\":\\"{7f4114ae-43aa-452d-92d0-68a702222005}\\",\\"province\\":\\"\\",\\"query\\":{\\"Elementtype\\":\\"\xe7\xaa\x97\\"},\\"regionrule\\":\\"\xe5\xb9\xbf\xe8\x81\x94\xe8\xbe\xbe\xe5\xbb\xba\xe7\xad\x91\xe4\xb8\x8e\xe8\xa3\x85\xe9\xa5\xb0\xe5\xb7\xa5\xe7\xa8\x8b\xe9\x87\x8f\xe8\xae\xa1\xe9\x87\x8f\xe5\xae\x9a\xe9\xa2\x9d\xe8\xae\xa1\xe7\xae\x97\xe8\xa7\x84\xe5\x88\x99;\xe5\xb9\xbf\xe8\x81\x94\xe8\xbe\xbe\xe5\xbb\xba\xe7\xad\x91\xe4\xb8\x8e\xe8\xa3\x85\xe9\xa5\xb0\xe5\xb7\xa5\xe7\xa8\x8b\xe9\x87\x8f\xe8\xae\xa1\xe9\x87\x8f\xe6\xb8\x85\xe5\x8d\x95\xe8\xae\xa1\xe7\xae\x97\xe8\xa7\x84\xe5\x88\x99\\",\\"serialnum\\":\\"000000000011CB44\\",\\"uid\\":\\"{94180721-774E-4FE1-AD9E-EFB739687A93}\\",\\"usetype\\":\\"\xe6\xad\xa3\xe5\xbc\x8f\xe7\x89\x88\\",\\"ver\\":\\"1.0.32.1\\",\\"ver2\\":\\"1.0.32.1\\",\\"vername\\":\\"\xe5\xb9\xbf\xe8\x81\x94\xe8\xbe\xbeBIM\xe5\x9c\x9f\xe5\xbb\xba\xe8\xae\xa1\xe9\x87\x8f\xe5\xb9\xb3\xe5\x8f\xb0 GTJ2021\\"}","app_name":"GTJ2021","app_version":"1.0.32.1","msg_type":"5","device_id":"c728b9dd-1a0c-4519-af09-69dc81610df3","mt_devid":"{BC925DB6-FB26-0DF2-4207-837F00000000}","remote_ip":"121.8.215.90","sessionid":"1669075737466","logid":"e5c4b570284a4330985b99de1342146f","routing_key":"gux2.5.GTJ2021","data_version":"2.4","created_at":"2022-11-22 11:05:57.059","updated_at":"2022-11-22 11:12:54.386"}', checksum=1746313613, serialized_key_size=-1, serialized_value_size=1322)

"""
i = 0
for message in consumer:
    print(message)
    print(message.key, message.value)
    """
    (None, '{"country":"\xe4\xb8\xad\xe5\x9b\xbd","province":"\xe6\xb9\x96\xe5\x8c\x97","city":"\xe6\xad\xa6\xe6\xb1\x89","timestamp":"2022-11-22 11:10:35.618","ssid":"{53A1EF0E-FF32-4F74-A1A4-E724956AED0C}","env":"prod","count":"1","name":"\xe5\x88\xa0\xe9\x99\xa4-\xe7\xa1\xae\xe8\xae\xa4\xe5\x88\xa0\xe9\x99\xa4","data":"{\\"debug\\":\\"false\\",\\"dognum\\":\\"Y320953737\\",\\"duration\\":\\"\\",\\"fncode\\":\\"700011\\",\\"fngroup\\":\\"\xe9\x80\x9a\xe7\x94\xa8\xe7\xbc\x96\xe8\xbe\x91\\",\\"fnname\\":\\"\xe5\x88\xa0\xe9\x99\xa4-\xe7\xa1\xae\xe8\xae\xa4\xe5\x88\xa0\xe9\x99\xa4\\",\\"gid\\":\\"5985954625294451096\\",\\"licensetype\\":\\"0\\",\\"major\\":\\"\\",\\"pcode\\":\\"13025\\",\\"prjcost\\":\\"\\",\\"prjedocnt\\":\\"\\",\\"prjfullpath\\":\\"\\",\\"prjname\\":\\"\\",\\"prjsize\\":\\"\\",\\"projectid\\":\\"{5c5261db-1c72-43ba-a914-dc95168c82b5}\\",\\"query\\":{\\"\xe5\x8c\xba\xe5\x9f\x9f\\":\\"\xe9\x9f\xa9\xe5\xae\xb6\xe5\xa2\xa9\\",\\"\xe6\x9e\x84\xe4\xbb\xb6\xe7\xb1\xbb\xe5\x9e\x8b\\":\\"\xe7\x8e\xb0\xe6\xb5\x87\xe6\x9d\xbf\\",\\"\xe6\xa5\xbc\xe5\xb1\x82\\":\\"\xe7\xac\xac2\xe5\xb1\x82\\"},\\"regionrule\\":\\"\\",\\"serialnum\\":\\"00000000000FB597\\",\\"trigertime\\":\\"2022-11-22 11:10:35 613\\",\\"uid\\":\\"{53A1EF0E-FF32-4F74-A1A4-E724956AED0C}\\",\\"usetype\\":\\"\xe6\xad\xa3\xe5\xbc\x8f\xe7\x89\x88\\",\\"utype\\":\\"\\",\\"ver\\":\\"1.0.34.2\\",\\"ver2\\":\\"\\",\\"vername\\":\\"\xe5\xb9\xbf\xe8\x81\x94\xe8\xbe\xbeBIM\xe5\x9c\x9f\xe5\xbb\xba\xe8\xae\xa1\xe9\x87\x8f\xe5\xb9\xb3\xe5\x8f\xb0 GTJ2021\\"}","app_name":"GTJ2021","app_version":"1.0.34.2","msg_type":"5","device_id":"722f6932-5883-476b-a723-ddf547ba786b","mt_devid":"{C80462A6-55F9-F46A-7AAD-510000000000}","remote_ip":"171.113.180.139","sessionid":"1669082157259","logid":"5c3c4e9a043b40b8b40d3c42bf81d0dd","routing_key":"gux2.5.GTJ2021","data_version":"2.4","created_at":"2022-11-22 11:15:24.894","updated_at":"2022-11-22 11:15:26.047"}')
    """
    # print(type(message))
    if """\\"pcode\\":\\"13073\\""" in message.value:
        print(message.value)
        i+=1
        print(i)
        break
    if i > 3:
        break

