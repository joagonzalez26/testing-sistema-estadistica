# Prompts Usados - Testing Asistido por IA 

# Nota personal

En esta etapa también puse en práctica habilidades que vengo desarrollando en Prompt Engineering (certificación en curso), buscando usar la IA de forma más consciente, útil y bien enfocada. La idea no fue “pedirle todo a la IA”, sino aprovecharla como herramienta para pensar mejor simplemente obvio siempre teniendo mejoras y comparaciones :D

## Objetivo
Documentar los prompts utilizados durante la Etapa 3 para ampliar cobertura de pruebas, detectar mejoras, generar ideas de testing y refinar automatizaciones sobre el sistema de Estadística y Probabilidad.

La IA se utilizó como apoyo, no como reemplazo del criterio QA.

---

## Prompt 1 - Generación de casos borde para calculadora

**Objetivo:** descubrir escenarios no cubiertos por los casos positivos y negativos ya ejecutados.

**Prompt usado:**

> Analizá una calculadora estadística web que recibe números separados por comas y calcula media, mediana, moda, varianza y desvío estándar. Ya probé casos válidos, campo vacío y texto inválido. Proponé casos borde y escenarios adicionales desde una perspectiva QA manual y automation QA.

**Resultado esperado del uso del prompt:**
- detectar casos no contemplados
- ampliar cobertura de testing
- generar nuevas ideas para pruebas manuales y automáticas

---

## Prompt 2 - Generación de casos borde para simulador

**Objetivo:** ampliar cobertura sobre entradas válidas e inválidas del simulador de probabilidad.

**Prompt usado:** 

> Analizá un simulador de probabilidad web que recibe probabilidad, cantidad de ensayos y cantidad de simulaciones. Ya probé casos válidos, probabilidad fuera de rango, ensayos inválidos y simulaciones inválidas. Proponé nuevos casos borde, riesgos funcionales y posibles mejoras de validación.

**Resultado esperado del uso del prompt:**
- descubrir escenarios límite
- detectar validaciones faltantes
- generar ideas para nuevas automatizaciones

---

## Prompt 3 - Detección de mejoras QA sobre UX y mensajes

**Objetivo:** identificar inconsistencias entre comportamiento real del sistema y mensajes mostrados al usuario.

**Prompt usado:**

> Desde una perspectiva QA, revisá este comportamiento: el simulador indica en su mensaje que se debe usar punto y no coma, pero internamente convierte coma a punto y acepta ambos formatos. ¿Cómo documentarías esto como bug o mejora? ¿Qué severidad y prioridad le asignarías?

**Resultado esperado del uso del prompt:**
- mejorar el reporte de bugs
- justificar severidad y prioridad
- fortalecer criterio QA

---

## Prompt 4 - Mejora de asserts en automatización

**Objetivo:** refinar automatizaciones Selenium cuando fallan por selectores o validaciones incorrectas.

**Prompt usado:**

> Estoy automatizando una aplicación web con Selenium y uno de mis tests falla porque no encuentra un elemento por ID. Quiero que me ayudes a analizar el error como si fueras un QA automation engineer: identificar si el problema está en el test, en el selector o en el sistema bajo prueba, y proponer una versión más robusta usando waits explícitos.

**Resultado esperado del uso del prompt:**
- corregir scripts
- mejorar estabilidad
- aprender a depurar automatizaciones

---

## Prompt 5 - Comparación entre frameworks

**Objetivo:** comparar Selenium y Robot Framework dentro del mismo proyecto.

**Prompt usado:**

> Compará Selenium y Robot Framework para automatizar pruebas sobre una aplicación web educativa. Quiero una comparación enfocada en legibilidad, velocidad de escritura, mantenimiento, flexibilidad, curva de aprendizaje y utilidad para portfolio como qa

**Resultado esperado del uso del prompt:**
- documentar diferencias entre frameworks
- justificar decisiones de la Etapa 2
- fortalecer la comparación metodológica

---

## Prompt 6 - Comparación entre testing manual y testing asistido por IA

**Objetivo:** analizar qué cambia cuando la IA se usa como apoyo al testing.

**Prompt usado:**

> Compará testing manual tradicional vs testing asistido por IA en un proyecto QA personal. Quiero entender ventajas, limitaciones, riesgos y valor profesional de usar IA para generar casos, detectar mejoras y refinar automatizaciones

**Resultado esperado del uso del prompt:**
- construir la comparación final de la Etapa 3
- identificar ventajas reales de la IA
- dejar una conclusión madura y profesional

---

## Conclusión inicial
Durante esta etapa, la IA se utilizó como apoyo para:

- ampliar cobertura de casos de prueba
- detectar mejoras funcionales y de UX
- sugerir escenarios borde
- refinar automatizaciones
- comparar enfoques de testing
- fortalecer la documentación del proyecto

La decisión final sobre qué probar, cómo documentarlo y cómo automatizarlo siguió dependiendo del criterio de uno mismo, osea del tester.

