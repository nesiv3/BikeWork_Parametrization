
class CatalogData:
    def __init__(self, identity: str, catalog_identity: str, name: str, description: str = None, order: int = None, active: bool = True):
        self.identity = identity
        self.catalog_identity = catalog_identity
        self.name = name
        self.description = description
        self.order = order
        self.active = active