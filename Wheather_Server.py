# server.py
from concurrent import futures
import grpc
import time
import argparse
import weather_pb2
import weather_pb2_grpc

class WeatherServiceServicer(weather_pb2_grpc.WeatherServiceServicer):
    def __init__(self, temperature):
        self.temperature = temperature

    def GetTemperature(self, request, context):
        city = request.city
        print(f"[{time.strftime('%H:%M:%S')}] Received request for city='{city}' -> returning {self.temperature}°C")
        return weather_pb2.TemperatureResponse(city=city, temperature=self.temperature)

def serve(port, temperature):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    weather_pb2_grpc.add_WeatherServiceServicer_to_server(
        WeatherServiceServicer(temperature), server)
    server.add_insecure_port(f"[::]:{port}")
    server.start()
    print(f"Server started on port {port} with temperature={temperature}°C")
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, default=50051)
    parser.add_argument("--temperature", type=float, default=25.0)
    args = parser.parse_args()
    serve(args.port, args.temperature)
