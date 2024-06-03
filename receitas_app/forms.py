from django.forms import ModelForm
from receitas_app.models import Receitas

# Create the form class.
class ReceitasForm(ModelForm):
	class Meta:
		model = Receitas
		fields = ["nome_receita", "ingredientes_receita", "descricao_receita"]
