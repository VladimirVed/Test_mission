from objectpack.ui import BaseEditWindow, make_combo_box, ModelEditWindow
from m3_ext.ui import all_components as ext
from django.contrib.contenttypes.models import ContentType


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

       self.field__content_type = make_combo_box(
           label=u'Content type',
           name='content_type',
           allow_blank=False,
           anchor='100%',
           data=[(ct.id, f" {ct.model}") for ct in ContentType.objects.all()]
        )

  
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
