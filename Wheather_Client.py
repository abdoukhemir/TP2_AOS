import grpc
import weather_pb2
import weather_pb2_grpc
import itertools
import time

def make_stub(address):
    channel = grpc.insecure_channel(address)
    stub = weather_pb2_grpc.WeatherServiceStub(channel)
    return stub, channel

def main():
    servers = ["localhost:50051", "localhost:50052"]
    server_cycle = itertools.cycle(servers)

    num_requests = 8
    city = "Tunis"

    for i in range(1, num_requests + 1):
        addr = next(server_cycle)
        stub, channel = make_stub(addr)
        try:
            response = stub.GetTemperature(weather_pb2.CityRequest(city=city), timeout=5)
            print(f"Request {i} → {addr} → {response.city} {response.temperature}°C")
        except grpc.RpcError as e:
            print(f"Request {i} → {addr} FAILED: {e}")
        finally:
            channel.close()
        time.sleep(0.5)

if __name__ == "__main__":
    main()
