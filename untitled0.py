# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 08:31:39 2023

@author: agilgim
"""


from scipy import stats
#import numpy as np
#import matplotlib.pyplot as plt


def impuesto(patrimonio):
    #Reducción base imponible
    tramo = patrimonio - 3000000
    if tramo < 0:
        pagar = 0
    elif 7993.45 > tramo:
        pagar = tramo * 0.0765
    elif 15980.9 > tramo:
        pagar = (tramo - 7993.45) * 0.085
        pagar = 7993.45 * 0.0765 + pagar
    elif 23968.35 > tramo:
        pagar = (tramo - 15980.9) * 0.0935
        pagar = 7993.45 * 0.0765 + pagar
        pagar = (15980.9 - 7993.45) * 0.085 + pagar
    elif 31955.8 > tramo:
        pagar = (tramo - 23968.35) * 0.102
        pagar = 7993.45 * 0.0765 + pagar
        pagar = (15980.9 - 7993.45) * 0.085 + pagar
        pagar = (23968.35 - 15980.9) * 0.0935 + pagar
    elif 39943.25 > tramo:
        pagar = (tramo - 31955.8) * 0.1105
        pagar = 7993.45 * 0.0765 + pagar
        pagar = (15980.9 - 7993.45) * 0.085 + pagar
        pagar = (23968.35 - 15980.9) * 0.0935 + pagar
        pagar = (31955.8 - 23968.35) * 0.102 + pagar
    elif 47930.71 > tramo:
        pagar = (tramo - 47930.71) * 0.119
        pagar = 7993.45 * 0.0765 + pagar
        pagar = (15980.9 - 7993.45) * 0.085 + pagar
        pagar = (23968.35 - 15980.9) * 0.0935 + pagar
        pagar = (31955.8 - 23968.35) * 0.102 + pagar
        pagar = (39943.25 - 31955.8) * 0.1105 + pagar
    elif 55918.16 > tramo:
        pagar = (tramo - 55918.16) * 0.1275
        pagar = 7993.45 * 0.0765 + pagar
        pagar = (15980.9 - 7993.45) * 0.085 + pagar
        pagar = (23968.35 - 15980.9) * 0.0935 + pagar
        pagar = (31955.8 - 23968.35) * 0.102 + pagar
        pagar = (39943.25 - 31955.8) * 0.1105 + pagar
        pagar = (47930.71 - 39943.25) * 0.119 + pagar
    elif 63905.16 > tramo:
        pagar = (tramo - 63905.16) * 0.136
        pagar = 7993.45 * 0.0765 + pagar
        pagar = (15980.9 - 7993.45) * 0.085 + pagar
        pagar = (23968.35 - 15980.9) * 0.0935 + pagar
        pagar = (31955.8 - 23968.35) * 0.102 + pagar
        pagar = (39943.25 - 31955.8) * 0.1105 + pagar
        pagar = (47930.71 - 39943.25) * 0.119 + pagar
        pagar = (55918.16 - 47930.71) * 0.1275 + pagar
    elif 71893.06 > tramo:
        pagar = (tramo - 71893.06) * 0.1445
        pagar = 7993.45 * 0.0765 + pagar
        pagar = (15980.9 - 7993.45) * 0.085 + pagar
        pagar = (23968.35 - 15980.9) * 0.0935 + pagar
        pagar = (31955.8 - 23968.35) * 0.102 + pagar
        pagar = (39943.25 - 31955.8) * 0.1105 + pagar
        pagar = (47930.71 - 39943.25) * 0.119 + pagar
        pagar = (55918.16 - 47930.71) * 0.1275 + pagar
        pagar = (63905.16 - 55918.16) * 0.136 + pagar
    elif 79880.51 > tramo:
        pagar = (tramo - 79880.51) * 0.153
        pagar = 7993.45 * 0.0765 + pagar
        pagar = (15980.9 - 7993.45) * 0.085 + pagar
        pagar = (23968.35 - 15980.9) * 0.0935 + pagar
        pagar = (31955.8 - 23968.35) * 0.102 + pagar
        pagar = (39943.25 - 31955.8) * 0.1105 + pagar
        pagar = (47930.71 - 39943.25) * 0.119 + pagar
        pagar = (55918.16 - 47930.71) * 0.1275 + pagar
        pagar = (63905.16 - 55918.16) * 0.136 + pagar
        pagar = (71893.06 - 63905.16) * 0.1445 + pagar
    elif 119757.66 > tramo:
        pagar = (tramo - 119757.66) * 0.1615
        pagar = 7993.45 * 0.0765 + pagar
        pagar = (15980.9 - 7993.45) * 0.085 + pagar
        pagar = (23968.35 - 15980.9) * 0.0935 + pagar
        pagar = (31955.8 - 23968.35) * 0.102 + pagar
        pagar = (39943.25 - 31955.8) * 0.1105 + pagar
        pagar = (47930.71 - 39943.25) * 0.119 + pagar
        pagar = (55918.16 - 47930.71) * 0.1275 + pagar
        pagar = (63905.16 - 55918.16) * 0.136 + pagar
        pagar = (71893.06 - 63905.16) * 0.1445 + pagar
        pagar = (79880.51 - 71893.06) * 0.153 + pagar
    elif 159634.82 > tramo:
        pagar = (tramo - 159634.82) * 0.187
        pagar = 7993.45 * 0.0765 + pagar
        pagar = (15980.9 - 7993.45) * 0.085 + pagar
        pagar = (23968.35 - 15980.9) * 0.0935 + pagar
        pagar = (31955.8 - 23968.35) * 0.102 + pagar
        pagar = (39943.25 - 31955.8) * 0.1105 + pagar
        pagar = (47930.71 - 39943.25) * 0.119 + pagar
        pagar = (55918.16 - 47930.71) * 0.1275 + pagar
        pagar = (63905.16 - 55918.16) * 0.136 + pagar
        pagar = (71893.06 - 63905.16) * 0.1445 + pagar
        pagar = (79880.51 - 71893.06) * 0.153 + pagar
        pagar = (119757.66 - 79880.51) * 0.1615 + pagar
    elif 239389.12 > tramo:
        pagar = (tramo - 239389.12) * 0.2125
        pagar = 7993.45 * 0.0765 + pagar
        pagar = (15980.9 - 7993.45) * 0.085 + pagar
        pagar = (23968.35 - 15980.9) * 0.0935 + pagar
        pagar = (31955.8 - 23968.35) * 0.102 + pagar
        pagar = (39943.25 - 31955.8) * 0.1105 + pagar
        pagar = (47930.71 - 39943.25) * 0.119 + pagar
        pagar = (55918.16 - 47930.71) * 0.1275 + pagar
        pagar = (63905.16 - 55918.16) * 0.136 + pagar
        pagar = (71893.06 - 63905.16) * 0.1445 + pagar
        pagar = (79880.51 - 71893.06) * 0.153 + pagar
        pagar = (119757.66 - 79880.51) * 0.1615 + pagar
        pagar = (159634.82 - 119757.66) * 0.187 + pagar
    elif 398777.53 > tramo:
        pagar = (tramo - 398777.53) * 0.255
        pagar = 7993.45 * 0.0765 + pagar
        pagar = (15980.9 - 7993.45) * 0.085 + pagar
        pagar = (23968.35 - 15980.9) * 0.0935 + pagar
        pagar = (31955.8 - 23968.35) * 0.102 + pagar
        pagar = (39943.25 - 31955.8) * 0.1105 + pagar
        pagar = (47930.71 - 39943.25) * 0.119 + pagar
        pagar = (55918.16 - 47930.71) * 0.1275 + pagar
        pagar = (63905.16 - 55918.16) * 0.136 + pagar
        pagar = (71893.06 - 63905.16) * 0.1445 + pagar
        pagar = (79880.51 - 71893.06) * 0.153 + pagar
        pagar = (119757.66 - 79880.51) * 0.1615 + pagar
        pagar = (159634.82 - 119757.66) * 0.187 + pagar
        pagar = (239389.12 - 159634.82) * 0.2125 + pagar
    elif 797555.07 > tramo:
        pagar = (tramo - 797555.07) * 0.3175
        pagar = 7993.45 * 0.0765 + pagar
        pagar = (15980.9 - 7993.45) * 0.085 + pagar
        pagar = (23968.35 - 15980.9) * 0.0935 + pagar
        pagar = (31955.8 - 23968.35) * 0.102 + pagar
        pagar = (39943.25 - 31955.8) * 0.1105 + pagar
        pagar = (47930.71 - 39943.25) * 0.119 + pagar
        pagar = (55918.16 - 47930.71) * 0.1275 + pagar
        pagar = (63905.16 - 55918.16) * 0.136 + pagar
        pagar = (71893.06 - 63905.16) * 0.1445 + pagar
        pagar = (79880.51 - 71893.06) * 0.153 + pagar
        pagar = (119757.66 - 79880.51) * 0.1615 + pagar
        pagar = (159634.82 - 119757.66) * 0.187 + pagar
        pagar = (239389.12 - 159634.82) * 0.2125 + pagar
        pagar = (398777.53 - 239389.12) * 0.255 + pagar
    else:
        pagar = (tramo - 797555.07) * 0.365
        pagar = 7993.45 * 0.0765 + pagar
        pagar = (15980.9 - 7993.45) * 0.085 + pagar
        pagar = (23968.35 - 15980.9) * 0.0935 + pagar
        pagar = (31955.8 - 23968.35) * 0.102 + pagar
        pagar = (39943.25 - 31955.8) * 0.1105 + pagar
        pagar = (47930.71 - 39943.25) * 0.119 + pagar
        pagar = (55918.16 - 47930.71) * 0.1275 + pagar
        pagar = (63905.16 - 55918.16) * 0.136 + pagar
        pagar = (71893.06 - 63905.16) * 0.1445 + pagar
        pagar = (79880.51 - 71893.06) * 0.153 + pagar
        pagar = (119757.66 - 79880.51) * 0.1615 + pagar
        pagar = (159634.82 - 119757.66) * 0.187 + pagar
        pagar = (239389.12 - 159634.82) * 0.2125 + pagar
        pagar = (398777.53 - 239389.12) * 0.255 + pagar
        pagar = (797555.07 - 398777.53) * 0.3175 + pagar
    return pagar




#Valores iniciales
ahorro_previo = 100000
qx = 0.005
edad = 25
pago_total = 0
ahorro_nuevo = 0
ahorro = 0

# Parametrizando la gamma
a_ing = 0 # valor de inicio, mínimo
alpha_ing = 1.7 # parametro de forma. Beta
beta_ing = 1000 # parametro de escala. Gamma
a_gas = 2000 # valor de inicio, mínimo
alpha_gas = 1.6 # parametro de forma. Beta
beta_gas = 1000 # parametro de escala. Gamma

#calculando ahorro
ingresos = stats.gamma.rvs(alpha_ing, loc=a_ing, scale=beta_ing)
gastos_p = stats.gamma.cdf(ingresos, alpha_ing, loc=a_ing, scale=beta_ing)
gastos = stats.gamma.ppf(gastos_p, alpha_gas, loc=a_gas, scale=beta_gas)
ahorro = ingresos - gastos


while edad <120:
    #ahorro acumulado
    ahorro = ahorro_previo + ahorro
    pago = impuesto(ahorro)
    pago = qx * pago
    
    #año proximo
    incremento_renta = 1.02
    incremento_gasto = 1.02
    incremento_ahorro = 1.02
    ingresos = ingresos * incremento_renta
    gastos = gastos * incremento_gasto
    ahorro = ahorro * incremento_ahorro
    ahorro_nuevo = ingresos - gastos
    ahorro = ahorro + ahorro_nuevo
    pago_total = pago_total + pago
    
    edad += 1





























