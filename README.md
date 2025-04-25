# Spark-Clase

Proyecto integral para la materia de Big Data.

Este repositorio contiene un entorno reproducible basado en Docker para administrar Spark y trabajar con análisis de datos (PySpark), facilitando la descarga de datasets de Kaggle y el análisis exploratorio (EDA).

---

## **Instrucciones para levantar el entorno y replicar el proyecto**

### 1. **Clonar el repositorio**

```bash
git clone https://github.com/Son-Of-Fry/Spark-Clase.git
cd Spark-Clase
```




### 2. **Configurar la API de Kaggle**

	1.	Crea una cuenta en Kaggle si no tienes una.
	2.	Ve a My Account y haz clic en Create New API Token.
	3.	Descarga el archivo kaggle.json.
	4.	Coloca kaggle.json en la ruta: 
        
        .kaggle/kaggle.json
        
        (Si la carpeta .kaggle no existe, créala en la raíz del proyecto)



### 3. **Levantar el contenedor Docker**
```bash
docker-compose up -d --build
```
Esto instalará todas las dependencias y levantará un entorno Jupyter Lab en el puerto 8891 ( puedes cambiar el puerto en el docker-compose.yml si ya está ocupado).



### 4. **Conectarse al contenedor y trabajar el proyecto**
	•	Abre http://localhost:8891 en tu navegador para usar Jupyter Lab dentro del contenedor.
	•	O usa VS Code con la extensión “Remote - Containers” para abrir y editar los archivos dentro del contenedor.



### 5. **Descargar el dataset de Kaggle**

Dentro del contenedor, ejecuta:

```python
python src/download_data.py
```

Esto descargará el dataset y lo dejará listo en data/raw/.



### 6. **Explorar los datos (EDA)**

Abre el notebook:

notebooks/EDA.ipynb

y ejecuta las celdas para analizar la estructura y estadísticas iniciales de los datos.



## 📁 **Estructura recomendada del proyecto**
```
Spark-Clase/
│
├── .kaggle/
│   └── kaggle.json
├── data/
│   ├── processed/
│   └── raw/
├── notebooks/
│   └── EDA.ipynb
├── src/
│   └── download_data.py
├── requirements.txt
├── docker-compose.yml
├── .gitignore
└── README.md
```




## 📋 **Notas y buenas prácticas**
	•	Los datos y archivos .kaggle/ están en .gitignore y no deben subirse al repositorio.
	•	Modifica los paths en notebooks/scripts según la ubicación de los datos.
	•	Si tienes problemas de RAM o espacio, descarga los archivos grandes de Kaggle uno por uno, no el ZIP completo.
	•	Si el puerto 8891 está ocupado, edítalo en docker-compose.yml.

---

¿Dudas? Revisa los comentarios en los notebooks o pregunta al responsable del repositorio.

Equipo de la maestria.

Esta data es de Kaggle, no se tiene ninguna propiedad sobre la data.

---
