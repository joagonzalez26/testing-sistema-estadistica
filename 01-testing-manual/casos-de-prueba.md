# Casos de Prueba - Testing Manual :)

## Reglas de los casos para implementar 
- Estado: Passed / Failed / Blocked
- Prioridad: Alta / Media / Baja

---

## CP-001 - Acceso a la aplicación
**Objetivo:** Verificar que la aplicación cargue correctamente desde Flask.  
**Precondición:** Servidor iniciado con `python app.py`.  
**Pasos:**
1. Abrir `http://127.0.0.1:5000/`
2. Esperar carga completa
**Resultado esperado:** La home carga sin errores, con fondo, sidebar y texto de bienvenida.  
**Prioridad:** Alta

---

## CP-002 - Navegación a Notas
**Objetivo:** Verificar acceso a la sección Notas.  
**Pasos:**
1. Entrar a la home
2. Hacer clic en "Notas"
**Resultado esperado:** Se abre `notas.html` mostrando la tarjeta "Próximamente" y el botón "Volver al inicio".  
**Prioridad:** Alta

---

## CP-003 - Volver al inicio desde Notas
**Objetivo:** Validar retorno desde Notas.  
**Pasos:**
1. Entrar a Notas
2. Hacer clic en "Volver al inicio"
**Resultado esperado:** El usuario vuelve a la home correctamente.  
**Prioridad:** Alta

---

## CP-004 - Navegación a Estadística
**Objetivo:** Verificar acceso al módulo Estadística.  
**Pasos:**
1. Entrar a la home
2. Hacer clic en "Estadística"
**Resultado esperado:** Se abre `estadistica.html` sin errores visuales ni de carga.  
**Prioridad:** Alta

---

## CP-005 - Acceso a Conceptos
**Objetivo:** Verificar acceso desde tarjeta de conceptos.  
**Pasos:**
1. Entrar a `estadistica.html`
2. Hacer clic en "Ir" dentro de "Conceptos básicos"
**Resultado esperado:** Se abre `conceptos.html`.  
**Prioridad:** Media

---

## CP-006 - Acceso a Teoremas
**Objetivo:** Verificar acceso desde tarjeta de teoremas.  
**Pasos:**
1. Entrar a `estadistica.html`
2. Hacer clic en "Ir" dentro de "Teoremas estadísticos"
**Resultado esperado:** Se abre `teoremas.html`.  
**Prioridad:** Media

---

## CP-007 - Acceso a Variables
**Objetivo:** Verificar acceso desde tarjeta de variables.  
**Pasos:**
1. Entrar a `estadistica.html`
2. Hacer clic en "Ir" dentro de "Variables estadísticas"
**Resultado esperado:** Se abre `variables.html`.  
**Prioridad:** Media

---

## CP-008 - Acceso a Calculadora
**Objetivo:** Verificar acceso a calculadora estadística.  
**Pasos:**
1. Entrar a `estadistica.html`
2. Hacer clic en "Calculadora estadística"
**Resultado esperado:** Se abre `calculadora.html`.  
**Prioridad:** Alta

---

## CP-009 - Cálculo correcto con datos válidos
**Objetivo:** Verificar cálculo estadístico con entrada válida.  
**Datos de prueba:** `4,8,15,16,23,42`  
**Pasos:**
1. Entrar a la calculadora
2. Ingresar `4,8,15,16,23,42`
3. Presionar "Calcular"
**Resultado esperado:** Se muestran resultados de media, mediana, moda, varianza y desvío estándar.  
**Prioridad:** Alta

---

## CP-010 - Calculadora con campo vacío
**Objetivo:** Validar comportamiento con input vacío.  
**Pasos:**
1. Entrar a la calculadora
2. Dejar el campo vacío
3. Presionar "Calcular"
**Resultado esperado:** Aparece alerta indicando que se deben ingresar números.  
**Prioridad:** Alta

---

