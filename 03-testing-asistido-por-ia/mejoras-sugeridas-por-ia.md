# Mejoras Sugeridas por IA

## Objetivo
Registrar mejoras funcionales, de experiencia de usuario y de testing identificadas con apoyo de IA durante la Etapa 3.

¡Estas sugerencias no se consideran automáticamente correctas por venir de una IA. Fueron tomadas como insumo para análisis QA y evaluación crítica! Cualquier tipo de evaluación sigue dependiendo de mi criterio, es decír del humano.

---

## 1. Mejoras sugeridas para la calculadora

### MS-IA-001 — Mostrar “sin moda” cuando no exista una moda única
**Situación observada:**  
Con ciertos conjuntos de datos, la calculadora muestra todos los valores como moda cuando todos tienen la misma frecuencia.

**Ejemplo:**  
`4,8,15,16,23,42`

**Sugerencia de mejora:**  
Cuando todos los valores tengan igual frecuencia, mostrar un mensaje como:
- `Sin moda`
- `Distribución amodal`

**Valor QA:**  
Mejora la claridad estadística y evita interpretaciones confusas.

---

### MS-IA-002 — Mejor manejo visual de listas largas de resultados
**Situación observada:**  
En entradas extensas o con muchos valores, el bloque de resultados podría volverse poco cómodo de leer.

**Sugerencia de mejora:**  
- mejorar espaciado
- usar mejor jerarquía visual
- separar resultados en bloques o tarjetas

**Valor QA:**  
Mejora usabilidad y legibilidad.

---

### MS-IA-003 — Aceptar y limpiar mejor espacios y separadores
**Situación observada:**  
La calculadora ya tolera ciertos formatos, pero podría robustecerse frente a entradas como:
- espacios múltiples
- comas duplicadas
- mezcla rara de separadores

**Sugerencia de mejora:**  
Agregar una limpieza previa más explícita del input antes de procesarlo.

**Valor QA:**  
Reduce errores de usuario y aumenta tolerancia a entradas reales.

---

### MS-IA-004 — Mensajes de error más específicos
**Situación observada:**  
Actualmente algunos errores son correctos, pero podrían ser más informativos.

**Sugerencia de mejora:**  
Distinguir mejor entre:
- campo vacío
- texto inválido
- formato incompleto
- mezcla de datos válidos e inválidos

**Valor QA:**  
Mejora experiencia de uso y claridad funcional.

---

## 2. Mejoras sugeridas para el simulador

### MS-IA-005 — Corregir inconsistencia entre mensaje y comportamiento real
**Situación observada:**  
El simulador indica que se debe usar punto y no coma, pero internamente convierte coma a punto y acepta ambos formatos.

**Sugerencia de mejora:**  
Elegir una de estas dos opciones:
1. permitir ambos y corregir el mensaje
2. exigir solo punto y validar en consecuencia

**Valor QA:**  
Mejora consistencia entre UX y comportamiento real del sistema.

---

### MS-IA-006 — Validaciones más explícitas para ensayos y simulaciones
**Situación observada:**  
El sistema valida bien muchos casos, pero podría hacer más claros los mensajes.

**Sugerencia de mejora:**  
Separar mensajes según error:
- valor vacío
- valor decimal cuando debe ser entero
- valor menor o igual a cero
- formato inválido

**Valor QA:**  
Facilita al usuario corregir el input.

---

### MS-IA-007 — Explicación breve del resultado teórico vs empírico
**Situación observada:**  
La tabla del simulador funciona, pero podría resultar abstracta para usuarios no técnicos.

**Sugerencia de mejora:**  
Agregar una explicación breve debajo de la tabla, por ejemplo:
- qué representa el valor empírico
- qué representa la PMF teórica
- cómo interpretar diferencias

**Valor QA:**  
Aumenta comprensión del usuario y valor educativo del sistema.

---

### MS-IA-008 — Mejorar feedback visual luego de simular
**Situación observada:**  
El simulador muestra resultados, pero podría reforzarse el feedback visual al terminar.

**Sugerencia de mejora:**  
- mensaje de éxito más visible
- resaltar bloque de resultados
- animación o transición suave

**Valor QA:**  
Mejora experiencia y percepción de respuesta del sistema.

---

## 3. Mejoras sugeridas para navegación e interfaz

### MS-IA-009 — Mayor consistencia visual entre pantallas
**Situación observada:**  
El sistema tiene una estética cuidada, pero algunas pantallas podrían alinearse aún más entre sí en espaciados, botones o estructura visual.

**Sugerencia de mejora:**  
Revisar consistencia de:
- márgenes
- tamaños de botones
- jerarquía de títulos
- alineación de componentes

**Valor QA:**  
Mejora sensación de producto unificado.

---

### MS-IA-010 — Reforzar responsividad básica
**Situación observada:**  
El sistema fue probado principalmente en entorno de escritorio.

**Sugerencia de mejora:**  
Revisar cómo se comporta en:
- ventanas más pequeñas
- resoluciones intermedias
- pantallas reducidas

**Valor QA:**  
Reduce riesgos visuales y mejora robustez de interfaz.

---

### MS-IA-011 — Señalizar mejor el módulo actual
**Situación observada:**  
En ciertos flujos podría ser útil que el usuario identifique más fácilmente en qué sección se encuentra.

**Sugerencia de mejora:**  
Agregar una indicación más clara del módulo actual:
- botón activo
- subtítulo contextual
- breadcrumb simple

**Valor QA:**  
Mejora navegación y orientación del usuario.

---

## 4. Mejoras sugeridas para automatización y testing

### MS-IA-012 — Usar utilidades compartidas en Selenium
**Situación observada:**  
Varios tests repiten la creación del driver y lógica común.

**Sugerencia de mejora:**  
Extraer funciones comunes a:
- `utils.py`
o
- `conftest.py`

**Valor QA:**  
Mejora mantenimiento y escalabilidad de automatizaciones.

---

### MS-IA-013 — Agregar más casos borde automatizados
**Situación observada:**  
La cobertura actual ya es buena, pero todavía pueden sumarse escenarios adicionales.

**Sugerencia de mejora:**  
Automatizar más adelante:
- decimales
- números negativos
- probabilidades límite (`0` y `1`)
- una sola simulación
- un solo valor en calculadora

**Valor QA:**  
Amplía cobertura y fortalece la suite.

---

### MS-IA-014 — Documentar comparación entre frameworks
**Situación observada:**  
Ya se utilizaron Selenium y Robot Framework dentro de la Etapa 2.

**Sugerencia de mejora:**  
Agregar una comparación explícita entre ambos sobre:
- legibilidad
- rapidez de escritura
- facilidad de mantenimiento
- claridad para portfolio

**Valor QA:**  
Aporta valor metodológico al proyecto.

---

## 5. Conclusión
Las mejoras sugeridas por IA fueron útiles principalmente para:

- detectar inconsistencias de UX
- proponer escenarios no contemplados
- mejorar claridad funcional
- fortalecer la mantenibilidad de las automatizaciones
- ampliar la mirada QA más allá de los casos ya ejecutados

