import grpc
import warnings

import weather_pb2 as weather__pb2

GRPC_GENERATED_VERSION = '1.76.0'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + ' but the generated code in weather_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class WeatherServiceStub(object):
   

    def __init__(self, channel):
      
        self.GetTemperature = channel.unary_unary(
                '/weather.WeatherService/GetTemperature',
                request_serializer=weather__pb2.CityRequest.SerializeToString,
                response_deserializer=weather__pb2.TemperatureResponse.FromString,
                _registered_method=True)


class WeatherServiceServicer(object):
   
    def GetTemperature(self, request, context):
       
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_WeatherServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetTemperature': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTemperature,
                    request_deserializer=weather__pb2.CityRequest.FromString,
                    response_serializer=weather__pb2.TemperatureResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'weather.WeatherService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('weather.WeatherService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class WeatherService(object):
    

    @staticmethod
    def GetTemperature(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/weather.WeatherService/GetTemperature',
            weather__pb2.CityRequest.SerializeToString,
            weather__pb2.TemperatureResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
