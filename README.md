# Sistema Escalável com Docker: Elasticidade Horizontal
Este repositório contém a implementação de um sistema escalável baseado em containers Docker. O projeto utiliza Flask para o backend, Nginx para balanceamento de carga e Locust para geração de carga sintética. Embora o escalonamento automático não esteja configurado, o sistema emprega um escalonamento estático, com réplicas pré-definidas no arquivo docker-compose.yml.

## 📋 Objetivo
O objetivo deste projeto é demonstrar a configuração de um ambiente escalável com containers Docker, explorando conceitos como:  

- **Elasticidade horizontal** através de réplicas estáticas.  
- **Balanceamento de carga automático** com Nginx.  
- **Geração de carga sintética** para testes de desempenho.

## ⚙️ Componentes do Sistema

1. **Configuração dos Containers**  
   Foram configurados três containers Flask, cada um respondendo a requisições simples e operando de forma independente.

2. **Rede Compartilhada**  
   Todos os containers estão conectados a uma mesma rede Docker para permitir comunicação interna e facilitar o balanceamento de carga.

3. **Coleta de Informações**  
   O uso de recursos, como CPU, memória e taxa de requisições, pode ser monitorado utilizando ferramentas como `docker stats`.

4. **Geração de Carga Sintética**  
   Para testar o sistema, foi configurada uma ferramenta de geração de carga sintética com o **Locust**, que simula cenários de alta e baixa demanda.

5. **Repasse Manual de Requisições**  
   Implementado por meio de um script Flask que redireciona as requisições para os containers utilizando um método de **round-robin manual**.

6. **Balanceamento de Carga**  
   Configurado utilizando o **Nginx** como proxy reverso, distribuindo automaticamente as requisições entre os containers.

7. **Escalonamento Estático**  
   Definido no arquivo `docker-compose.yml` com o uso de **réplicas estáticas** para manter o sistema escalado independentemente da carga.

---

## 🚀 Como Executar o Projeto

### 1. Pré-requisitos

- Docker e Docker Compose instalados na máquina.

### 2. Clonar o Repositório

```bash
git clone <URL_DO_REPOSITORIO>
cd sistema_escalavel_flask


