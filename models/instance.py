from pydantic import BaseModel, Field

class CobaltInfo(BaseModel):
    """Information about the cobalt instance."""
    version: str
    url: str
    start_time: str = Field(alias="startTime")
    duration_limit: int | None = Field(alias="durationLimit")
    turnstile_site_key: str | None = Field(default=None, alias="turnstileSitekey")
    services: list[str]
    
class GitInfo(BaseModel):
    """Information about the git instance."""
    commit: str
    branch: str
    remote: str
    
class InstanceInfo(BaseModel):
    """Information about the instance."""
    cobalt_info: CobaltInfo = Field(alias="cobalt")
    git_info: GitInfo = Field(alias="git")
