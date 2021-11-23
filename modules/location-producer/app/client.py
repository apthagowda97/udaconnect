import grpc
import location_pb2
import location_pb2_grpc

print("Sending location payload...")

channel = grpc.insecure_channel("localhost:5555")
stub = location_pb2_grpc.LocationServiceStub(channel)

# Update this with desired payload
location = location_pb2.LocationMessage(
    id=45,
    person_id=10,
    longitude="37.55363",
    latitude="-122.290883",
    creation_time="2020-07-07T10:37:06"
    
)


response = stub.Create(location)