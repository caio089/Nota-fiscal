from reportlab.pdfgen import canvas

pdf = canvas.Canvas('meu_projeto.pdf')
y = 800
linha_altura = 20

def escrever(texto):
    global y
    pdf.setFont("Courier-Bold", 14)
    pdf.drawString(100, y, texto)
    y -= linha_altura
    print(texto)

# início
escrever('Emissor de Nota Fiscal')
escrever('Dados do Emitente (quem está vendendo/prestando o serviço):')

def Emitente():
    NomeR = input('Nome/Razão Social: ')
    CNPJ = input('CNPJ: ')
    Insc = input('Inscrição Estadual ou Municipal: ')
    end = input('Endereço completo: ')
    escrever(f'Emitente: {NomeR}')
    escrever(f'CNPJ: {CNPJ}')
    escrever(f'Inscrição: {Insc}')
    escrever(f'Endereço: {end}')

def destinatario():
    escrever('')
    escrever('Dados do Destinatário (quem está comprando/recebendo):')
    Nome = input('Nome/Razão social (ou CPF, se for pessoa física): ')
    CPF = input('CNPJ ou CPF: ')
    endereco = input('Endereço: ')
    res = input('Você tem Inscrição Estadual? (sim/não): ')
    if res.lower() == 'sim':
        inscricao = input('Qual é a inscrição? ')
        escrever(f'Inscrição Estadual: {inscricao}')
    escrever(f'Destinatário: {Nome}')
    escrever(f'CNPJ/CPF: {CPF}')
    escrever(f'Endereço: {endereco}')
    escrever('')

def dadosP():
    escrever('Dados dos produtos ou serviços')
    desc = input('Descrição: nome do produto ou serviço: ')
    uni = int(input('Unidades: '))
    valor = float(input('Valor unitário: '))
    estado = input('Estado: ')
    escrever(f'Descrição: {desc}')
    escrever(f'Unidades: {uni}')
    escrever(f'Valor: {valor}')
    escrever(f'Estado: {estado}')
    return valor, uni

def Rfinal(valor, uni):
    escrever('')
    escrever('Tributos (ICMS, IPI, PIS, COFINS)')
    escrever('ICMS: 18%')
    escrever('IPI: 10%')
    escrever('PIS: 0,65%')
    escrever('CONFINS: 3%')
    ValoR = valor * uni
    valor1 = valor * 0.18
    valor2 = valor * 0.10
    valor3 = valor * 0.0065
    valor4 = valor * 0.03
    valorT = (valor1 + valor2 + valor3 + valor4) * uni
    escrever(f'Valor total pago: R$ {ValoR:.2f}')
    escrever(f'Imposto total: R$ {valorT:.2f}')
    escrever('')
    escrever('CFOP (Código Fiscal da Operação)')
    escrever('Venda dentro do estado: 5102')
    escrever('Venda fora do estado: 6102')
    escrever('Devolução de venda: 1202 ou 2202')

# execução
Emitente()
destinatario()
valor, uni = dadosP()
Rfinal(valor, uni)
escrever('Fim da Nota Fiscal')
pdf.save()
