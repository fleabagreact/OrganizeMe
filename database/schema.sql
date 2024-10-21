-- Criação do banco de dados
CREATE DATABASE sistema_tarefas;
USE sistema_tarefas;

-- Tabela de Status das Tarefas (Ex: "Concluída", "Em andamento", "Pendente")
CREATE TABLE status_tarefa (
    id_status INT AUTO_INCREMENT PRIMARY KEY,
    descricao VARCHAR(50) NOT NULL
);

-- Tabela de Prioridades das Tarefas (Ex: "Baixa", "Média", "Alta")
CREATE TABLE prioridade_tarefa (
    id_prioridade INT AUTO_INCREMENT PRIMARY KEY,
    descricao VARCHAR(50) NOT NULL
);

-- Tabela de Categorias das Tarefas (Ex: "Trabalho", "Estudo", "Pessoal")
CREATE TABLE categoria_tarefa (
    id_categoria INT AUTO_INCREMENT PRIMARY KEY,
    descricao VARCHAR(50) NOT NULL
);

-- Tabela de Tarefas
CREATE TABLE tarefas (
    id_tarefa INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    descricao TEXT NOT NULL,
    data_criacao DATE NOT NULL,
    data_limite DATE,
    id_status INT,
    id_prioridade INT,
    id_categoria INT,
    FOREIGN KEY (id_status) REFERENCES status_tarefa(id_status),
    FOREIGN KEY (id_prioridade) REFERENCES prioridade_tarefa(id_prioridade),
    FOREIGN KEY (id_categoria) REFERENCES categoria_tarefa(id_categoria)
);

-- Inserção de valores iniciais para status
INSERT INTO status_tarefa (descricao) VALUES 
('Concluída'),
('Em andamento'),
('Pendente');

-- Inserção de valores iniciais para prioridades
INSERT INTO prioridade_tarefa (descricao) VALUES 
('Baixa'),
('Média'),
('Alta');

-- Inserção de valores iniciais para categorias
INSERT INTO categoria_tarefa (descricao) VALUES 
('Trabalho'),
('Estudo'),
('Pessoal');

-- Consulta para filtrar tarefas por status
SELECT * FROM tarefas
WHERE id_status = (SELECT id_status FROM status_tarefa WHERE descricao = 'Pendente');

-- Consulta para filtrar tarefas por data de criação
SELECT * FROM tarefas
WHERE data_criacao BETWEEN '2024-01-01' AND '2024-12-31';

-- Consulta para filtrar tarefas por prazo
SELECT * FROM tarefas
WHERE data_limite BETWEEN '2024-10-01' AND '2024-12-31';

-- Consulta para filtrar tarefas por prioridade
SELECT * FROM tarefas
WHERE id_prioridade = (SELECT id_prioridade FROM prioridade_tarefa WHERE descricao = 'Alta');

-- Consulta para filtrar tarefas por palavras-chave na descrição
SELECT * FROM tarefas
WHERE descricao LIKE '%palavra-chave%';

-- Consulta para filtrar tarefas por categoria
SELECT * FROM tarefas
WHERE id_categoria = (SELECT id_categoria FROM categoria_tarefa WHERE descricao = 'Trabalho');