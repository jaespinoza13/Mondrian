"""
read adult data set
"""

# !/usr/bin/env python
# coding=utf-8

# Read data and read tree functions for INFORMS data
# attributes ['age', 'work_class', 'final_weight', 'education', 'education_num',
# 'marital_status', 'occupation', 'relationship', 'race', 'sex', 'capital_gain',
# 'capital_loss', 'hours_per_week', 'native_country', 'class']
# QID ['age', 'work_class', 'education', 'marital_status', 'race', 'sex', 'native_country']
# SA ['occupation']

ATT_NAME = ['id', 'Númeración', 'prov_insc',
            'cant_insc','parr_insc','anio_insc', 
            'mes_insc','dia_insc','fecha_insc', 
            'nac_fall', 'cod_pais', 'sexo',
            'anio_nac', 'mes_nac', 'dia_nac',
            'fecha_nac', 'anio_fall', 'mes_fall',
            'dia_fall', 'fecha_fall', 'cod_edad', 
            'edad', 'prov_res', 'sabe_leer', 'etnia', 
            'lugar_ocur', 'prov_fall', 'cant_fall', 
            'parr_fall', 'muj_fertil', 'mor_viol', 
            'lug_viol', 'autopsia', 'causa4', 'cer_por', 
            'area_fall', 'area_res', 'est_civil', 'niv_inst',
            'residente', 'causa', 'lc1', 'causa103', 'causa80', 
            'causa67A', 'causa67B']

# ATT_NAME = ['age', 'work_class', 'final_weight', 'education',
#             'education_num', 'marital_status', 'occupation', 'relationship',
#             'race', 'sex', 'capital_gain', 'capital_loss', 'hours_per_week',
#             'native_country', 'class']
#QI_INDEX = [0]#, 1, 4, 5, 6, 8, 9, 13]
QI_INDEX = [11,21]#,21]
IS_CAT = [True,False]#,False]
#IS_CAT = [False]#, True, False, True, True, True, True, True]
SA_INDEX = -1
__DEBUG = False


def read_data():
    """
    read microdata for *.txt and return read data

    # Note that Mondrian can only handle numeric attribute
    # So, categorical attributes should be transformed to numeric attributes
    # before anonymization. For example, Male and Female should be transformed
    # to 0, 1 during pre-processing. Then, after anonymization, 0 and 1 should
    # be transformed to Male and Female.
    """
    QI_num = len(QI_INDEX)
    data = []
    # oder categorical attributes in intuitive order
    # here, we use the appear number
    intuitive_dict = []
    intuitive_order = []
    intuitive_number = []
    for i in range(QI_num):
        intuitive_dict.append(dict())
        intuitive_number.append(0)
        intuitive_order.append(list())
    #data_file = open('data/adult.data')
    data_file = open('data/defunciones2019_limpio.csv',encoding='utf-8')
    for line in data_file:
        line = line.strip()
        # remove empty and incomplete lines
        # only 30162 records will be kept
        if len(line) == 0 or '?' in line:
            continue
        # remove double spaces
        line = line.replace(' ', '')
        temp = line.split(',')
        ltemp = []
        for i in range(QI_num):
            index = QI_INDEX[i]
            if IS_CAT[i]:
                try:
                    ltemp.append(intuitive_dict[i][temp[index]])
                except KeyError:
                    intuitive_dict[i][temp[index]] = intuitive_number[i]
                    ltemp.append(intuitive_number[i])
                    intuitive_number[i] += 1
                    intuitive_order[i].append(temp[index])
            else:
                ltemp.append(int(temp[index]))
        ltemp.append(temp[SA_INDEX])
        data.append(ltemp)
    return data, intuitive_order
