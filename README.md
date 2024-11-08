# Laboratorio: Análisis Estático e Integración Continua

Las herramientas de análisis estático y dinámico te ayudan a mantener el código saludable. En esta recitación, aprenderemos cómo configurar estas herramientas en CI (GitHub Actions).

# Paso 1: Configura tu repositorio de ejemplo en Python

Primero, usa este repositorio de plantilla y úsalo para crear tu propio repositorio.

Ya deberías saber que es un gran error hacer push directamente en la rama `main`. Podemos, de hecho, imponer esta restricción usando [reglas de protección de ramas](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/defining-the-mergeability-of-pull-requests/managing-a-branch-protection-rule). Lee la documentación para entender en qué consisten, y establece las siguientes reglas:

* Requiere una solicitud de pull antes de fusionar en `main`.
* Requiere que las pruebas pasen antes de fusionar en `main`.
* Busca el nombre del trabajo en las verificaciones requeridas (en este caso, `test`). Puede que necesites guardar la configuración primero antes de que aparezca esta caja de búsqueda.

Tu configuración debería verse así.

![](assets/images/branch-protection.png)


Los casos de prueba fallidos ❌ no habrían estado allí si hubiera habilitado estas reglas desde el principio. Ahora, arreglemos nuestra prueba fallida.

# Paso 2: Arregla el CI roto

El ❌ realmente no debería haber estado allí desde el principio si hubiera habilitado estas reglas. Ahora arreglémoslo. Crea una rama a partir de `main` y abre una PR para arreglar el CI roto.

Revisa en la página de Actions para ver qué prueba está fallando. Crea una rama a partir de `main` y abre una PR para arreglar el CI roto. (¡la solución debería ser MUY simple!)

El trabajo `test` debería pasar en tu PR. Haz clic en "Squash and merge"* para fusionar después de que pasen las verificaciones de estado.

*: Es simplemente más limpio que la fusión predeterminada.

# Paso 3: Haz que tu código luzca bonito

¿Las diferentes tamaños de tabulación te están volviendo loco? Usemos una herramienta para estandarizarlos todos. Un formateador de código, una herramienta de análisis estático, ayuda a identificar y corregir problemas de formato en el código. Usemos [black](https://github.com/psf/black) como ejemplo.

Primero, crea otra rama para configurar un formateador de código.

Luego, ejecuta los siguientes comandos para instalarlo localmente y probar su funcionamiento:

* `pipenv install --dev black`: `black` es solo una _dependencia de desarrollo_. Tu paquete realmente no lo utiliza.
* `pipenv run black . --check`:
  * Ejecuta `black` en el directorio actual. `--check` realiza una ejecución de prueba de `black` sin alterar ningún archivo.
  * Observa algunos archivos en la lista.
* `pipenv run black .`:
  * Esto realmente cambiará los archivos.
  * Ejecuta `git diff` para observar los cambios en los archivos.

Usando CI, podemos imponer requisitos de formato utilizando las mismas GH Actions + verificaciones de estado. Para herramientas populares, alguien ya lo ha hecho antes, y puedes reutilizar su flujo de trabajo.

* Ve a [este Action existente de `black` en GH Marketplace](https://github.com/marketplace/actions/run-black-formatter)
* Haz clic en "Use lastest version" para ver qué necesita ser agregado a `.github/workflows/main.yml`
* Agrega otro trabajo llamado “format” al archivo `main.yml` para usar `black` y verificar el formato de los archivos.
* Haz push de tus archivos formateados a la rama y observa que `format` pasa.
* Haz Squash y merge de la PR.

# Paso 4: Agrega cobertura de prueba al flujo de trabajo de CI

Finalmente, también puedes hacer algún análisis dinámico. Ya que estamos usando `pytest`, usemos [`pytest-cov`](https://pytest-cov.readthedocs.io/en/latest/), un plugin que informa sobre la cobertura de pruebas.

Primero, instálalo y prueba usarlo localmente:

* Crea otra rama.
* Instala `pytest-cov` localmente: `pipenv install --dev pytest-cov`
* Ejecuta `pytest` con el informe de cobertura: `pipenv run pytest --cov=app`

Ahora, agreguemos otro trabajo en el flujo de trabajo para informar la cobertura:

* En el flujo de trabajo `test`, modifica la linea correspondiente a `pytest` para  informar la cobertura: `pipenv run pytest --cov`
* Haz push y observa la nueva verificación en ejecución.

## Bonus: informar la cobertura en PRs

El trabajo de cobertura realmente no agrega mucho al flujo de trabajo ahora, ya que no falla. Sin ser demasiado estrictos con la cobertura, al menos podemos mostrar el estado de la cobertura en la PR.

[Alguien ya lo ha hecho](https://github.com/marketplace/actions/pytest-coverage-commentator), por lo que también podemos usarlo en nuestro repositorio. __Pista__: solo deberías necesitar los últimos dos pasos en el flujo de trabajo.

Nota que esta acción solo se ejecutará en flujos de trabajo basados en solicitudes de pull, por lo que deberás modificar tus disparadores.

Si se configura, el trabajo comentará automáticamente en las PRs con la información de cobertura. Obtendrás algo similar a esto:
![](assets/images/coverage-report.png)
