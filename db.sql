-- Script de Criação do Banco de Dados e Tabela

-- Criação do Banco de Dados
CREATE SCHEMA  `ouvidoria`;

-- Seleção do Banco de Dados
USE ouvidoria;

-- Criação da Tabela ouvidoria
CREATE TABLE ouvidoria (
    codigo INT AUTO_INCREMENT,
    nome VARCHAR(100),
    tipo VARCHAR(50),
    descricao VARCHAR(255),
    PRIMARY KEY (codigo)
);

-- Inserção de dados de teste (Manifestações)
INSERT INTO ouvidoria (nome, tipo, descricao) VALUES 
('João da Silva', 'Reclamação', 'O sistema apresenta lentidão durante o horário de pico.'),
('Maria Oliveira', 'Elogio', 'O atendimento do suporte foi excelente e rápido.'),
('Carlos Souza', 'Sugestão', 'Seria interessante ter um aplicativo móvel para facilitar o acesso.'),
('Ana Pereira', 'Reclamação', 'Não recebi o protocolo de atendimento por e-mail.'),
('Lucas Mendes', 'Denúncia', 'Há inconsistências nos relatórios financeiros do mês passado.'),
('Fernanda Costa', 'Elogio', 'Adorei a nova interface do usuário, ficou muito intuitiva.'),
('Roberto Almeida', 'Sugestão', 'Poderiam incluir um modo noturno nas configurações.'),
('Juliana Santos', 'Reclamação', 'Estou tentando cancelar meu cadastro e não consigo.'),
('Paulo Rodrigues', 'Denúncia', 'Presenciei um ato de desrespeito de um funcionário.'),
('Camila Lima', 'Elogio', 'A resolução do meu problema foi muito ágil, parabéns!'),
('Ricardo Ferreira', 'Sugestão', 'Aumentar o prazo para pagamento das faturas seria ótimo.'),
('Patrícia Gomes', 'Reclamação', 'O telefone de contato nunca atende.'),
('Marcos Vinícius', 'Denúncia', 'Identifiquei uma falha de segurança no login.'),
('Eduarda Martins', 'Elogio', 'O atendente Carlos foi muito educado e prestativo.'),
('Gustavo Henrique', 'Sugestão', 'Deveria ter uma opção de chat online no site.'),
('Gabriel Torres', 'Reclamação', 'Cobrança indevida na fatura deste mês.'),
('Beatriz Rocha', 'Elogio', 'A entrega do produto foi realizada antes do prazo previsto.'),
('Felipe Araujo', 'Sugestão', 'Seria legal criar um programa de fidelidade para clientes antigos.'),
('Mariana Costa', 'Denúncia', 'Suspeita de uso indevido de dados pessoais por terceiros.'),
('Rafael Barbosa', 'Reclamação', 'O site trava sempre que tento finalizar a compra.'),
('Larissa Silva', 'Elogio', 'Estou muito satisfeita com a qualidade do serviço prestado.'),
('Thiago Nogueira', 'Sugestão', 'Melhorar a descrição técnica dos produtos no site.'),
('Amanda Souza', 'Reclamação', 'Estou com dificuldade para redefinir minha senha de acesso.'),
('Bruno Cardoso', 'Denúncia', 'A promoção divulgada não está sendo aplicada no carrinho.'),
('Jessica Lima', 'Elogio', 'Equipe muito atenciosa, resolveram minha dúvida rapidamente.');
