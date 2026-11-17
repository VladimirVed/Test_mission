from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from .controller import observer
from m3 import ApplicationLogicException
from objectpack.actions import ObjectPack
from . import ui
from objectpack.ui import BaseEditWindow, make_combo_box, ModelEditWindow
from m3_ext.ui import all_components as ext

class ContentTypePack(ObjectPack):
    model = ContentType
    
    columns = [
        {
            'data_index': 'app_label',
            'header': u'Application',
        },
        {
            'data_index': 'model',
            'header': u'Model',
            'searchable':True,
        }
    ]
    
    add_to_menu = True

    add_window = edit_window = ModelEditWindow.fabricate(model=ContentType)

    column_name_on_select = 'model'
      
class UserPack(ObjectPack):
    
    model = User
    
    columns = [
        {
            'data_index': 'username',
            'header': u'Login',
            'searchable':True,
        },
        {
            'data_index': 'first_name',
            'header': u'First_Name',
            'searchable':True,
        },
        {
            'data_index': 'last_name',
            'header': u'Last_Name',
            'searchable':True,
        },
        {
            'data_index': 'password',
            'header': u'Password',
        },
        {
            'data_index': 'is_staff',
            'header': u'Staff_Personal',
        },
        {
            'data_index': 'is_active',
            'header': u'Active',
        }
    ]

    add_to_menu = True

    def save_row(self, obj, create_new, request, context):
        if not (obj.password.isalnum()):
           raise ApplicationLogicException(
              u'The password must consist only of numbers and letters!')
        super(UserPack, self).save_row(obj, create_new, request, context)
  
    add_window = edit_window = ui.UserAddWindow

    can_delete = True

class GroupPack(ObjectPack):
    model = Group
    
    columns = [
        
        {'data_index': 'name',
         'header': 'Name',
        }
    ]

    add_to_menu=True

    add_window  = ModelEditWindow.fabricate(model=Group)


class PermissionPack(ObjectPack):
    
    model = Permission

    columns = [
        
        {
            'data_index': 'name',
             'header': 'Name',
        },
        {
            'data_index': 'codename',
             'header': 'Codename',
        },
        {
            'data_index': 'content_type',
            'header': 'Content_Type',
        }
    ]
  
    add_to_menu = True
    
    add_window = edit_window =  ModelEditWindow.fabricate(Permission, model_register = observer)

    can_delete =True
# actions.py
 
