import aiohttp
from loguru import logger

from models import InstanceInfo
from ..exceptions import (
    SmaltError,
    InternalServerError,
    NotFoundError,
    InvalidURLError
)
from ..constants import (
    NOT_FOUND, 
    INTERNAL_SERVER_ERROR
)

class Client:
    """Client for interacting with the cobalt API."""
    def __init__(self, base_url: str) -> None:
        """Initialize the wrapper with the API url.

        Parameters
        ----------
        base_url : str
            The API url of the cobalt instance.
        """
        self.base_url = base_url
        self.session = aiohttp.ClientSession()
        
    def validate_base_url(self, base_url: str) -> None:
        """Ensure that the base url is valid."""
        if not base_url.endswith('/'):
            raise InvalidURLError("Base URL must end with a '/'")

    async def close(self) -> None:
        """Close the HTTP session."""
        await self.session.close()

    async def get_instance_info(self) -> InstanceInfo:
        """Get information about the cobalt instance."""
        try:
            async with self.session.get(f"{self.base_url}") as r:
                r.raise_for_status()
                data = await r.json()

                return InstanceInfo(**data)
        except aiohttp.ClientResponseError as e:
            if e.status == NOT_FOUND:
                raise NotFoundError("Instance not found") from e
            elif e.status == INTERNAL_SERVER_ERROR:
                raise InternalServerError("Internal server error") from e
            else:
                logger.error(f"Unexpected error while getting instance info: {e}")
                raise SmaltError("Unexpected error occurred") from e