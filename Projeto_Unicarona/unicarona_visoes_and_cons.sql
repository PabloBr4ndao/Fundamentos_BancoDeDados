-- ====================================================================
-- UNIVERSIDADE FEDERAL DO CEARÁ - CAMPUS QUIXADÁ
-- QXD0011 - FUNDAMENTOS DE BANCO DE DADOS
-- PROF. FRANCISCO VICTOR DA SILVA PINHEIRO
--
-- TRABALHO FINAL - Comandos SQL das visões, criação de usuários e permissões (ENTREGA 4)
-- SISTEMA: UNICARONA
-- EQUIPE: 
--   - Francisca Ariane dos Santos da Silva
--   - Gabriel Braga Martins
--   - Kailany Sofia Alves de Lima
--   - Pablo Brandão Passos
--   - Raul Camurça Rabelo de Almeida
-- ====================================================================

-- ====================================================================
-- 1. VISÃO: vw_detalhes_caronas
-- Consolida os dados operacionais de todas as caronas, trazendo os nomes 
-- do motorista, veículo, placa, origem, destino, data, horário e vagas disponíveis.
-- Evita que a aplicação tenha que fazer 5 JOINs toda vez que listar viagens (por exemplo).
-- ====================================================================
CREATE OR REPLACE VIEW vw_detalhes_caronas AS
SELECT C.id_carona, 
       U.nome AS motorista, 
       V.modelo AS veiculo, 
       V.placa,
       L1.nome_local AS origem, 
       L2.nome_local AS destino, 
       C.data, 
       C.horario, 
       C.vagas_disponiveis
FROM CARONA C
JOIN MOTORISTA M ON C.cpf_motorista = M.cpf
JOIN USUARIO U ON M.cpf = U.cpf
JOIN VEICULO V ON C.placa_veiculo = V.placa
JOIN LOCAL L1 ON C.id_origem = L1.id_local
JOIN LOCAL L2 ON C.id_destino = L2.id_local;

-- ====================================================================
-- 2. VISÃO: vw_ranking_motoristas
-- Agrega as notas da tabela de avaliações para gerar um 
-- ranking de reputação dos motoristas com média arredondada, filtrando 
-- apenas quem tem boa atividade na plataforma.
-- ====================================================================
CREATE OR REPLACE VIEW vw_ranking_motoristas AS
SELECT U.nome AS motorista, 
       ROUND(AVG(A.nota)::numeric, 2) AS media_reputacao,
       COUNT(A.id_avaliacao) AS total_avaliacoes_recebidas
FROM AVALIACAO A
JOIN MOTORISTA M ON A.cpf_avaliado = M.cpf
JOIN USUARIO U ON M.cpf = U.cpf
GROUP BY U.cpf, U.nome
ORDER BY media_reputacao DESC;

-- ====================================================================
-- CONTROLE DE ACESSO (DCL)
-- ====================================================================

-- Criando os usuários
CREATE USER unicarona_admin WITH PASSWORD 'admin_unicarona_2026';
CREATE USER unicarona_leitura WITH PASSWORD 'leitura_unicarona_2026';

-- 1. Permissões do Usuário Admin (Privilégios totais de leitura e escrita)
GRANT ALL PRIVILEGES ON DATABASE unicarona TO unicarona_admin;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO unicarona_admin;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO unicarona_admin;

-- 2. Permissões do Usuário Somente Leitura (Apenas SELECT)
-- Revogando qualquer direito de escrita
REVOKE INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public FROM unicarona_leitura;

-- Concedendo estritamente o acesso de leitura nas tabelas e visões
GRANT CONNECT ON DATABASE unicarona TO unicarona_leitura;
GRANT USAGE ON SCHEMA public TO unicarona_leitura;
GRANT SELECT ON ALL TABLES IN SCHEMA public TO unicarona_leitura;
GRANT SELECT ON ALL SEQUENCES IN SCHEMA public TO unicarona_leitura;