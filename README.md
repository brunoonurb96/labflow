# 🧪 LabFlow

**Sistema de gerenciamento de pacientes, exames e amostras laboratoriais.**

O LabFlow é um projeto desenvolvido em Python com o objetivo de aplicar conceitos de desenvolvimento de software na construção de um sistema voltado ao gerenciamento de informações laboratoriais.

O projeto utiliza SQLite para persistência de dados e uma arquitetura organizada em camadas, buscando manter o código estruturado, reutilizável e de fácil manutenção.

## 🚀 Tecnologias utilizadas

- **Python** – Linguagem principal do projeto.
- **SQLite** – Banco de dados relacional.
- **SQL** – Consultas, relacionamentos e manipulação de dados.
- **Git e GitHub** – Controle de versão.

## 📌 Funcionalidades

O sistema possui uma estrutura voltada ao gerenciamento de três entidades principais:

- **Pacientes:** armazenamento de informações pessoais, como CPF, nome, data de nascimento, endereço e telefone.
- **Exames:** gerenciamento dos exames disponíveis.
- **Amostras:** associação entre pacientes e exames, permitindo acompanhar informações como data de coleta e status.

### Consultas ao banco de dados

- Consulta de amostras vinculadas a um paciente por meio do CPF.
- Utilização de `INNER JOIN` para relacionar informações de diferentes tabelas.
- Suporte a múltiplas amostras associadas ao mesmo paciente.

## 🏗️ Arquitetura do projeto

O LabFlow utiliza uma organização baseada em camadas, separando as responsabilidades de cada parte da aplicação:

| Camada | Responsabilidade |
| --- | --- |
| Models | Representação das entidades do sistema. |
| Repositories | Comunicação com o banco de dados e execução de consultas SQL. |
| Services | Aplicação das regras de negócio e validações. |

Essa organização facilita a manutenção, a reutilização de código e a evolução do sistema.

## 🗄️ Banco de dados

O projeto utiliza SQLite, com as seguintes entidades principais:

- `patient`
- `exams`
- `sample`

As tabelas possuem relacionamentos por meio de chaves primárias e estrangeiras, permitindo integrar as informações de pacientes, exames e amostras.

## 🎯 Objetivo do projeto

O LabFlow faz parte da minha jornada de aprendizado em desenvolvimento de software, sendo uma oportunidade de aprofundar conhecimentos em Python, banco de dados, programação orientada a objetos, arquitetura de software e organização de código.

O projeto continua em desenvolvimento e novas funcionalidades serão implementadas ao longo da evolução da aplicação.

---

**Desenvolvido por Bruno** 💻

Tecnologias: Python | SQLite | SQL
