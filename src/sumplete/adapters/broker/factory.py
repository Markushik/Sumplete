from dishka import provide, Provider, Scope
from faststream.nats import NatsBroker

from src.sumplete.common.builder.url import build_nats_url
from src.sumplete.common.config.schemas import NatsConfig


class BrokerProvider(Provider):
    @provide(scope=Scope.APP)
    async def create_broker(self, config: NatsConfig) -> ...: ...
