# Casos Generados por IA

## Objetivo
Registrar casos de prueba sugeridos con apoyo de IA para ampliar la cobertura del sistema de Estadística y Probabilidad.

Estos casos no reemplazan los ya ejecutados en testing manual ni en automatización, sino que complementan el análisis previo con nuevos escenarios borde, validaciones adicionales y oportunidades de mejora.

# Nota Personal :D

En esta etapa también puse en práctica habilidades que vengo desarrollando en Prompt Engineering (certificación en curso), buscando usar la IA de forma más consciente, útil y bien enfocada. La idea no fue “pedirle todo a la IA”, sino aprovecharla como herramienta para pensar mejor casos!

---

## 1. Casos sugeridos para la calculadora

### CG-IA-001 — Un solo valor numérico
**Objetivo:** validar comportamiento con una lista de un solo número.  
**Datos de prueba:** `5`  
**Resultado esperado:** el sistema debe calcular media, mediana y, según implementación, una varianza/desvío coherente o bien informar el caso especial.

---

### CG-IA-002 — Números repetidos
**Objetivo:** validar que la moda se calcule correctamente cuando sí existe un valor dominante.  
**Datos de prueba:** `2,2,2,3,4,5`  
**Resultado esperado:** la moda debe ser `2`.

---

### CG-IA-003 — Números negativos
**Objetivo:** comprobar si la calculadora procesa correctamente valores negativos.  
**Datos de prueba:** `-5,-2,0,2,5`  
**Resultado esperado:** el sistema debe calcular correctamente los indicadores sin errores.

---

### CG-IA-004 — Números decimales
**Objetivo:** validar funcionamiento con decimales.  
**Datos de prueba:** `1.5,2.5,3.5,4.5`  
**Resultado esperado:** la calculadora debe aceptar decimales y devolver resultados correctos.

---

### CG-IA-005 — Espacios en blanco entre valores
**Objetivo:** validar tolerancia a formato de entrada no limpio.  
**Datos de prueba:** `4, 8, 15, 16, 23, 42`  
**Resultado esperado:** el sistema debería ignorar espacios y procesar correctamente los números.

---

### CG-IA-006 — Comas consecutivas
**Objetivo:** evaluar manejo de separadores duplicados.  
**Datos de prueba:** `4,,8,15,,,16`  
**Resultado esperado:** el sistema debería ignorar entradas vacías o advertir formato incorrecto, sin romperse.

---

### CG-IA-007 — Mezcla de enteros, decimales y texto
**Objetivo:** probar robustez frente a entradas mixtas complejas.  
**Datos de prueba:** `10, 20.5, hola, 30, -, 40.2`  
**Resultado esperado:** debería procesar solo los valores válidos o informar claramente el problema.

---

### CG-IA-008 — Cantidad grande de números
**Objetivo:** observar comportamiento con entrada extensa.  
**Datos de prueba:** lista larga de 30 a 50 valores  
**Resultado esperado:** el sistema debería seguir respondiendo correctamente y mostrar resultados sin errores visuales.

---

## 2. Casos sugeridos para el simulador

### CG-IA-009 — Probabilidad límite inferior
**Objetivo:** validar comportamiento con `p = 0`.  
**Datos de prueba:** `p=0`, `ensayos=10`, `simulaciones=100`  
**Resultado esperado:** todos los resultados empíricos deberían tender a `0 éxitos`.

---

### CG-IA-010 — Probabilidad límite superior
**Objetivo:** validar comportamiento con `p = 1`.  
**Datos de prueba:** `p=1`, `ensayos=10`, `simulaciones=100`  
**Resultado esperado:** todos los resultados empíricos deberían tender a `10 éxitos`.

---

### CG-IA-011 — Un solo ensayo
**Objetivo:** observar comportamiento binomial mínimo.  
**Datos de prueba:** `p=0.5`, `ensayos=1`, `simulaciones=100`  
**Resultado esperado:** los resultados deberían distribuirse entre 0 y 1 éxito.

---

### CG-IA-012 — Una sola simulación
**Objetivo:** validar funcionamiento con mínima cantidad de simulaciones permitidas.  
**Datos de prueba:** `p=0.5`, `ensayos=10`, `simulaciones=1`  
**Resultado esperado:** el sistema debería ejecutar y mostrar una tabla coherente.

---

### CG-IA-013 — Probabilidad con coma
**Objetivo:** validar coherencia entre mensaje y comportamiento real.  
**Datos de prueba:** `p=0,5`, `ensayos=10`, `simulaciones=100`  
**Resultado esperado:** actualmente el sistema lo acepta, aunque el mensaje sugiere usar punto. Esto puede documentarse como inconsistencia UX.

---

### CG-IA-014 — Valores decimales inválidos en ensayos
**Objetivo:** verificar si el sistema rechaza ensayos no enteros.  
**Datos de prueba:** `p=0.5`, `ensayos=10.5`, `simulaciones=100`  
**Resultado esperado:** debería mostrar alerta indicando que el número de ensayos debe ser entero.

---

### CG-IA-015 — Valores decimales inválidos en simulaciones
**Objetivo:** verificar si el sistema rechaza simulaciones no enteras.  
**Datos de prueba:** `p=0.5`, `ensayos=10`, `simulaciones=100.7`  
**Resultado esperado:** debería mostrar alerta indicando que el número de simulaciones debe ser entero.

---

### CG-IA-016 — Campo probabilidad vacío
**Objetivo:** validar control de campo vacío específico.  
**Datos de prueba:** probabilidad vacía, ensayos y simulaciones válidos  
**Resultado esperado:** debería aparecer una alerta o validación clara.

---

### CG-IA-017 — Todos los campos vacíos
**Objetivo:** validar robustez ante formulario completamente vacío.  
**Datos de prueba:** todos los campos vacíos  
**Resultado esperado:** el sistema no debe romperse y debe informar el error al usuario.

---

## 3. Casos sugeridos para interfaz y navegación

### CG-IA-018 — Recarga de página tras mostrar resultados
**Objetivo:** evaluar si al recargar se limpia el estado visual o quedan residuos.  
**Resultado esperado:** la página debería volver a un estado consistente.

---

### CG-IA-019 — Cambio de tamaño de ventana
**Objetivo:** revisar comportamiento visual en tamaños menores.  
**Resultado esperado:** no deberían aparecer elementos superpuestos o ilegibles.

---

### CG-IA-020 — Navegación repetitiva entre módulos
**Objetivo:** comprobar estabilidad básica de navegación.  
**Pasos:** ir varias veces entre inicio, notas, estadística, calculadora y simulador  
**Resultado esperado:** no deberían aparecer errores 404 ni páginas mal cargadas.

---

## 4. Valor de estos casos
Los casos sugeridos por IA aportaron valor principalmente en:

- identificación de escenarios límite
- ampliación de cobertura más allá de los casos iniciales
- detección de inconsistencias de UX
- generación de nuevas ideas para testing manual y automatizado

---

## 5. Conclusión
La IA fue útil para proponer nuevos escenarios, pero la decisión de cuáles son relevantes, cuáles se ejecutan y cómo se documentan siguió dependiendo del análisis humano.

Estos casos sirven como base para:
- futuras pruebas manuales
- nuevas automatizaciones
- mejoras funcionales y de experiencia de usuario