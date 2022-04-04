from typing import List
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import ARRAY
import pydantic
from pydantic import constr

### sa (SQLAlchemy)
Base = sa.ext.declarative.declarative_base()
class CompanyOrm(Base):
    __tablename__ = 'companies'
    id         = sa.Column(sa.Integer, primary_key=True, nullable=False)
    public_key = sa.Column(sa.String(20), index=True, nullable=False, unique=True)
    name       = sa.Column(sa.String(63), unique=True)
    domains    = sa.Column(ARRAY(sa.String(255)))

co_orm = CompanyOrm(
    id=123,
    public_key='foobar',
    name='Testing',
    domains=['example.com', 'foobar.com'],
)

### pydantic
class CompanyModel(pydantic.BaseModel):
    id: int
    public_key: constr(max_length=20)
    name: constr(max_length=63)
    domains: List[constr(max_length=255)]
    class Config:
        orm_mode = True

co_model = CompanyModel.from_orm(co_orm)


print(co_orm)
#> <models_orm_mode.CompanyOrm object at 0x7f0bdac44850>
print(co_model)
#> id=123 public_key='foobar' name='Testing' domains=['example.com',
#> 'foobar.com']