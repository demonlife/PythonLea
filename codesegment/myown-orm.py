#!/usr/bin/env python
#encoding: utf8

class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)

class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')

class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')

class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        print 'attrs = %s' % attrs
        if name == 'Model':
            print 'Model meta'
            return type.__new__(cls, name, bases, attrs)

        mapping = dict()
        for k, v in attrs.iteritems():
            if isinstance(v, Field):
                print 'Found Mapping: %s ==> %s' % (k, v)
                mapping[k] = v
        for k in mapping.iterkeys():
            print 'pop k = ', k
            attrs.pop(k)

        attrs['__table__'] = name
        attrs['__mappings__'] = mapping
        return type.__new__(cls, name, bases, attrs)

class Model(dict):
    __metaclass__ = ModelMetaclass

    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []

        for k, v in self.__mappings__.iteritems():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))

        sql = 'insert into %s (%s) values (%s)' % (self.__table__, \
                                                   '.'.join(fields), \
                                                   ','.join(params))
        print 'SQL: %s' % sql
        print 'ARGS: %s' % str(args)

# test 
class User(Model):
    uid = IntegerField('id')
    name = StringField('username')
    email = StringField('email')

u = User(uid=12345, name='demon', email='demonlife2013@gmail.com')
u.save()
