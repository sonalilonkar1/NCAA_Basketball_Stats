from fastapi import APIRouter
from .service import Service

class BaseRouter:
    def __init__(self, service: Service, prefix: str, tags: list[str]) -> None:
        self.router = APIRouter(
            prefix=prefix,
            tags=tags
        )
        self.service = service
       
    def get_router(self) -> APIRouter:
        return self.router
    
    def include_routes(self) -> APIRouter:
        from src.apis import fetch_players, compare_players, historical_win_loss, team_performance, three_point_percent

        fetch_players.include_route(self)
        compare_players.include_route(self)
        historical_win_loss.include_route(self)
        team_performance.include_route(self)
        three_point_percent.include_route(self)

        return self.router
