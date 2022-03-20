from hyper.ma import ma
from models.entities import People
from marshmallow.validate import Validator
from marshmallow import validates_schema,ValidationError
from marshmallow import fields,validate

class PeopleSchema(ma.SQLAlchemyAutoSchema):
    pid = fields.Int(required=True)
    name = fields.Str(required=True, validate=[validate.Length(min=5, max=25)])
    ptype = fields.Str(required=True, validate=[validate.Length(min=4, max=8)])
    desc = fields.Str(required=True, validate=[validate.Length(min=5, max=500)])
    age = fields.Int(required=True,validate=[validate.Range(min=15,max=75)])
    desc= fields.Str(required=True)
    check=fields.Bool(required=True)
    class Meta:
        model = People
        include_relationships = True
        load_instance = True

'''
        @validates_schema
        def validate_age(self, data, **kwargs):
            print(data['ptype'])
            if data['ptype'].lower() == 'male':
                if data['age'] < 21:
                    raise ValidationError("Minimum age for males is 21.")

            if data['ptype'].lower() == 'female':
                if data['age'] < 18:
                    raise ValidationError("Minimum age for females is 18.")
'''