# Sistemas-Operacionais
🔴Aulas Quintas-feiras na sala LAB 110A e Sextas-feiras na SALA 202A das 18h30 às 20h10🔴

Condição de Corrida em uma Conta Bancária

Imagine uma conta bancária conjunta compartilhada por várias pessoas. Cada pessoa tem um cartão e pode fazer saques. O que aconteceria se duas pessoas tentassem sacar R$ 100 exatamente ao mesmo tempo, quando o saldo da conta é de apenas R$ 150?
Em um sistema bancário robusto, uma transação seria aprovada e a outra recusada. Mas em um programa simples e sem as devidas proteções, um erro grave pode ocorrer:
Pessoa A olha o saldo: R$ 150. O saque de R$ 100 é válido.
Exatamente no mesmo instante, antes da Pessoa A concluir o saque, a Pessoa B também olha o saldo: R$ 150. O saque de R$ 100 também parece válido.
Pessoa A completa a operação: R$ 150 - R$ 100 = R$ 50. O novo saldo é R$ 50.
Pessoa B também completa a sua operação, baseada no saldo de R$ 150 que ela leu: R$ 150 - R$ 100 = R$ 50. O novo saldo também é R$ 50.
Resultado: Duas pessoas sacaram R$ 100 cada (total R$ 200), mas o saldo da conta só diminuiu em R$ 100. O banco perdeu R$ 100! Este bug é conhecido como Condição de Corrida (Race Condition). Ele ocorre quando o resultado de uma operação depende da ordem imprevisível de execução de múltiplas threads acessando um recurso compartilhado.

Exercício
Seu objetivo é simular exatamente este problema. Você criará um programa com múltiplas threads que realizarão saques simultâneos de uma conta bancária compartilhada. O desafio será dividido em duas partes:
Parte 1 (aula 02/10): Implementar a simulação sem nenhuma proteção para observar a condição de corrida acontecer e o saldo final da conta ficar incorreto.
Parte 2 (aula 09/10): Corrigir o problema implementando um Mutex (Lock) para proteger o acesso à conta, garantindo que o saldo final seja sempre o correto.
