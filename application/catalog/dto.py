from pydantic import BaseModel

class CatalogDTO(BaseModel):
    identity: str
    description: str
    active: bool
    class Config:
        from_attributes = True

class CatalogDataDTO(BaseModel):
    identity: str
    catalog_identity: str
    name: str
    description: str | None = None
    order: int | None = None
    active: bool
    class Config:
        from_attributes = True