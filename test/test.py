import datetime
import random

from influxdb import InfluxDBClient

client = InfluxDBClient(host='localhost', port=8086, username='ehsan', password='influxdb4ever',database='pyexample')
# client.create_database('pyexample')
print(client.get_list_database())
# client.switch_database('pyexample')


base = datetime.datetime.today()
date_list = [base - datetime.timedelta(hours=x) for x in range(0, 20)]
# for i in date_list:
#     value=random.uniform(.002,3.0)
#     json_body = [
#         {
#             "measurement": "cpu_load_short",
#             "tags": {
#                 "host": "server01",
#                 "region": "us-west"
#             },
#             "time": i.isoformat(),
#             "fields": {
#                 "value": value
#             }
#         }
#     ]
#     client.write_points(json_body)
result = client.query('select value from cpu_load_short;')
print("Result: {0}".format(result))



# json_body = [
#     {
#         "measurement": "brushEvents",
#         "tags": {
#             "user": "Carol",
#             "brushId": "6c89f539-71c6-490d-a28d-6c5d84c0ee2f"
#         },
#         "time": "2018-03-28T8:01:00Z",
#         "fields": {
#             "duration": 127
#         }
#     },
#     {
#         "measurement": "brushEvents",
#         "tags": {
#             "user": "Carol",
#             "brushId": "6c89f539-71c6-490d-a28d-6c5d84c0ee2f"
#         },
#         "time": "2018-03-29T8:04:00Z",
#         "fields": {
#             "duration": 132
#         }
#     },
#     {
#         "measurement": "brushEvents",
#         "tags": {
#             "user": "Carol",
#             "brushId": "6c89f539-71c6-490d-a28d-6c5d84c0ee2f"
#         },
#         "time": "2018-03-30T8:02:00Z",
#         "fields": {
#             "duration": 129
#         }
#     }
# ]
# print(client.write_points(json_body))
#
# results=client.query('SELECT "duration" FROM "pyexample"."autogen"."brushEvents" WHERE time > now() - 4d GROUP BY "user"')
# print(results.raw)
# # print(results.get_points(tags={'user': 'Carol'}))
# points = results.get_points(tags={'user': 'Carol'})
# for point in points:
#     print("Time: %s, Duration: %i" % (point['time'], point['duration']))

# results.raw
