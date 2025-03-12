import psycopg2

def obter_ultima_mensagem_sigmet():
    try:
        # Configuração da conexão com o banco de dados
        conexao = psycopg2.connect(
            host="seu_host",
            database="nome_do_banco",
            user="seu_usuario",
            password="sua_senha"
        )
        cursor = conexao.cursor()

        # Query para obter a última mensagem SIGMET da FIR Amazônica
        consulta = """
        SELECT numero_sigmet
        FROM opmet
        WHERE fir = 'SBAM'  -- FIR Amazônica
        ORDER BY data_hora DESC
        LIMIT 1;
        """
        cursor.execute(consulta)

        # Obter o resultado
        resultado = cursor.fetchone()

        if resultado:
            return resultado[0]
        else:
            return "Nenhuma mensagem SIGMET encontrada para a FIR Amazônica."

    except Exception as e:
        return f"Ocorreu um erro: {e}"

    finally:
        # Fechar a conexão
        if 'conexao' in locals():
            cursor.close()
            conexao.close()

# Exemplo de uso
print(obter_ultima_mensagem_sigmet())
