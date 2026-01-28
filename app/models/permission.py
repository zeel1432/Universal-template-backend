class Permission(Base):
    __tablename__ = "permissions"

    id = Column(UUID, primary_key=True)
    key = Column(String, unique=True)


role_permissions = Table(
    "role_permissions",
    Base.metadata,
    Column("role_id", ForeignKey("roles.id")),
    Column("permission_id", ForeignKey("permissions.id")),
)
