from backend.database import conectar

def inserir_usuarios():
    conn = conectar()
    cursor = conn.cursor()

    usuarios = [
        ('admin', 'admin123', 'dono'),
        ('joao', 'joao123', 'funcionario')
    ]

    cursor.executemany('''
        INSERT INTO usuarios (nome, senha, tipo) VALUES (?, ?, ?)
    ''', usuarios)

    conn.commit()
    conn.close()
    print("Usuários inseridos com sucesso!")

inserir_usuarios()
