from marshmallow import Schema, fields, validate


class TaskSchema(Schema):
    id = fields.Integer(dump_only=True)
    title = fields.String(required=True, validate=validate.Length(min=1, max=100))
    decription = fields.String()
    date_created = fields.DateTime()
    user_id = fields.Integer(dump_only=True)