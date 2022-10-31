import os

info = {
    'name':str,
    'party':str,
    'number':int
}
votes = {
    13:0,
    22:0,
    'null':0
}
print("digite 'sair' para sair.")
while True:
    print('=== Justiça Eleitoral ===')
    vote = input('Digite seu voto: ')

    if vote == 'sair':
        break

    elif vote == 'nulo':
        info['name'] = 'null'
        info['party'] = 'null'
        info['number'] = 'null'

    elif int(vote) == 13:
        info['name'] = 'Luiz Inácio Lula da Silva'
        info['party'] = 'PT'
        info['number'] = 13

    elif int(vote) == 22:
        info['name'] = 'Jair Messias Bolsonaro'
        info['party'] = 'PL'
        info['number'] = 22
    
    print(
        f"Nome: {info['name']}\n",
        f"Partido: {info['party']}\n",
        f"Número: {info['number']}\n",
    )
    confirm = input('Confirmar voto? Y/n: ')

    if confirm == 'y' or 'Y':
        votes[info['number']] += 1
    
    os.system('cls')
os.system('cls')
votes_b = votes[22]
votes_l = votes[13]
null_votes = votes['null']
total_votes = sum(votes.values())
percent = lambda vote: (vote/total_votes) * 100 
print(
    f'Votos totais: [{total_votes}]\n\n'
    f'=== Resultado ===\n',
    f'Lula: {percent(votes_l):.2f}% [{votes_l}]\n',
    f'Bolsonaro: {percent(votes_b):.2f}% [{votes_b}]\n',
    f'Nulo: {percent(null_votes):.2f}% [{null_votes}]\n',
    f'================='
)