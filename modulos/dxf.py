#--coding: utf-8 --

import ezdxf


def PositionLast(x, s):  # Encontra posicao da ultima ocorrencia de um char
    count = len(s)
    for i in s[::-1]:
        count -= 1
        if i == x:
            return count
    return None


def enderecoFinalParaSalvarDxf(endereco2dxfpontos,doisDtresD):

    posicao_do_ultimo_ponto = PositionLast(".", endereco2dxfpontos)

    endereco_sem_o_nome_arquivo = endereco2dxfpontos[0:posicao_do_ultimo_ponto]

    endereco_final_do_arquivo_dxf_completo = endereco_sem_o_nome_arquivo + doisDtresD

    return endereco_final_do_arquivo_dxf_completo


# ESSE CHAMA O DA ABA PONTOS 2 DXF
def gravaPontosEmDxf(vax,vay,vaz,indice,descricao,descricao_layer,nome_completo_do_arquivo_dxf):

    # Create a new drawing in the DXF format of AutoCAD 2004
    dwg = ezdxf.new('ac1018')
    # Get the modelspace of the drawing.
    modelspace = dwg.modelspace()
    dwg.styles.new('novo', dxfattribs={'font': 'arial.ttf', 'width': 0.8})  # Arial, default width factor of 0.8

    COR_LARANJA = 20
    COR_VERDE = 3
    COR_AZUL = 4
    COR_VERMELHA = 1
    COR_PONTO = 0
    COR_DESCR = 0
    COR_COTAZ = 0
    COR_AMARELA = 2

    flag = dwg.blocks.new("CRUZETA_BOLINHA")
    flag.add_circle((0, 0), 0.5, dxfattribs={'color': COR_VERDE})
    flag.add_point((0, 0), dxfattribs={'color': COR_VERDE})

    for i in range(len(vax)):

        if descricao[i] == 'V':
            COR_PONTO == COR_LARANJA
            COR_COTAZ == COR_VERMELHA
            COR_DESCR == COR_LARANJA
        else:
            COR_PONTO = COR_VERMELHA
            COR_DESCR = COR_AZUL
            COR_COTAZ = COR_VERMELHA

        blockref = modelspace.add_blockref("CRUZETA_BOLINHA", (float(vax[i]), float(vay[i]), float(vaz[i])),
                                           dxfattribs={'layer': "_" + descricao[i]})

        blockref.add_attrib("PONTO", indice[i],
                            dxfattribs={'color': COR_PONTO, 'height': 0.4, 'layer': "_" + descricao[i]}).set_pos(
            ((float(vax[i]) + 0.3), (float(vay[i]) + 0.6)), align="MIDDLE_CENTER")

        blockref.add_attrib("DESC", descricao[i],
                            dxfattribs={'style': 'novo', 'color': COR_DESCR, 'height': 0.3,
                                        'layer': "_" + descricao[i]}).set_pos(
            (float(vax[i]) - 0.7, float(vay[i]) - 0.7), align="LEFT")

        blockref.add_attrib("COTA", vaz[i],
                            dxfattribs={'style': 'novo', 'color': COR_COTAZ, 'height': 0.3, 'layer': "_zCOTA"}).set_pos(
            (float(vax[i]) - 0.7, float(vay[i]) - 1.1), align="LEFT")

    dwg.saveas(nome_completo_do_arquivo_dxf)
    print("Arquivo dxf Salvo em: " + nome_completo_do_arquivo_dxf)


'''////////////////////////////////////////////////////////////////////////////////////'''

# ESSE RECEBE OS PARAMETROS DA ABA TOPOGRAFIA
def gravaPontosEstacaoEmDxf(vax,vay,vaz,indice,descricao,descricao_layer, nome_completo_do_arquivo_dxf,N_estacao,E_estacao,Z_estacao,indice_estacao,descricao_estacao):

    # Create a new drawing in the DXF format of AutoCAD 2004
    dwg = ezdxf.new('ac1018')
    # Get the modelspace of the drawing.
    modelspace = dwg.modelspace()
    dwg.styles.new('novo', dxfattribs={'font': 'arial.ttf', 'width': 0.8})  # Arial, default width factor of 0.8

    COR_LARANJA = 20
    COR_VERDE = 3
    COR_AZUL = 4
    COR_VERMELHA = 1
    COR_PONTO = 0
    COR_DESCR = 0
    COR_COTAZ = 0
    COR_AMARELA = 2

    flag = dwg.blocks.new("CRUZETA_BOLINHA")
    flag.add_circle((0, 0), 0.5, dxfattribs={'color': COR_VERDE})
    flag.add_point((0,0), dxfattribs={'color': COR_VERDE})


    for i in range(len(vax)):





        if descricao[i] == 'V':
            COR_PONTO == COR_LARANJA
            COR_COTAZ == COR_VERMELHA
            COR_DESCR == COR_LARANJA
        else:
            COR_PONTO = COR_VERMELHA
            COR_DESCR = COR_AZUL
            COR_COTAZ = COR_VERMELHA




        blockref = modelspace.add_blockref("CRUZETA_BOLINHA", (float(vax[i]), float(vay[i]), float(vaz[i])), dxfattribs={'layer': "_"+descricao[i]})

        blockref.add_attrib("PONTO", indice[i], dxfattribs={'color': COR_PONTO, 'height': 0.4, 'layer': "_"+descricao[i]}).set_pos(
            ((float(vax[i]) + 0.3), (float(vay[i]) + 0.6)), align="MIDDLE_CENTER")

        blockref.add_attrib("DESC", descricao[i],
                            dxfattribs={'style': 'novo', 'color': COR_DESCR, 'height': 0.3, 'layer': "_"+descricao[i]}).set_pos(
            (float(vax[i]) - 0.7, float(vay[i]) - 0.7), align="LEFT")

        blockref.add_attrib("COTA", vaz[i],
                            dxfattribs={'style': 'novo', 'color': COR_COTAZ, 'height': 0.3, 'layer': "_zCOTA"}).set_pos(
            (float(vax[i]) - 0.7, float(vay[i]) - 1.1), align="LEFT")




    # QUANDO A ESTAÇÃO TIVER COORDENADAS DIFERENTE DE ZERO

    if N_estacao and E_estacao and Z_estacao:
        vax = E_estacao
        vay = N_estacao
        vaz = Z_estacao

    else:

        vax = 0
        vay = 0
        vaz = 0

    blockref = modelspace.add_blockref("CRUZETA_BOLINHA", (float(vax), float(vay), float(vaz)),
                                       dxfattribs={'layer': "_E"})

    blockref.add_attrib("PONTO", "0",
                        dxfattribs={'color': COR_AMARELA, 'height': 0.4, 'layer': "_E"}).set_pos(
        ((float(vax) + 0.3), (float(vay)+ 0.6)), align="MIDDLE_CENTER")

    blockref.add_attrib("DESC", "E",
                        dxfattribs={'style': 'novo', 'color': COR_DESCR, 'height': 0.3,
                                    'layer': "_E"}).set_pos(
        (float(vax) - 0.7, float(vay) - 0.7), align="LEFT")

    blockref.add_attrib("COTA", vaz,
                        dxfattribs={'style': 'novo', 'color': COR_COTAZ, 'height': 0.3, 'layer': "_zCOTA"}).set_pos(
        (float(vax) - 0.7, float(vay) - 1.1), align="LEFT")

    dwg.saveas(nome_completo_do_arquivo_dxf)
    print("Arquivo dxf Salvo em: " + nome_completo_do_arquivo_dxf)



    '''////////////////////////////////////////////////////////////////////////////////////'''










