# Proyecto Django — Sebastián Duarte Ruiz

## Demo en vivo (producción)

https://u3s6-duarte-ruiz-sebastian.onrender.com

## Semana 6 — Autenticación, sesiones y seguridad

Se implementaron las funciones de registro, inicio y cierre de sesión utilizando `django.contrib.auth`. Cada usuario puede consultar, crear, editar y eliminar únicamente sus propios servicios.

## Prueba de aislamiento

Se registraron dos cuentas de prueba: `usuario_a` y `usuario_b`, y se crearon dos servicios con cada una. Al iniciar sesión con `usuario_b`, solo se mostraron sus propios servicios, sin acceder a los de `usuario_a`.

También se intentó editar y eliminar un servicio de `usuario_a` escribiendo directamente su ID en la URL mientras estaba iniciada la sesión de `usuario_b`. En ambos casos, el sistema respondió con un error 404, lo que confirmó la restricción de acceso por propietario.
