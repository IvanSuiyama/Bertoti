import telebot

BOT_TOKEN = "YOUR TOKEN"
bot = telebot.TeleBot(BOT_TOKEN)

user_stories = {
    "cliente": {
        "user_story": "Como um cliente, quero adicionar itens ao carrinho para fazer uma compra.",
        "tasks": [
            "Criar uma interface de adição de produtos ao carrinho.",
            "Implementar um botão 'Comprar agora'.",
            "Adicionar funcionalidade de remoção de itens do carrinho.",
            "Exibir o total de itens e o preço atualizado.",
            "Testar a integração com o sistema de pagamentos."
        ]
    },
    "adm": {
        "user_story": "Como um administrador, quero gerenciar os produtos para manter o catálogo atualizado.",
        "tasks": [
            "Criar uma interface para adicionar novos produtos.",
            "Implementar funcionalidade de edição de informações do produto.",
            "Habilitar exclusão de produtos obsoletos.",
            "Adicionar filtro por categoria no catálogo.",
            "Testar permissões de acesso para evitar erros."
        ]
    },
    "suporte": {
        "user_story": "Como um agente de suporte, quero responder às perguntas dos clientes para resolver problemas rapidamente.",
        "tasks": [
            "Criar uma interface para visualizar solicitações de suporte.",
            "Implementar funcionalidade de envio de respostas rápidas.",
            "Adicionar um sistema de classificação de prioridade para tickets.",
            "Exibir histórico de interações com o cliente.",
            "Testar integrações com chat em tempo real."
        ]
    },
    "gerente de projetos": {
        "user_story": "Como um gerente de projetos, quero acompanhar o progresso das tarefas para garantir que os prazos sejam cumpridos.",
        "tasks": [
            "Configurar um painel de controle com status de tarefas.",
            "Adicionar funcionalidade para atribuir tarefas a membros da equipe.",
            "Habilitar notificações para prazos críticos.",
            "Integrar com calendários para rastreamento de datas.",
            "Implementar relatórios de desempenho da equipe."
        ]
    },
    "desenvolvedor": {
        "user_story": "Como um desenvolvedor, quero acessar a documentação do projeto facilmente para agilizar meu trabalho.",
        "tasks": [
            "Criar uma página centralizada para a documentação.",
            "Implementar busca por palavras-chave na documentação.",
            "Adicionar exemplos de código em diferentes linguagens.",
            "Configurar um sistema de feedback para melhorias na documentação.",
            "Integrar a documentação com o repositório de código."
        ]
    },
    "designer": {
        "user_story": "Como um designer, quero criar protótipos visuais para testar ideias antes do desenvolvimento.",
        "tasks": [
            "Configurar uma ferramenta de arrastar e soltar para prototipagem.",
            "Adicionar bibliotecas de componentes reutilizáveis.",
            "Habilitar compartilhamento de protótipos com a equipe.",
            "Implementar comentários diretamente nos protótipos.",
            "Testar a compatibilidade com diferentes dispositivos."
        ]
    },
    "cliente corporativo": {
        "user_story": "Como um cliente corporativo, quero acessar relatórios detalhados de consumo para otimizar os custos.",
        "tasks": [
            "Criar um painel com gráficos de consumo.",
            "Adicionar opções de download em formatos como PDF e Excel.",
            "Habilitar personalização de filtros por período ou categoria.",
            "Configurar alertas automáticos para gastos excessivos.",
            "Testar integrações com sistemas ERP."
        ]
    },
    "treinador": {
        "user_story": "Como um treinador, quero acompanhar o progresso dos participantes para ajustar meu plano de treinamento.",
        "tasks": [
            "Criar uma funcionalidade para registrar progresso individual.",
            "Adicionar gráficos de desempenho por período.",
            "Habilitar envio de feedback personalizado.",
            "Configurar notificações para tarefas pendentes dos participantes.",
            "Implementar relatórios comparativos para turmas ou grupos."
        ]
    }
}


user_state = {}

@bot.message_handler(commands=['start'])
def send_welcome(message):
    chat_id = message.chat.id
    user_state[chat_id] = {"awaiting_persona": True}  
    bot.reply_to(
        message,
        "Bem-vindo ao ChatBot que vai te ajudar a criar tasks baseadas em user stories!\n"
        "Escolha uma das personas para começar:\n"
        "- Cliente\n"
        "- Adm\n"
        "- Desenvolvedor\n"
        "- Suporte\n"
        "- Gerente de projetos\n"
        "- Designer\n"
        "- Cliente corporativo\n"
        "- Treinador\n"
        "Digite o nome da persona:"
    )

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(
        message,
        "**O que é uma User Story?**\n"
        "Uma *user story* (história do usuário) descreve o que um usuário precisa ou deseja alcançar. Ela é escrita no formato:\n"
        "- *'Como um [tipo de usuário], quero [meta] para [razão].'*\n\n"
        "**O que são Tasks?**\n"
        "Tasks são ações específicas ou atividades necessárias para implementar uma *user story*. Elas ajudam a dividir o trabalho em etapas menores.\n\n"
        "**O que são Personas?**\n"
        "Personas representam diferentes tipos de usuários ou papéis envolvidos em um projeto. Elas ajudam a entender as necessidades específicas de cada grupo de usuários.\n\n"
        "Digite `/start` para escolher uma persona e começar!"
    )

@bot.message_handler(func=lambda message: user_state.get(message.chat.id, {}).get("awaiting_persona", False))
def handle_persona_choice(message):
    chat_id = message.chat.id
    choice = message.text.strip().lower()

    if choice in user_stories:
        story = user_stories[choice]
        tasks = "\n".join([f"{i+1}. {task}" for i, task in enumerate(story["tasks"])])
        bot.send_message(
            chat_id,
            f"User Story para '{choice.capitalize()}':\n"
            f"- {story['user_story']}\n\n"
            "Tarefas sugeridas:\n" + tasks
        )
        bot.send_message(chat_id, "Deseja escolher outra persona? (sim/não)")
        user_state[chat_id] = {"awaiting_continue": True}  
    else:
        bot.reply_to(message, "Opção inválida. Por favor, escolha uma das personas disponíveis.")

@bot.message_handler(func=lambda message: user_state.get(message.chat.id, {}).get("awaiting_continue", False))
def handle_continue_choice(message):
    chat_id = message.chat.id
    choice = message.text.strip().lower()

    if choice == "sim":
        user_state[chat_id] = {"awaiting_persona": True}  
        bot.send_message(
            chat_id,
            "Escolha uma das personas:\n"
            "- Cliente\n"
            "- Adm\n"
            "- Desenvolvedor\n"
            "- Suporte\n"
            "- Gerente de projetos\n"
            "- Designer\n"
            "- Cliente corporativo\n"
            "- Treinador\n"
            "Digite o nome da persona:"
        )
    elif choice == "não" or choice == "nao":
        bot.send_message(chat_id, "Obrigado por usar os nossos serviços. Até a próxima!")
        user_state.pop(chat_id, None)
    else:
        bot.reply_to(message, "Resposta inválida. Por favor, responda com 'sim' ou 'não'.")

bot.polling()
