import pandas as pd
import numpy as np


def generarDataFrame():
    # Leemos los dataframes (Niñxs y abuelxs)
    df = pd.read_csv('Datasets/Características y composición del hogar.csv',
                     sep=';', decimal=',', header=0)

    eliminar = ['SECUENCIA_P', 'ORDEN', 'FEX_C', 'P6016', 'P6071S1', 'P756', 'P756S1', 'P756S2', 'P756S3', 'P6074',
                'P767', 'P6076', 'P6076S1', 'P6076S2', 'P6077', 'P6096', 'P6081S1', 'P6083S1', 'P5667', 'P1894', 'P6034']

    posibles = ['P6051', 'P6087', 'P6088', 'P2057', 'P2059',
                'P2061', 'P1901', 'P1903', 'P1904', 'P1905', 'P1927']

    dejar = ['P6020', 'P6040', 'P6080', 'P1895',
             'P1896', 'P1897', 'P1898', 'P1899', 'P3175', 'P6071']

    # Se eliminan columnas que no se usarán
    df = df.drop(columns=eliminar)
    df = df.drop(columns=posibles)

    # Espacios en blanco como nulos
    df = df.replace(r'^\s*$', np.nan, regex=True)

    # Pasar a flotante
    df[['P1895', 'P1896', 'P1897', 'P1898', 'P1899', 'P3175']] = \
        df[['P1895', 'P1896', 'P1897', 'P1898',
            'P1899', 'P3175', ]].astype(float)

    # Se reemplazan los nulos con la media, agrupado por directorio
    df[['P1895', 'P1896', 'P1897', 'P1898', 'P1899', 'P3175']] = \
        df[['P1895', 'P1896', 'P1897', 'P1898', 'P1899', 'P3175']]\
        .fillna(df.groupby('DIRECTORIO')[['P1895', 'P1896', 'P1897', 'P1898', 'P1899', 'P3175']].transform('mean').round(0))

    # Eliminamos las filas que tengan satisfacción nula, ya que es la variable resultado y es necesaria para el modelo
    df = df.dropna(subset=['P1895', 'P1896', 'P1897',
                   'P1898', 'P1899', 'P3175'])
    df = df.replace(np.nan, -1)

    # Pasar a entero
    df = df.astype(int)

    # Los datos atípicos mayores a 10 se igualan a 10
    df.loc[df['P1896'].gt(10), 'P1896'] = 10
    # Se crea una variable con el promedio se satisfacción por persona
    df['prom_satisfaccion'] = df[['P1895', 'P1896',
                                  'P1897', 'P1898', 'P1899', 'P3175']].mean(axis=1).round(2)

    # Se eliminan columnas que no se usarán
    # df = df.drop(columns=['P1895', 'P1896', 'P1897',
    #             'P1898', 'P1899', 'P3175'])

    # Trabajo infantil
    df_ti = pd.read_csv('Datasets/Trabajo infantil.csv',
                        sep=';', decimal=',', header=0)

    eliminar = ['SECUENCIA_P', 'ORDEN', 'FEX_C', 'P10000', 'P404',
                'P408', 'P4900', 'P406S2', 'P407S2', 'P809', 'P420']

    posibles = ['P6850', 'P5971', 'P5971S1', 'P5971S1A1', 'P5971S2', 'P5971S2A1', 'P5971S3', 'P5971S3A1', 'P5971S4', 'P5971S4A1', 'P5971S5',
                'P5971S5A1', 'P5971S6', 'P5971S6A1', 'P5971S7', 'P5971S7A1', 'P5971S8', 'P5971S8A1', 'P5971S9', 'P5971S9A1', 'P5971S10', 'P5971S10A1']

    dejar = ['P400', 'P401', 'P402', 'P403', 'P807', 'P809S1', 'P171']

    # Se eliminan columnas que no se usarán
    df_ti = df_ti.drop(columns=eliminar)
    df_ti = df_ti.drop(columns=posibles)

    # Se convierte a entero
    df_ti = df_ti.replace(r'^\s*$', 0, regex=True)
    df_ti = df_ti.astype(int)

    # Se crea una columna que indica si trabaja o no
    df_ti.loc[df_ti['P400'].eq(1) | df_ti['P401'].eq(1) |
              df_ti['P402'].eq(1) | df_ti['P403'].eq(1), 'trabaja'] = 1
    df_ti['trabaja'] = df_ti['trabaja'].fillna(0)

    # Dinero que gana
    df_ti['dinero'] = df_ti['P807'] + df_ti['P809S1']
    # Se eliminan columnas que no se usarán
    df_ti = df_ti.drop(
        columns=['P400', 'P401', 'P402', 'P403', 'P807', 'P809S1'])

    # Educación
    df_ed = pd.read_csv('Datasets/Educación.csv',
                        sep=';', decimal=',', header=0)

    eliminar = ['SECUENCIA_P', 'ORDEN', 'FEX_C', 'P6218', 'P8587S1', 'P6211', 'P1088', 'P1088S1', 'P6216', 'P5673', 'P5674', 'P6223', 'P1101', 'P3191', 'P4693', 'P6167', 'P6180', 'P6180S1', 'P6180S2', 'P8610', 'P8610S1', 'P8610S2', 'P6229',
                'P8612', 'P8612S1', 'P8612S2', 'P6238', 'P8614', 'P8614S1', 'P8614S2', 'P6202', 'P3192', 'P781', 'P781S1', 'P781S2', 'P782', 'P783', 'P3004', 'P3004S1', 'P3004S2', 'P3004S3', 'P3004S4', 'P3004S5', 'P3004S6', 'P3004S7', 'P3004S8']

    posibles = []

    dejar = ['P6160', 'P8586']

    # Se eliminan columnas que no se usarán
    df_ed = df_ed.drop(columns=eliminar)
    df_ed = df_ed.drop(columns=posibles)

    # Se convierte a entero
    df_ed = df_ed.replace(r'^\s*$', 0, regex=True)
    df_ed = df_ed.astype(int)

    # Salud
    df_sld = pd.read_csv('Datasets/Salud.csv', sep=';', decimal=',', header=0)

    eliminar = ['SECUENCIA_P', 'ORDEN', 'FEX_C', 'P768', 'P6115', 'P5669', 'P5669S1', 'P798', 'P799', 'P1930S1', 'P1906', 'P1908', 'P1908S1', 'P1908S2', 'P1908S3', 'P1908S4', 'P1908S5', 'P1908S6', 'P1908S7', 'P1908S8', 'P5665', 'P6134', 'P8563', 'P1092', 'P8573', 'P8575', 'P8577', 'P770', 'P6153', 'P6199', 'P6199S1', 'P6145', 'P8554', 'P801', 'P8556', 'P8556S1', 'P8556S2', 'P8556S4', 'P8556S5', 'P8556S6', 'P8556S9', 'P8556S10', 'P6147', 'P6148', 'P6149', 'P3178', 'P3178S1', 'P3178S1A1', 'P3178S2', 'P3178S2A1', 'P3178S3', 'P3178S3A1', 'P3179',
                'P3179S1', 'P3179S1A1', 'P3179S2', 'P3179S2A1', 'P3179S3', 'P3179S3A1', 'P3181', 'P3181S1', 'P3182', 'P3183', 'P3183S1', 'P3184', 'P3184S1', 'P3182S1', 'P3185', 'P3185S1', 'P3186', 'P3186S1', 'P3187S1', 'P3187S2', 'P3188', 'P3188S1', 'P3188S2', 'P3188S3', 'P3188S1A1', 'P3188S2A1', 'P3188S3A1', 'P3008', 'P3008S1A1', 'P3008S1A2', 'P1707S1', 'P3003S1', 'P6133', 'P8560', 'P8560S1', 'P8560S2', 'P8560S3', 'P8560S4', 'P8560S5', 'P3189', 'P3189S1', 'P3189S1A1', 'P3189S2', 'P3189S2A1', 'P8561', 'P6138', 'P5672', 'P5694', 'P5695', 'P6161', 'P1089',
                'P1906S1', 'P1906S2', 'P1906S3', 'P1906S4', 'P1906S5', 'P1906S6', 'P1906S7', 'P1906S8', 'P1708', 'P1708S1']

    posibles = ['P6181', 'P6127', 'P1909', 'P1909S1', 'P1909S2', 'P1909S3',
                'P1909S4', 'P1909S5', 'P1909S6', 'P6126', 'P6126S1', 'P6126S2', 'P6126S3',
                'P8551', 'P799S2', 'P799S3', 'P799S1', 'P799S4', 'P799S5', 'P3176',
                'P3008S1', 'P3008S2', 'P1707', 'P3003', 'P5452', 'P6161S1']

    dejar = ['P6090', 'P6100', 'P1930']

    # Se eliminan columnas que no se usarán
    df_sld = df_sld.drop(columns=eliminar)
    df_sld = df_sld.drop(columns=posibles)

    # Se reemplazan los nulos según corresponda
    df_sld['P6100'] = df_sld['P6100'].replace(r'^\s*$', 9, regex=True)
    df_sld = df_sld.astype(int)

    # Atención Niños
    df_aten = pd.read_csv(
        'Datasets/Atencion integral de los niños y niñas menores de 5 años.csv', sep=';', decimal=',', header=0)

    eliminar = ['SECUENCIA_P', 'ORDEN', 'FEX_C', 'P6169', 'P6169S1', 'P8564', 'P8564S1', 'P8566', 'P8566S1', 'P8568', 'P8568S1', 'P6191', 'P6191S1', 'P8572', 'P8572S1', 'P8574', 'P8574S1', 'P8576', 'P8576S1', 'P55', 'P774', 'P774S1',
                'P774S2', 'P774S3', 'P775', 'P776', 'P776S1', 'P776S2', 'P776S3', 'P58S1', 'P58S2', 'P777', 'P778', 'P779', 'P779S1', 'P779S2', 'P779S3', 'P779S11', 'P779S12', 'P779S5', 'P779S6', 'P779S7', 'P779S8', 'P779S13', 'P779S9']

    posibles = ['P58']

    dejar = ['P51', 'P771', 'P772', 'P773']

    # Se eliminan columnas que no se usarán
    df_aten = df_aten.drop(columns=eliminar)
    df_aten = df_aten.drop(columns=posibles)

    # Se reemplazan los nulos según corresponda
    df_aten['P771'] = df_aten['P771'].replace(r'^\s*$', 9, regex=True)
    df_aten[['P772', 'P773']] = df_aten[['P772', 'P773']
                                        ].replace(r'^\s*$', 0, regex=True)
    df_aten['P773'] = df_aten['P773'].replace(r'^\s*$', 0, regex=True)
    df_aten[['P779S1A1', 'P779S2A1', 'P779S3A1', 'P779S11A1', 'P779S12A1', 'P779S5A1', 'P779S6A1', 'P779S7A1', 'P779S8A1', 'P779S13A1', 'P779S9A2', 'P779S14']] = \
        df_aten[['P779S1A1', 'P779S2A1', 'P779S3A1', 'P779S11A1', 'P779S12A1', 'P779S5A1', 'P779S6A1',
                 'P779S7A1', 'P779S8A1', 'P779S13A1', 'P779S9A2', 'P779S14']].replace(r'^\s*$', 0, regex=True)
    df_aten = df_aten.astype(int)

    # Se crea una columna donde especifica cada cuanto hace alguna actividad diferente
    df_aten.loc[df_aten['P779S14'].eq(1), 'P779S14'] = 5
    df_aten['actividad'] = \
        df_aten[['P779S1A1', 'P779S2A1', 'P779S3A1', 'P779S11A1', 'P779S12A1', 'P779S5A1',
                 'P779S6A1', 'P779S7A1', 'P779S8A1', 'P779S13A1', 'P779S9A2', 'P779S14']].min(axis=1)

    # Se eliminan columnas que no se usarán
    df_aten = df_aten.drop(columns=['P779S1A1', 'P779S2A1', 'P779S3A1', 'P779S11A1', 'P779S12A1',
                                    'P779S5A1', 'P779S6A1', 'P779S7A1', 'P779S8A1', 'P779S13A1', 'P779S9A2', 'P779S14'])

    # Fuerza de trabajo
    df_fuerza = pd.read_csv('Datasets/Fuerza de trabajo.csv',
                            sep=';', decimal=',', header=0)

    eliminar = ['SECUENCIA_P', 'ORDEN', 'FEX_C', 'P6230', 'P6240', 'P6250', 'P6260', 'P6270', 'P6280', 'P6300', 'P6330', 'P6340', 'P6351', 'P6370S2', 'P6390S2', 'P6435', 'P6440', 'P6450', 'P6460', 'P6460S1', 'P6990', 'P8622', 'P8624', 'P6595', 'P6605', 'P6605', 'P6623', 'P6615', 'P8626', 'P8626S1', 'P8628', 'P8628S1', 'P8630', 'P8630S1', 'P8631', 'P8631S1', 'P1087', 'P1087S1', 'P1087S1A1', 'P1087S2', 'P1087S2A1', 'P1087S3', 'P1087S3A1', 'P1087S4', 'P1087S4A1', 'P1087S5', 'P1087S5A1', 'P8632', 'P8634', 'P6885', 'P6886', 'P415', 'P416', 'P6830', 'P3193S1', 'P3193S2',
                'P3193S3', 'P3193S4', 'P1709', 'P1709S1', 'P1709S2', 'P1709S3', 'P1709S4', 'P1709S5', 'P1709S6', 'P1709S7', 'P1709S8', 'P1709S9', 'P1709S10', 'P1709S11', 'P1709S12', 'P8636', 'P7250', 'P7310', 'P7270S2', 'P8640', 'P8640S1', 'P6920', 'P6935', 'P8642', 'P8642S1', 'P8644', 'P8644S1', 'P8646', 'P8650', 'P8650S1', 'P8652', 'P8654', 'P421', 'P421S1', 'P421S1A1', 'P421S2', 'P421S2A1', 'P421S3', 'P421S3A1', 'P421S4', 'P421S4A1', 'P421S5', 'P421S5A1', 'P421S6', 'P421S6A1', 'P421S7', 'P421S7A1', 'P421S8', 'P421S8A1', 'P421S9', 'P421S9A1', 'P421S10', 'P421S10A1', 'P8648', 'P550']

    posibles = ['P6320']

    dejar = ['P6426', 'P6595S1', 'P6605S1', 'P6605S1', 'P6623S1', 'P6615S1', 'P6750',
             'P550', 'P3193', 'P8636S1', 'P8648S1', 'P8646S1', 'P8650S1A1', 'P8652S1', 'P8654S1']

    # Se eliminan columnas que no se usarán
    df_fuerza = df_fuerza.drop(columns=eliminar)
    df_fuerza = df_fuerza.drop(columns=posibles)

    # Se reemplazan los nulos según corresponda
    df_fuerza = df_fuerza.replace(r'^\s*$', 0, regex=True)
    df_fuerza['P3193'] = df_fuerza['P3193'].replace(0, 2, regex=True)
    df_fuerza = df_fuerza.astype(int)

    # Se agregan dos columnas, con el dinero ganado
    df_fuerza['dinero_trabajo'] = df_fuerza['P6595S1'] + df_fuerza['P6605S1'] + \
        df_fuerza['P6623S1'] + df_fuerza['P6615S1'] + df_fuerza['P6750']
    df_fuerza['dinero_extra'] = df_fuerza['P8636S1'] + df_fuerza['P8646S1'] + \
        df_fuerza['P8648S1'] + df_fuerza['P8650S1A1'] + \
        df_fuerza['P8652S1'] + df_fuerza['P8654S1']

    # Se eliminan columnas que no se usarán
    df_fuerza = df_fuerza.drop(columns=['P6595S1', 'P6605S1', 'P6623S1', 'P6615S1',
                                        'P6750', 'P8636S1', 'P8646S1', 'P8648S1', 'P8650S1A1', 'P8652S1', 'P8654S1'])

    edad_max_ninxs = 12
    edad_min_abuelxs = 60

    # Se crean 3 columnas, número de niñxs en el hogar, número de adultxs en el hogar, número de abuelxs en el hogar
    df_num_ninxs = df[df['P6040'] <= edad_max_ninxs].groupby(
        ['DIRECTORIO'])['DIRECTORIO'].count().reset_index(name='count')
    df_num_abuelxs = df[df['P6040'] >= edad_min_abuelxs].groupby(
        ['DIRECTORIO'])['DIRECTORIO'].count().reset_index(name='count')
    df_num_dif = df.loc[df['P6040'].gt(edad_max_ninxs) & df['P6040'].lt(edad_min_abuelxs)].groupby([
        'DIRECTORIO'])['DIRECTORIO'].count().reset_index(name='count')

    df = pd.merge(df, df_num_ninxs, on=['DIRECTORIO'], how='inner')
    df = pd.merge(df, df_num_abuelxs, on=['DIRECTORIO'], how='inner')
    df = pd.merge(df, df_num_dif, on=['DIRECTORIO'], how='inner')

    df.columns = ['DIRECTORIO', 'SECUENCIA_ENCUESTA', 'P6020', 'P6040', 'P5502', 'P6071',
                  'P6081', 'P6083', 'P6080', 'P1895', 'P1896', 'P1897', 'P1898', 'P1899', 'P3175', 'prom_satisfaccion', 'num_ninxs', 'num_adultxs', 'num_abuelxs']

    # Se dividen los datos en niñxs y abuelxs

    df_ninxs = df[df['P6040'] <= edad_max_ninxs]
    df_abuelxs = df[df['P6040'] >= edad_min_abuelxs]

    df_ninxs = pd.merge(df_ninxs, df_ti, on=[
        'DIRECTORIO', 'SECUENCIA_ENCUESTA'], how='left')
    df_ninxs = pd.merge(df_ninxs, df_ed, on=[
        'DIRECTORIO', 'SECUENCIA_ENCUESTA'], how='left')
    df_ninxs = pd.merge(df_ninxs, df_sld, on=[
        'DIRECTORIO', 'SECUENCIA_ENCUESTA'], how='left')
    df_ninxs = pd.merge(df_ninxs, df_aten, on=[
        'DIRECTORIO', 'SECUENCIA_ENCUESTA'], how='left')

    df_abuelxs = pd.merge(df_abuelxs, df_ed, on=[
        'DIRECTORIO', 'SECUENCIA_ENCUESTA'], how='left')
    df_abuelxs = pd.merge(df_abuelxs, df_sld, on=[
        'DIRECTORIO', 'SECUENCIA_ENCUESTA'], how='left')
    df_abuelxs = pd.merge(df_abuelxs, df_fuerza, on=[
        'DIRECTORIO', 'SECUENCIA_ENCUESTA'], how='left')

    no_ninxs = ['P5502', 'P6071', 'P8587']
    no_abuelxs = ['P6081', 'P6083']
    df_ninxs = df_ninxs.drop(columns=no_ninxs)
    df_abuelxs = df_abuelxs.drop(columns=no_abuelxs)

    df_ninxs = df_ninxs.drop(columns=['DIRECTORIO', 'SECUENCIA_ENCUESTA'])
    df_abuelxs = df_abuelxs.drop(columns=['DIRECTORIO', 'SECUENCIA_ENCUESTA'])

    df_ninxs[['P171', 'trabaja', 'dinero', 'P6160', 'P772', 'P773']] = \
        df_ninxs[['P171', 'trabaja', 'dinero',
                  'P6160', 'P772', 'P773']].fillna(0)

    df_ninxs['P8586'] = df_ninxs['P8586'].fillna(2)
    df_ninxs['P51'] = df_ninxs['P51'].fillna(8)
    df_ninxs['P771'] = df_ninxs['P771'].fillna(9)
    df_ninxs['actividad'] = df_ninxs['actividad'].fillna(5)

    df_ninxs.to_csv('ninxs.csv', index=False)
    df_abuelxs.to_csv('abuelxs.csv', index=False)