## CP-011 - Calculadora con caracteres no válidos
**Objetivo:** Evaluar manejo de datos inválidos.  
**Datos de prueba:** `a,b,c`  
**Pasos:**
1. Entrar a la calculadora
2. Ingresar `a,b,c`
3. Presionar "Calcular"
**Resultado esperado:** El sistema informa que no se reconocieron números válidos.  
**Prioridad:** Alta

---

## CP-012 - Calculadora con mezcla de números y texto
**Objetivo:** Evaluar tolerancia a entradas mixtas.  
**Datos de prueba:** `5,10,abc,20`  
**Pasos:**
1. Entrar a la calculadora
2. Ingresar `5,10,abc,20`
3. Presionar "Calcular"
**Resultado esperado:** El sistema procesa solo los números válidos y muestra resultados.  
**Prioridad:** Media

---

## CP-013 - Acceso a Simulador
**Objetivo:** Verificar acceso al simulador de probabilidad.  
**Pasos:**
1. Entrar a `estadistica.html`
2. Hacer clic en "Simulador de probabilidad"
**Resultado esperado:** Se abre `simulador.html`.  
**Prioridad:** Alta

---

## CP-014 - Simulación válida
**Objetivo:** Verificar ejecución correcta del simulador.  
**Datos de prueba:** p=0.5 / n=10 / simulaciones=100  
**Pasos:**
1. Entrar al simulador
2. Ingresar `0.5`, `10`, `100`
3. Presionar "Simular"
**Resultado esperado:** Aparece mensaje de simulación completada y una tabla de resultados.  
**Prioridad:** Alta

---

## CP-015 - Simulador con probabilidad fuera de rango
**Objetivo:** Validar control de probabilidad inválida.  
**Datos de prueba:** p=1.5 / n=10 / simulaciones=100  
**Pasos:**
1. Entrar al simulador
2. Ingresar `1.5`, `10`, `100`
3. Presionar "Simular"
**Resultado esperado:** Aparece alerta indicando que la probabilidad debe estar entre 0 y 1.  
**Prioridad:** Alta

---

## CP-016 - Simulador con ensayos inválidos
**Objetivo:** Validar control de ensayos inválidos.  
**Datos de prueba:** p=0.5 / n=0 / simulaciones=100  
**Pasos:**
1. Entrar al simulador
2. Ingresar `0.5`, `0`, `100`
3. Presionar "Simular"
**Resultado esperado:** Aparece alerta indicando que el número de ensayos debe ser entero mayor a 0.  
**Prioridad:** Alta

---

## CP-017 - Simulador con número de simulaciones inválido
**Objetivo:** Validar control de simulaciones inválidas.  
**Datos de prueba:** p=0.5 / n=10 / simulaciones=0  
**Pasos:**
1. Entrar al simulador
2. Ingresar `0.5`, `10`, `0`
3. Presionar "Simular"
**Resultado esperado:** Aparece alerta indicando que el número de simulaciones debe ser entero mayor a 0.  
**Prioridad:** Alta

---

## CP-018 - Revisión visual básica
**Objetivo:** Verificar consistencia visual general.  
**Pasos:**
1. Navegar por home, notas, estadística, calculadora y simulador
2. Revisar fondo, tipografía, botones, espaciados y legibilidad
**Resultado esperado:** No hay elementos cortados, superpuestos o invisibles.  
**Prioridad:** Media

---

## CP-019 - Validación de imágenes principales
**Objetivo:** Verificar carga de imágenes importantes.  
**Pasos:**
1. Entrar a la home
2. Revisar fondo e imagen de perfil
**Resultado esperado:** Las imágenes cargan correctamente.  
**Prioridad:** Media

---

## CP-020 - Navegación sin errores 404
**Objetivo:** Validar que las rutas principales no estén rotas.  
**Pasos:**
1. Navegar entre los módulos principales
2. Confirmar que cada acceso abra página existente
**Resultado esperado:** Ningún acceso principal produce error 404 o pantalla rota.  
**Prioridad:** Alta

---

