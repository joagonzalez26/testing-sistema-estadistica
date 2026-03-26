# Reporte de Bugs

## Plantilla

### BUG-001
**Título:** Mensaje del simulador indica que debe usarse punto, pero el sistema acepta coma  
**Módulo:** Simulador de probabilidad  
**Severidad:** Baja  
**Prioridad:** Media  

**Entorno:**  
- Aplicación web local
- Archivo: `simulador.html`
- Fecha: 2026-03-22

**Precondiciones:**  
Estar en la pantalla del simulador.

**Pasos para reproducir:**  
1. Revisar la validación del campo de probabilidad.
2. Ingresar un valor con coma, por ejemplo `0,5`.
3. Ejecutar la simulación con el resto de datos válidos.

**Resultado esperado:**  
Si el mensaje indica “usa punto, no coma”, el sistema no debería aceptar coma.

**Resultado obtenido:**  
El sistema convierte la coma a punto internamente y acepta el valor.

**Evidencia:**  
Revisión del código: `replace(',', '.')`

**Estado:** Abierto


### BUG-002
**Título:** La calculadora muestra todos los valores como moda cuando no existe una moda única  
**Módulo:** Calculadora estadística  
**Severidad:** Baja  
**Prioridad:** Media  

**Entorno:**  
- Aplicación web local
- Archivo: `calculadora.html`
- Fecha: 2026-03-22

**Precondiciones:**  
Estar en la pantalla de la calculadora.

**Pasos para reproducir:**  
1. Ingresar `4,8,15,16,23,42`
2. Presionar `Calcular`

**Resultado esperado:**  
El sistema debería indicar que no existe moda o que la distribución es amodal.

**Resultado obtenido:**  
El sistema muestra todos los valores como moda.

**Evidencia:**  
Resultado esperado por lógica estadística y revisión del algoritmo de frecuencia.

**Estado:** Abierto