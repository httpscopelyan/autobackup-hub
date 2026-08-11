# backup-sentinel

Sistema desktop de backup automático desenvolvido em Python, construído sobre **Arquitetura Hexagonal (Ports & Adapters)** para permitir múltiplos provedores de armazenamento intercambiáveis sem acoplamento com a lógica de negócio. O sistema monitora pastas configuradas em tempo real, categoriza arquivos por extensão, compacta antes do envio e notifica o usuário por email a cada lote processado — com controle de limite de armazenamento e rate limiting nas integrações externas.

> 🚧 Projeto em desenvolvimento — construído como estudo prático de Python, arquitetura de software e integração com APIs externas.

---

## 🔄 Fluxo de Usuário

> _placeholder — diagrama/imagem do fluxo de usuário será inserido aqui_

---

## 📌 Sobre o Projeto

O **backup-sentinel** resolve um problema comum: manter cópias de segurança de pastas importantes de forma automática, organizada por tipo de arquivo, e com flexibilidade para escolher onde esses arquivos são armazenados — seja em provedores de nuvem (AWS S3, Google Drive) ou em um servidor local acessível via internet.

A escolha pela Arquitetura Hexagonal foi intencional: o núcleo de regras de negócio (categorização, controle de limite, orquestração de backup) não conhece detalhes de infraestrutura. Cada provedor de armazenamento é um *adapter* que implementa uma *port* comum, permitindo adicionar novos destinos de backup sem alterar a lógica central do sistema.

---

## 🏗️ Arquitetura

```
src/
├── domain/           → entidades puras (File, Category, BackupJob)
├── application/
│   ├── use_cases/    → regras de negócio (BackupFile, CategorizeFile, CheckStorageLimit...)
│   └── ports/        → contratos abstratos (StorageProvider, Notifier, ConfigRepository...)
└── adapters/
    ├── storage/       → S3Provider, GoogleDriveProvider, LocalServerProvider
    ├── notification/  → SmtpNotifier
    ├── persistence/   → SqliteRepository
    └── gui/           → interface com abas (CustomTkinter)
```

`domain/` e `application/` nunca dependem de `adapters/` — a dependência sempre aponta para dentro, seguindo o princípio de inversão de dependência.

---

## ✅ Requisitos Funcionais

### Interface

- O sistema terá uma interface de ativação e configuração.
- O sistema deverá ter abas de páginas.

### Configuração de Armazenamento (Cloud & Local)

- A aba de configuração permite selecionar pastas importantes individualmente e selecionar todas as pastas de uma vez.
- A aba de configuração possui um input de vínculo com o Google Drive via conta do usuário.
- O sistema deve permitir, na aba de configuração, conectar com outros serviços de cloud além do Google Drive.
- O sistema deve possuir uma aba que permita configurar um servidor local via internet como alternativa à nuvem.
- De acordo com a categoria de extensão, o sistema deve permitir configurar o nome da pasta que ficará no armazenamento (cloud ou local) ao ser enviada.

### Categorização de Arquivos

- O sistema deve permitir configurar categorias por tipo de arquivo (ex: `.mp4`/`.mp3` → categoria "Mídia"), configurável por extensão.
- O sistema deve permitir mais de uma extensão por categoria.
- De acordo com a categoria, o sistema deve permitir criar pastas personalizadas para envio aos serviços de armazenamento.
- Se a configuração de pasta personalizada estiver ativa, o usuário poderá definir quais categorias entram naquela pasta ao serem enviadas.

### Dashboard (Página Inicial)

- Após ativo, o sistema deve mostrar na página inicial a quantidade de arquivos transferidos por ele.
- Após ativo, o sistema deve mostrar na página inicial a quantidade de armazenamento usada pelos arquivos transferidos.
- O sistema deve fornecer um limite de armazenamento configurável para os arquivos transferidos.

### Notificações

- A cada 5 arquivos enviados, o sistema deve enviar um email de confirmação contendo: nome dos arquivos, data de envio e quantidade de armazenamento usado por esses arquivos.
- A aba de configuração deve conter um input de email.

### Compactação

- O sistema deve compactar os arquivos enviados para a nuvem antes de serem transferidos.

---

## 🔒 Requisitos Não Funcionais

- O sistema deve ser totalmente personalizável.
- O sistema deve ser totalmente desativável — ao fechar o app, todos os processos e fluxos em andamento devem ser encerrados.
- O sistema deve garantir que o limite de armazenamento configurado nunca seja excedido.
- Ao escrever o email uma vez e confirmar, o campo deve ser ocultado.
- Deve existir um botão para exibir novamente o email ocultado.
- Deve haver rate-limits para requisições às APIs de armazenamento em nuvem e ao servidor local.

---

## 🛠️ Tecnologias

| Camada | Biblioteca |
|---|---|
| Ambiente | `venv` |
| Interface (GUI) | `customtkinter` |
| Persistência | `sqlite3` |
| Observação de pastas | `watchdog` |
| Compactação | `zipfile` |
| Cloud — AWS S3 | `boto3` |
| Cloud — Google Drive | `google-api-python-client`, `google-auth-oauthlib` |
| Servidor local | `requests` |
| Notificações por email | `smtplib` |
| Segurança de credenciais | `keyring` |
| Rate limiting | implementação própria (token bucket) |
| Concorrência | `threading`, `queue.Queue` |
| Empacotamento | `pyinstaller` |

---

## ▶️ Como Executar

```bash
git clone https://github.com/ScopelYann/backup-sentinel.git
cd backup-sentinel
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

---

## 📄 Licença

Em definição.
