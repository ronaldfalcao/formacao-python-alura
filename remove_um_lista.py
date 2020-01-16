def rem(lista):
    i = 0
    seen = set()
    nova_lista = lista.copy()
    while i < len(lista):
        # print(lista[i])

        if lista.count(lista[i]) >= 2:

            if lista[i] not in seen:
                nova_lista.remove(lista[i])
                seen.add(lista[i])

        i += 1
        print(f"seen :{seen}, nova_lista:{nova_lista}")
    print()
    print(nova_lista)


# Permite rodar no terminal
if __name__ == '__main__':    
    
    # lista = [3,4,5,6,5,5]
    # lista = [4,4]
    # lista = [3,4,5,6,5,5,5,6,6,3,6,4]
        
    lista = [0]
    rem(lista)