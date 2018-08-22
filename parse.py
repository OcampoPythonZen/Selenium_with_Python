#! -*- coding: utf-8 -*-
import xlrd

def cargar_MA( nombre_archivo ):
    archivo_excel_nombre = str(nombre_archivo)
    archivo = xlrd.open_workbook( archivo_excel_nombre )
    hoja = archivo.sheet_by_index(0)
    numero_registros = hoja.nrows
    print "Numero de registros en la hoja: %d" % numero_registros
    row = 2
    lista_registros = []
    lista_dicc = []

    while row < numero_registros:
        r1 = hoja.cell_value( rowx=row, colx=1 )
        r2 = hoja.cell_value( rowx=row, colx=2 )
        r3 = hoja.cell_value( rowx=row, colx=3 )
        r4 = hoja.cell_value( rowx=row, colx=4 )
        r5 = hoja.cell_value( rowx=row, colx=5 )
        r6 = hoja.cell_value( rowx=row, colx=6 )
        r7 = hoja.cell_value( rowx=row, colx=7 )
        r8 = hoja.cell_value( rowx=row, colx=8 )
        r9 = hoja.cell_value( rowx=row, colx=9 )
        r10 = hoja.cell_value( rowx=row, colx=10 )
        r11 = hoja.cell_value( rowx=row, colx=11 )
        r12 = hoja.cell_value( rowx=row, colx=12 )
        r13 = hoja.cell_value( rowx=row, colx=13 )
        r14 = hoja.cell_value( rowx=row, colx=14 )
        r15 = hoja.cell_value( rowx=row, colx=15 )
        r16 = hoja.cell_value( rowx=row, colx=16 )
        r17 = hoja.cell_value( rowx=row, colx=17 )
        r18 = hoja.cell_value( rowx=row, colx=18 )
        r19 = hoja.cell_value( rowx=row, colx=19 )
        r20 = hoja.cell_value( rowx=row, colx=20 )
        r21 = hoja.cell_value( rowx=row, colx=21 )
        r22 = hoja.cell_value( rowx=row, colx=22 )
        r23 = hoja.cell_value( rowx=row, colx=23 )
        r24 = hoja.cell_value( rowx=row, colx=24 )
        r25 = hoja.cell_value( rowx=row, colx=25 )
        r26 = hoja.cell_value( rowx=row, colx=26 )
        r27 = hoja.cell_value( rowx=row, colx=27 )
        r28 = hoja.cell_value( rowx=row, colx=28 )
        r29 = hoja.cell_value( rowx=row, colx=29 )
        r30 = hoja.cell_value( rowx=row, colx=30 )
        r31 = hoja.cell_value( rowx=row, colx=31 )
        r32 = hoja.cell_value( rowx=row, colx=32 )
        r33 = hoja.cell_value( rowx=row, colx=33 )
        r34 = hoja.cell_value( rowx=row, colx=34 )
        r35 = hoja.cell_value( rowx=row, colx=35 )

        if r1=="Director":
            r1=1
        elif r1=="Subdirector":
            r1=2
        elif r1=="Docente":
            r1=3
        elif r1.encode('utf-8')=="Asistente Técnico Pedagógico":
            r1=4
        elif r1=="Padres de familia":
            r1=5
        elif r1=="Supervisor":
            r1=6
        #print r1
#------------------------------------------------
        if r2=="Preescolar":
            r2=1
        elif r2=="Primaria":
            r2=2
        elif r2=="Secundaria":
            r2=3
        elif r2=="Media Superior":
            r2=4
#------------------------------------------------
        if r3=="No":
            r3=2
        elif r3.encode('utf-8')=="Sí":
            r3=1
#------------------------------------------------
        if r4=="Ingreso":
            r4=1
        elif r4.encode('utf-8')=="Promoción":
            r4=2
        elif r4=="Reconocimiento":
            r4=3
        elif r4=="Permanencia":
            r4=4
#------------------------------------------------
        if r16=="Temor a perder el empleo":
            r16=1
        elif r16.encode('utf-8')=="Mejor preparación":
            r16=2
        elif r16.encode('utf-8')=="Mejores condiciones laborales y económicas":
            r16=3
#------------------------------------------------
        if r17.encode('utf-8')=="Mejoras en los conocimientos y habilidades proyectadas a la planeación y aplicación":
            r17=1
        elif r17.encode('utf-8')=="Sin ninguna proyección ni resultados en los alumnos":
            r17=2
        elif r17.encode('utf-8')=="Pérdida de tiempo y carga administrativa":
            r17=3
#------------------------------------------------
        if r21.encode('utf-8')=="Sí":
            r21=1
        elif r21=="No":
            r21=2
        elif r21=="Tal vez":
            r21=3
#------------------------------------------------
        if r23.encode('utf-8')=="Sí":
            r23=1
        elif r23=="No":
            r23=2
#------------------------------------------
        if r30.encode('utf-8')=="Sí":
            r30=1
        elif r30=="No":
            r30=2
        elif r30=="Tal vez":
            r30=3
#------------------------------------------
        if r33.encode('utf-8')=="Sí":
            r33=1
        elif r33=="No":
            r33=2
        elif r33=="Tal vez":
            r33=3

        d = {
            'respuesta_1': r1,
            'respuesta_2': r2,
            'respuesta_3': r3,
            'respuesta_4': r4,
            'respuesta_5': r5,
            'respuesta_6': r6,
            'respuesta_7': r7,
            'respuesta_8': r8,
            'respuesta_9': r9,
            'respuesta_10': r10,
            'respuesta_11': r11,
            'respuesta_12': r12,
            'respuesta_13': r13,
            'respuesta_14': r14,
            'respuesta_15': r15,
            'respuesta_16': r16,
            'respuesta_17': r17,
            'respuesta_18': r18,
            'respuesta_19': r19,
            'respuesta_20': r20,
            'respuesta_21': r21,
            'respuesta_22': r22,
            'respuesta_23': r23,
            'respuesta_24': r24,
            'respuesta_25': r25,
            'respuesta_26': r26,
            'respuesta_27': r27,
            'respuesta_28': r28,
            'respuesta_29': r29,
            'respuesta_30': r30,
            'respuesta_31': r31,
            'respuesta_32': r32,
            'respuesta_33': r33,
            'respuesta_34': r34,
            'respuesta_35': r35,
            }

        lista_dicc.append(d)
        row += 1

    return lista_dicc
