#!/usr/bin/python3
"""
Defines the base model for various classes
"""
import uuid
from datetime import datetime


class BaseModel:
    """
    Defines all common attributes and methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes instance
        """
        if kwargs:
            if '__class__' in kwargs:
                del kwargs['__class__']
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'])
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'])
            self.__dict__.update(kwargs)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            from . import inst_storage
            inst_storage.new(self)

    def __str__(self):
        """
        String representation when instance printed
        """
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Save updates to instance
        """
        self.__dict__.update({'updated_at': datetime.now()})
        from .  import inst_storage
        inst_storage.save()

    def to_dict(self):
        """
        Returns a dictionary representation of an instance
        """
        inst_data = dict(self.__dict__)
        inst_data.update({'__class__': type(self).__name__,
                        'updated_at': self.updated_at.isoformat(),
                        'id': self.id,
                        'created_at': self.created_at.isoformat()})
        return inst_data
