from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, Http404, get_object_or_404
from django.urls import reverse
from django.views import generic

from .models import Questao, Opcao

class IndexView(generic.ListView):
    template_name = 'votacoes/index.html'
    context_object_name = 'lista_ultimas_questoes'

    def get_queryset(self):
        return Questao.objects.order_by('-pub_date')[:5]

class DetalhesView(generic.DetailView):
    model = Questao
    template_name = 'votacoes/detalhes.html'

class ResultadosView(generic.DetailView):
    model = Questao
    template_name = 'votacoes/resultados.html'

# def index (request):
 #   list_ultimas_questoes = Questao.objects.order_by('-pub_date')[:5]
  #  context = { 'lista_ultimas_questoes': lista_ultimas_questoes }
   # return render(request, 'votacoes/index.html', context)

#def detalhes (request, questao_id):
#    questao = get_object_or_404(Questao, pk=questao_id)
#    return render(request, 'votacoes/detalhes.html', {'questao': questao})

#def resultados(request, questao_id):
#    questao =  get_object_or_404(Questao, pk=questao_id)
#    return render(request, 'votacoes/resultados.html', {'questao': questao})

#def votar(request, questao_id):
#    questao = get_object_or_404(Questao, pk=questao_id)
#    try:
#        op_selecionada = questao.opcao_set.get(pk=request.POSt['opcao'])
#    except (KeyError, Opcao.DoesNotExist):
#        return render(request, 'votacoes/detalhes.html', {
#            'questao': questao,
#            'msg_erro': 'Você não selecionou uma opção.',
 #       })
  #  else:
   #     op_selecionada.votos += 1
    #    op_selecionada.save()
     #   return HttpResponseRedirect(reverse('votacoes:resultados',
    #                                args=(questao_id)))