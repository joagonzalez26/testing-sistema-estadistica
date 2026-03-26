# Plan de Pruebas - Sistema de Estadística y Probabilidad

## 1. Introducción
Este documento define el enfoque de testing manual para la aplicación "Sistema de Estadística y Probabilidad", desarrollada como proyecto educativo e interactivo. 

El objetivo de esta etapa es evaluar el sistema desde una perspectiva de QA manual, validando navegación, funcionalidad, usabilidad básica, consistencia visual y comportamiento ante datos válidos e inválidos.

---

## 2. Objetivo
Pensar y trabajar como QA manual, documentando pruebas sobre una aplicación real.

Se busca:
- validar que las funcionalidades principales operen correctamente
- detectar errores funcionales o visuales
- documentar bugs con evidencia
- generar una base sólida para futuras pruebas con Selenium
- dejar trazabilidad profesional en GitHub

---

## 3. Alcance
Se incluyen pruebas manuales sobre los siguientes módulos:

- Inicio
- Notas
- Estadística
- Conceptos
- Teoremas
- Variables
- Calculadora estadística
- Simulador de probabilidad
- Navegación general
- Elementos visuales principales

---

## 4. Fuera de alcance
En esta etapa no se incluyen:

- pruebas automatizadas
- pruebas de performance avanzadas
- pruebas de seguridad
- pruebas cross-browser exhaustivas
- pruebas sobre persistencia de datos o base de datos
- testing de Electron como app de escritorio

---

## 5. Tipos de prueba
Durante esta etapa se realizarán:

- Smoke testing
- Functional testing
- Navigation testing
- UI testing
- Exploratory testing
- Negative testing
- Regression testing básico

---

## 6. Entorno de prueba
- Sistema bajo prueba: Sistema de Estadística y Probabilidad
- Ejecución: navegador web local
- Servidor: Flask local con `python app.py`
- URL base: `http://127.0.0.1:5000/`
- Editor/desarrollo: Visual Studio Code

---

## 7. Criterios de entrada
Para iniciar testing debe cumplirse lo siguiente:

- el sistema debe iniciar sin errores
- la home debe cargar correctamente
- los archivos principales deben estar presentes
- las imágenes y estilos deben renderizarse
- la calculadora y el simulador deben ser accesibles

---

## 8. Criterios de salida
La etapa se considerará cerrada cuando:

- se ejecuten los casos de prueba definidos
- los resultados queden documentados
- los bugs detectados estén registrados
- exista un checklist de regresión básico
- haya capturas de evidencia

---

## 9. Riesgos identificados
- links rotos entre páginas
- botones sin acción real
- validaciones incompletas
- errores visuales según tamaño de pantalla
- resultados incorrectos en cálculos
- manejo deficiente de entradas inválidas

---

## 10. Prioridades de prueba
Alta prioridad:
- acceso al sistema
- navegación principal
- calculadora
- simulador

Media prioridad:
- consistencia visual
- contenido estático
- mensajes y textos

Baja prioridad:
- detalles cosméticos menores sin impacto funcional

---

## 11. Severidad de bugs
- Crítica: impide usar el sistema
- Alta: rompe una funcionalidad importante
- Media: afecta parcialmente una funcionalidad
- Baja: error visual o menor sin bloquear uso

---

## 12. Entregables
- plan de pruebas
- casos de prueba
- ejecución de pruebas
- reporte de bugs
- checklist de regresión
- capturas de evidencia

## 13. Autor

Joaquín Lorenzo Gonzalez

Estudiante de Licenciatura en Informática 
en la Universidad Empresarial Siglo21

