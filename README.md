# gs1_python

Luis Alberto Rocha Filho | RM: 553507

# O projeto:
Crei esse projeto para poder desenvolver um metodo para priorização de pacientes em um ambulatorio ou hospital, pois
algumas vezes com as salas de espera muito cheias podemos ir dando mais prioridade para pacientes mais urgentes e esquecendo
dos outros por nao serem casos muito graves, afinal uma pessoa com uma simples dor de cabeça ou febre leve não tem tanta 
urgencia de atendimento quanto um paciente que esta com um ferimento aberto, osso quebrado ou ate mesmo inicio de infarto.

no codigo temos tres funções principais, que são:
-adcionar um novo paciente;
-deletar um paciente antigo;
-retornar o dataframe ordenado por prioridade;

Adcionar paciente: Será pedido algumas informções do paciente para o seu cadastro, sendo a ultima delas sobre
sua queixa ou doença, depois a função define qual o nivel de urgencia do paciente diante a queixa, será isso que definirá qual 
o tempo maximo de espera de um paciente, os valores utilizados são apenas exemplos, apos isso sera inserida os valores no dataframe
do paciente.

Deletar paciente: Serve justamente para remover o paciente que ja foi atendido da lista, a função será utilizada quando o paciente sair ambiente
ou quando entrar em atendimento.

ordernar data frame: É utilizada justamente para devolver a lista dos pacientes com suas informaçoes, grau de urgencia, 
queixa principal ou doença, horario de chegada e horario maximo de atendimento.


#instruções de uso:

Adcionar paciente: Ao adicionar um novo paciente sera pedida algumas informações, na opção de enfermidade voce deve colocar exatamente as opções escritas,
porem podemos otimizar com um banco de dados com as principais doenças e devolvera ao usuario conforme ele for escrevendo em um campo de 
busca que terá acesso a esses dados para otimizar o tempo de cadastro, as opçoes sao: (dor de cabeça, febre, hemorragia), se a doença apresentada 
não existir no banco de dados voce pode digitando errado ou nada que você será redirecionado para um input para definir a urgencia sendo 1, 2 ou 3 respectivamente, 
então será caulculado o tempo de espera que será de 1 hora, 30 min ou 10 min respectivamente, porem se for selecionado 0 sera adcionado a hora atual, pois se
entende que alguns casos não se podem esperar (podemos criar uma forma de quando for adcionado esse paciente os medicos e enfermeros serem alertados instantaneamente para
atenderem ele o mais rapido possivel) (podemos otimizar para uma funçao onde se apertara apenas um botão para maior agilidade), apos isso você receberá a tabela ja ordenada.

deletar paciente: Ao chamar a função você devera passar no imput gerado o numero do indice do array do paciente (posteriormente trocado por um id).

ordenar data frame: Você apenas precisara chamar a função que será retornado o dataframe ordenado por hora do atendimento.

(podemos criar outros tipos de colunas ou filtros para ver a tabela com outras formas de ordenar)

(as informações dos pacientes podem alimentar um banco de dados para estudos futuros, tantos ligados a parte da medicina, como tambem da parte comercial, 
como tempo de espera medio, se os pacientes estão sendo atendidos na hora, quais os casos com maiores numeros de novos pacientes, mortes, x mortes por doença etc.)

(esse projeto é extendido para a diciplina de edge, sendo la apenas uma pequena automação do uso geral, podendo ser mais desenvolvida no futuro.)
