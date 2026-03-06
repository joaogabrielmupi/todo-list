# todo-list

Este repositório contém o projeto de Onboarding desenvolvido durante a minha primeira semana como estagiário. O objetivo principal foi a aplicação de padrões internos e o uso de ferramentas para o desenvolvimento de interfaces reativas.

## Ferramentas e Práticas Internas

### Tecnologias e Frameworks
* **HTMX**: Utilização de tags e atributos para atualizações parciais de página e comunicação assíncrona.
* **Alpine.js**: Framework para gerenciamento de estados e comportamentos interativos no lado do cliente.
* **Allauth**: Implementação de sistema de autenticação e gestão de usuários.

### Segurança e Arquitetura
* **Instalação Local**: Os frameworks Alpine e HTMX foram integrados diretamente ao projeto (sem uso de CDN) seguindo protocolos internos de segurança.
* **Uso de Partials**: Organização de templates através da fragmentação de código em arquivos menores (partials), visando facilitar a manutenção e o reaproveitamento.

### Funcionalidades Implementadas
* **Paginação**: Sistema de navegação para listagem de dados.
* **Modais**: Interface para criação e edição de itens sem recarregamento de página.
* **Integração Reativa**: Uso combinado de HTMX e Alpine para uma experiência de usuário fluida.

## Refatoração e Padronização de Views

O projeto passou por uma transição estrutural de **Function-Based Views (FBVs)** para **Class-Based Views (CBVs)**. O objetivo foi aplicar padrões de herança do Django para reduzir a duplicidade de código (DRY), realizando sobrescritas estratégicas para manter a compatibilidade com o comportamento assíncrono do **HTMX**.

### Sobrescrita de Métodos e Customizações
* **`get_template_names`**: Implementação de lógica dinâmica para alternar entre o template completo (`index.html`) e fragmentos (`partials/task_list.html`) baseada na detecção do cabeçalho `HX-Request`.
* **`form_valid`**: Customização do fluxo de sucesso para retornar respostas parciais (partials) e cabeçalhos de gatilho (`HX-Trigger`) em vez de redirecionamentos de página inteira.
* **`get_context_data`**: Gestão centralizada de variáveis de contexto, permitindo a passagem de títulos dinâmicos e metadados para os modais de interface.
* **`get_queryset`**: Reforço da camada de segurança e isolamento de dados, garantindo que a busca no banco de dados seja filtrada automaticamente pelo usuário autenticado (`request.user`).

### Abordagem Híbrida
Foi adotada uma estratégia pragmática: manteve-se o uso de **FBVs** para ações atômicas e rápidas (como o *toggle* de status de tarefas). Essa decisão evitou a complexidade desnecessária de sobrescrever classes genéricas em lógicas que não envolvem formulários ou listagens complexas, priorizando a legibilidade do código.
