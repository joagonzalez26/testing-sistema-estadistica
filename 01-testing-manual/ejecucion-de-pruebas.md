# Ejecución de Pruebas

## CP-001 — Acceso a la aplicación
**Prioridad:** Alta  
**Estado:** Passed
**Evidencia:** Captura local de ejecución Flask  
**Observaciones:** La aplicación inicia correctamente desde `app.py` y carga la home sin errores visibles.

## CP-002 — Navegación a Notas
**Prioridad:** Alta  
**Estado:** Passed  
**Evidencia:** Revisión de enlace `index.html -> notas.html`  
**Observaciones:** El enlace existe y `notas.html` está presente.

## CP-003 — Volver al inicio desde Notas
**Prioridad:** Alta  
**Estado:** Passed  
**Evidencia:** Revisión de enlace `notas.html -> index.html`  
**Observaciones:** El botón de retorno apunta correctamente a la home.

## CP-004 — Navegación a Estadística
**Prioridad:** Alta  
**Estado:** Passed  
**Evidencia:** Revisión de enlace `index.html -> estadistica.html`  
**Observaciones:** El acceso existe y la página está presente.

## CP-005 — Acceso a Conceptos
**Prioridad:** Media  
**Estado:** Passed  
**Evidencia:** Revisión de `onclick` en `estadistica.html`  
**Observaciones:** El botón apunta correctamente a `conceptos.html`.

## CP-006 — Acceso a Teoremas
**Prioridad:** Media  
**Estado:** Passed  
**Evidencia:** Revisión de `onclick` en `estadistica.html`  
**Observaciones:** El botón apunta correctamente a `teoremas.html`.

## CP-007 — Acceso a Variables
**Prioridad:** Media  
**Estado:** Passed  
**Evidencia:** Revisión de `onclick` en `estadistica.html`  
**Observaciones:** El botón apunta correctamente a `variables.html`.

## CP-008 — Acceso a Calculadora
**Prioridad:** Alta  
**Estado:** Passed  
**Evidencia:** Revisión de `onclick` en `estadistica.html`  
**Observaciones:** El botón apunta correctamente a `calculadora.html`.

## CP-009 — Cálculo correcto con datos válidos
**Prioridad:** Alta  
**Estado:** Passed  
**Evidencia:** Revisión de lógica JS en `calculadora.html`  
**Observaciones:** Con `4,8,15,16,23,42` el sistema debe mostrar: Media `18.00`, Mediana `15.50`, Moda `4, 8, 15, 16, 23, 42`, Varianza `151.67`, Desv. Estándar `12.32`.

## CP-010 — Calculadora con campo vacío
**Prioridad:** Alta  
**Estado:** Passed  
**Evidencia:** Revisión de validación JS  
**Observaciones:** Si el campo está vacío, muestra alerta: `Por favor ingresa algunos números.`

## CP-011 — Calculadora con caracteres no válidos
**Prioridad:** Alta  
**Estado:** Passed  
**Evidencia:** Revisión de validación JS  
**Observaciones:** Si se ingresa `a,b,c`, muestra alerta: `No se reconocieron números válidos.`

## CP-012 — Calculadora con mezcla de números y texto
**Prioridad:** Media  
**Estado:** Passed  
**Evidencia:** Revisión de lógica JS  
**Observaciones:** Si se ingresa `5,10,abc,20`, filtra el texto inválido y procesa solo `5,10,20`.

## CP-013 — Acceso a Simulador
**Prioridad:** Alta  
**Estado:** Passed  
**Evidencia:** Revisión de `onclick` en `estadistica.html`  
**Observaciones:** El botón apunta correctamente a `simulador.html`.

## CP-014 — Simulación válida
**Prioridad:** Alta  
**Estado:** Passed  
**Evidencia:** Revisión de lógica JS en `simulador.html`  
**Observaciones:** Con valores válidos genera mensaje de éxito y tabla de resultados empíricos y teóricos.

## CP-015 — Simulador con probabilidad fuera de rango
**Prioridad:** Alta  
**Estado:** Passed  
**Evidencia:** Revisión de validación JS  
**Observaciones:** Si `p < 0` o `p > 1`, muestra alerta de probabilidad inválida.

## CP-016 — Simulador con ensayos inválidos
**Prioridad:** Alta  
**Estado:** Passed  
**Evidencia:** Revisión de validación JS  
**Observaciones:** Si `n < 1` o no es válido, muestra alerta correspondiente.

## CP-017 — Simulador con simulaciones inválidas
**Prioridad:** Alta  
**Estado:** Passed  
**Evidencia:** Revisión de validación JS  
**Observaciones:** Si `simulaciones < 1` o no es válido, muestra alerta correspondiente.

## CP-018 — Revisión visual básica
**Prioridad:** Media  
**Estado:** Passed
**Evidencia:** Capturas en navegador  
**Observaciones:** Se validó visualmente home, notas, estadística, calculadora y simulador. No se detectaron elementos cortados, superpuestos ni problemas graves de legibilidad. 

## CP-019 — Validación de imágenes principales
**Prioridad:** Media  
**Estado:** Passed 
**Evidencia:** Capturas de home y páginas clave  
**Observaciones:** Las imágenes principales cargan correctamente, incluyendo fondo e imagen de perfil.

## CP-020 — Navegación sin errores 404
**Prioridad:** Alta  
**Estado:** Passed  
**Evidencia:** Revisión estructural de rutas y archivos  
**Observaciones:** No se detectaron enlaces internos rotos en las páginas principales.