-- Criação do banco de dados apenas se não existir
CREATE DATABASE IF NOT EXISTS sistema_tarefas;
USE sistema_tarefas;

-- Tabela de Usuários
CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    senha VARCHAR(255) NOT NULL
);

-- Tabela de Status das Tarefas (Ex: "Concluída", "Em andamento", "Pendente")
CREATE TABLE IF NOT EXISTS status_tarefa (
    id_status INT AUTO_INCREMENT PRIMARY KEY,
    descricao VARCHAR(50) NOT NULL
);

-- Tabela de Prioridades das Tarefas (Ex: "Baixa", "Média", "Alta")
CREATE TABLE IF NOT EXISTS prioridade_tarefa (
    id_prioridade INT AUTO_INCREMENT PRIMARY KEY,
    descricao VARCHAR(50) NOT NULL
);

-- Tabela de Categorias das Tarefas (Ex: "Trabalho", "Estudo", "Pessoal")
CREATE TABLE IF NOT EXISTS categoria_tarefa (
    id_categoria INT AUTO_INCREMENT PRIMARY KEY,
    descricao VARCHAR(50) NOT NULL
);

-- Tabela de Tarefas
CREATE TABLE IF NOT EXISTS tarefas (
    id_tarefa INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    descricao TEXT NOT NULL,
    data_criacao DATE NOT NULL,
    data_limite DATE,
    id_status INT,
    id_prioridade INT,
    id_categoria INT,
    usuario_id INT, -- Coluna adicionada para relacionar com a tabela usuarios
    FOREIGN KEY (id_status) REFERENCES status_tarefa(id_status),
    FOREIGN KEY (id_prioridade) REFERENCES prioridade_tarefa(id_prioridade),
    FOREIGN KEY (id_categoria) REFERENCES categoria_tarefa(id_categoria),
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id) -- Referência ao usuário que criou a tarefa
);

-- Inserção de valores iniciais para status (ignorar se já existir)
INSERT IGNORE INTO status_tarefa (descricao) VALUES 
('Concluída'),
('Em andamento'),
('Pendente');

-- Inserção de valores iniciais para prioridades (ignorar se já existir)
INSERT IGNORE INTO prioridade_tarefa (descricao) VALUES 
('Baixa'),
('Média'),
('Alta');

-- Inserção de valores iniciais para categorias (ignorar se já existir)
INSERT IGNORE INTO categoria_tarefa (descricao) VALUES 
('Trabalho'),
('Estudo'),
('Pessoal');
