class DBRouter:
    def db_for_read(self, model,
    **hints):
        if model._meta.app_label == 'ref':
            return 'default'
        return None
    def db_for_write(self, model,
    **hints):
        if model._meta.app_label == 'ref':
            return 'default'
        return None
    def allow_relation(self, obj1, obj2,
    **hints):
        if obj1._meta.app_label == 'ref' or \
            obj2._meta.app_label == 'ref':
            return True
        return None
    def allow_migrate(self, db, app_label, model_name=None,
    **hints):
        if app_label == 'ref':
            return db == 'default'
        return None
