from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine as ce

Base = automap_base()
engine = ce('mysql+pymysql://root:root@localhost:3306/sexshop')
Base.prepare(engine, reflect=True)
session = Session(engine)

Product = Base.classes.oc_product