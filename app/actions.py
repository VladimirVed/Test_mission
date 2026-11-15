from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType

from objectpack.actions import ObjectPack
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

    add_window = ModelEditWindow.fabricate(model=ContentType)

class UserAddWindow(BaseEditWindow):
 
   def _init_components(self):

       super(UserAddWindow, self)._init_components()

       self.field__username = ext.ExtStringField(
           label=u'Login',
           name='username',
           allow_blank=False,
           anchor='100%')

       self.field__first_name = ext.ExtStringField(
           label=u'First_Name',
           name='first_name',
           allow_blank=False,
           anchor='100%')

       self.field__last_name = ext.ExtStringField(
           label=u'Last_Name',
           name='last_name',
           allow_blank=False,
           anchor='100%')

       self.field__password = ext.ExtStringField(
           label=u'password',
           name='password',
           allow_blank=False,
           anchor='100%')

       self.field__is_staff = ext.ExtCheckBox(
           label=u'Staff_Personal',
           name='is_staff',
           anchor='100%')

       self.field__is_active = ext.ExtCheckBox(
           label=u'Active',
           name='is_active',
           anchor='100%')

   def _do_layout(self):
       super(UserAddWindow, self)._do_layout()
       self.form.items.extend((
           self.field__username,
           self.field__first_name,
           self.field__last_name,
           self.field__password,
           self.field__is_staff,
           self.field__is_active,
       ))
   def set_params(self, params):
       super(UserAddWindow, self).set_params(params)
       self.height = 'auto'

      
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
  
    add_window = edit_window = UserAddWindow

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


class PermissionAddWindow(BaseEditWindow):
 
   def _init_components(self):

       super(PermissionAddWindow, self)._init_components()

       self.field__name = ext.ExtStringField(
           label=u'name',
           name='name',
           allow_blank=False,
           anchor='100%')

       self.field__codename = ext.ExtStringField(
           label=u'Codename',
           name='codename',
           allow_blank=False,
           anchor='100%')

       self.field__content_type = ext.ExtDictSelectField(
           label=u'content type',
           name='content_type_id',
           allow_blank=False,
           anchor='100%',
           display_field=ContentTypePack.column_name_on_select)

       self.field__content_type.pack = ContentTypePack 
  
   def _do_layout(self):

       super(PermissionAddWindow, self)._do_layout()
       self.form.items.extend((
           self.field__name,
           self.field__codename,
           self.field__content_type,
       ))

   def set_params(self, params):
           
       super(PermissionAddWindow, self).set_params(params)
       self.height = 'auto' 

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
    
    add_window = edit_window = PermissionAddWindow

    can_delete =True
# actions.py
 
