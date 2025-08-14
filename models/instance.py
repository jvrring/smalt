from pydantic import BaseModel

class CobaltInfo(BaseModel):
    """Information about the cobalt instance."""
    version: str
    url: str
    start_time: str
    turnstile_site_key: str | None
    services: list[str]
    
class GitInfo(BaseModel):
    """Information about the git instance."""
    commit: str
    branch: str
    remote: str
    
class InstanceInfo(BaseModel):
    """Information about the instance."""
    cobalt_info: CobaltInfo
    git_info: GitInfo
