

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

def exibir_opcoes_disponiveis(opcoes_disponiveis):
    print("Escolha qual dos perfis abaixo se encaixa melhor na sua user story:")
    for perfil in opcoes_disponiveis:
        print(f"- {perfil.capitalize()}")

def tratar_escolha_usuario():
    opcoes_disponiveis = list(user_stories.keys())

    while opcoes_disponiveis:
        exibir_opcoes_disponiveis(opcoes_disponiveis)
        escolha = input("Digite o nome do perfil: ").strip().lower()

        if escolha in opcoes_disponiveis:
            historia_selecionada = user_stories[escolha]
            print(f"\nUser Story para '{escolha.capitalize()}':")
            print(f"- {historia_selecionada['user_story']}\n")
            print("Tarefas sugeridas:")
            for i, tarefa in enumerate(historia_selecionada["tasks"], 1):
                print(f"{i}. {tarefa}")
            print("\n")
            opcoes_disponiveis.remove(escolha)
        else:
            print("Opção inválida. Por favor, escolha um dos perfis listados.\n")
            continue

        if opcoes_disponiveis:
            mais = input("Deseja ver outra user story? (sim/não): ").strip().lower()
            if mais != "sim":
                break
        else:
            print("\nVocê já visualizou todas as user stories disponíveis.")
            break

    print("\nObrigado por usar o nosso chat. Boa sorte com a criação das suas tasks!")

tratar_escolha_usuario()
