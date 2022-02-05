from marshmallow import Schema, fields, EXCLUDE, pre_load


class IsbnSchema(Schema):

    isbn_13 = fields.Str(missing=None)
    isbn_10 = fields.Str(missing=None)
    title = fields.Str(missing=None)
    authors = fields.List(fields.Str(), missing=[], default=[])
    publisher = fields.Str(missing=None)
    year = fields.Int(missing=None)
    language = fields.Str(missing=None)

    class Meta:
        unknown = EXCLUDE

    @pre_load
    def _clean_keys(self, obj, **kwargs):

        result = {}
        for key, val in obj.items():
            key = key.replace('-', '_').lower()
            if key == 'authors' and val == ['']:
                val = []
            result[key] = val
        return result
