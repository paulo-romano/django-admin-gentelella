from django.contrib import admin
from gentelella.core.models import Pessoa

class PessoaAdminModel(admin.ModelAdmin):
    pass

admin.site.register(Pessoa, PessoaAdminModel)
