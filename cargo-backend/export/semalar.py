from db import Kargo, Kisi
from .ma import ma


# Kayıt Ekleme ve Listeleme


class KisiSema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Kisi


class KargoSema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Kargo
        include_fk = True
