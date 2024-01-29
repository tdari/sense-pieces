from pydantic import BaseModel, Field


class InputModel(BaseModel):
    """
    Reload Piece Input Model
    """
    app_id: str = Field(
        description="App ID to be reloaded",
    )


class OutputModel(BaseModel):
    """
    Reload Piece Output Model
    """
    message: str = Field(
        description="Reload piece executed"
    )


class SecretsModel(BaseModel):
    """
    Get Secrets
    """
    BEARER_TOKEN: str = Field(
        description = "Bearer token"
    )
    TENANT_URL: str = Field(
        description = "Qlik Cloud tenant url"
    )
