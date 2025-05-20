from reportlab.pdfgen import canvas

pdf = canvas.Canvas('meu projeto.pdf')
y = 800
linha_altura = 20

def escrever (texto):
    global y
    pdf.setFont("Courier-Bold", 14)
    pdf.drawString(100,y,texto)
    y -= linha_altura
    print(texto)


    #começo
escrever('Emissor de Nota Fiscal')
escrever('Dados do Emitente (quem está vendendo/prestando o serviço):')

# Emitente
NomeR = input('Nome/Razão Social: ')
CNPJ = input('CNPJ: ')
Insc = input('Inscrição Estadual ou Municipal: ')
end = input('Endereço completo: ')


escrever(f'Emitente: {NomeR}')
escrever(f'CNPJ: {CNPJ}')
escrever(f'Inscrição: {Insc}')
escrever(f'Endereço: {end}')
              
# Destinatário
escrever('')
escrever('Dados do Destinatário (quem está comprando/recebendo):')

Nome = input('Nome/Razão social (ou CPF, se for pessoa física): ')
CPF = input('CNPJ ou CPF: ')
endereco = input('Endereço: ')
res = input('Você tem Inscrição Estadual? (sim/não): ')

escrever(f'Destinatário: {Nome}')
escrever(f'CNPJ/CPF: {CPF}')
escrever(f'Endereço: {endereco}')   

escrever("") 
escrever('Dados dos produtos ou serviços')

desc = input('Descrição: nome do produto ou serviço: ')
uni = int(input('unidades: '))
valor = float(input('valor unitario: '))
estado = input('estado: ')

escrever(f'descriçao: {desc}')
escrever(f'unidades: {uni}')
escrever(f'valor: {valor}')
escrever(f'estado: {estado}')

escrever('')

escrever('Tributos (ICMS, IPI, PIS, COFINS')
escrever('ICMS:18%')
escrever('IPI:10%')
escrever('PIS:0,65%')
escrever('CONFINS:3%')

ValoR = valor * uni
valor1 = valor * 0.018
valor2 = valor * 0.1
valor3 = valor * 0.00065
valor4 = valor *0.003
valorT = (valor1 + valor2 + valor3 + valor4) * uni
escrever(f'valor total pago: {ValoR}')
escrever(f'imposto: {float(valorT)}')

escrever("") 
escrever('CFOP (Código Fiscal da Operação)')
escrever('Venda dentro do estado: 5102')
escrever('Venda fora do estado: 6102')
escrever('Devolução de venda: 1202 ou 2202')

escrever('fim da Nota Fiscal')

pdf.save()