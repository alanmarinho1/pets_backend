from django.core.mail import send_mail

def enviar_email_confirmacao(adocao):
    assunto = "Adoção realizada com sucesso!"
    conteudo = f"Parabens por realizar a adoção do pet {adocao.pets.nome} com o valor mensal de {adocao.valor}"
    remetente = "alanmarinho.ti@gmail.com"
    destinatario = [adocao.email]
    send_mail(assunto, conteudo, remetente, destinatario)
