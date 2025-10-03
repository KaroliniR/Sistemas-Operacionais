import threading
import time

# Recurso Compartilhado 
saldo = 1000


# --- Configuração da Simulação ---
NUM_THREADS = 10
SAQUES_POR_THREAD = 100
VALOR_SAQUE = 1

# --- Função da Thread ---
def realizar_operacoes():
    """
    Esta função simula uma pessoa realizando múltiplos saques.
    """
    global saldo
    
    for _ in range(SAQUES_POR_THREAD):
        
        # --- SEÇÃO CRÍTICA (Início) ---
        saldo_local = saldo
        novo_saldo = saldo_local - VALOR_SAQUE
        
        time.sleep(0.0001) 
        
        saldo = novo_saldo
        # --- SEÇÃO CRÍTICA (Fim) ---


# --- Função Principal ---
if __name__ == "__main__":
    saldo_inicial = saldo
    print("Saldo inicial da conta: R$ {:.2f}".format(saldo_inicial))
    print("Configuração: {} threads, cada uma fazendo {} saques de R$ {:.2f}".format(NUM_THREADS, SAQUES_POR_THREAD, VALOR_SAQUE))
    print("-" * 40)
    
    threads = []

    # Cria e inicia as threads
    for i in range(NUM_THREADS):
        thread = threading.Thread(target=realizar_operacoes)
        threads.append(thread)
        thread.start()

    # Espera todas as threads terminarem
    for thread in threads:
        thread.join()

    print("-" * 40)
    print("Todas as threads terminaram a execução.")
    
    # Calcula e exibe os resultados
    saldo_final_real = saldo
    saque_total = NUM_THREADS * SAQUES_POR_THREAD * VALOR_SAQUE
    saldo_final_esperado = saldo_inicial - saque_total

    # imprima os resultados
    print("\n--- Resultados ---")
    print("Valor total que deveria ter sido sacado: R$ {:.2f}".format(saque_total))
    print("Saldo final esperado na conta: R$ {:.2f}".format(saldo_final_esperado))
    print("SALDO FINAL REAL NA CONTA (BUG): R$ {:.2f}".format(saldo_final_real))
    
    diferenca = saldo_final_esperado - saldo_final_real
    if diferenca != 0:
        print("\n>> Condição de Corrida OCORREU! O banco perdeu R$ {:.2f}".format(-diferenca))