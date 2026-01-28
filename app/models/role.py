class Role(Base):
    __tablename__ = "roles"

    id = Column(UUID, primary_key=True)
    name = Column(String, unique=True)
