from marshmallow import Schema, fields, EXCLUDE, pre_load, post_load


class IsbnMeta(Schema):

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


class CrossRefAuthor(Schema):

    orcid = fields.URL(missing=None)
    given = fields.Str(missing=None)
    family = fields.Str(missing=None)

    class Meta:
        unknown = EXCLUDE


class CrossRefMeta(Schema):

    publisher = fields.Str(missing=None)
    issue = fields.Int(missing=None)
    doi = fields.Str(missing=None)
    pages = fields.Str(missing=None)
    volume = fields.Str(missing=None)
    type = fields.Str(missing=None)
    title = fields.Str(missing=None)
    author = fields.List(fields.Nested(CrossRefAuthor))
    url = fields.URL(missing=None)

    @pre_load
    def _clean_keys(self, obj, **kwargs):
        result = {}
        for key, val in obj.items():
            key = key.replace('-', '_')
            if key == 'title' and isinstance(val, list):
                val = val[0]
            result[key] = val
        return result

    class Meta:
        unknown = EXCLUDE
