# Eco13 - DT-APP

¡Bienvenido a **Eco13**! 🌿  
Una app desarrollada con **Streamlit** que te permite visualizar y analizar datos sobre la **calidad del aire en Fundautónoma** (Comuna 13, Cali).  
Esta herramienta busca promover la **ciencia ciudadana** y generar conciencia sobre el impacto ambiental y sanitario de la contaminación del aire.

---

## 🌎 Contexto del Proyecto

**Eco13** surge como respuesta a la crítica situación ambiental en el oriente de Santiago de Cali, donde factores como:

- Congestión vehicular  
- Emisiones industriales  
- Baja cobertura vegetal  

afectan gravemente la **calidad del aire**.

La app permite:

- Visualizar y analizar datos de sensores de bajo costo  
- Identificar patrones de contaminación  
- Proponer soluciones estratégicas basadas en datos

---

## Cómo correr la app

1. Clona este repositorio:

```bash
git clone https://github.com/mdlangeles/DT-APP.git
cd DT-APP
```

2. Activa tu entorno virtual:
```bash
python -m venv venv

```

**En Windows:**
```bash
venv\Scripts\activate
```

**En macOS/Linux:**
```bash
source venv/bin/activate
```

3. Instala las librerías necesarias:
```bash
pip install -r requirements.txt
```

4. Ejecuta la app con Streamlit:
```bash
python -m streamlit run Home.py
```

5. Si gustas ejecutarlo ya con Docker, los pasos recomendados son los siguientes:

**5.1. Abre Docker Desktop** [Docker Downloads](https://www.docker.com/)

**5.2. Construye la imagen:**

```bash
docker build -t dtapp .
```

**5.3. Ejecuta el contenedor:**

```bash
docker run -p 8501:8501 dtapp
```

**5.4. Abre tu navegador en:**  
👉 `http://localhost:8501`

---

## ¿Por qué usar Eco13?

- Datos reales recolectados desde un sensor instalado en Fundautónoma (Comuna 13 del oriente de Cali).  
- Visualización interactiva y clara de los contaminantes (PM2.5, CO₂, NH₃).  
- Enfocado en zonas vulnerables y con escasa cobertura de monitoreo oficial.  
- Fomenta la participación ciudadana y la toma de decisiones informadas.

---

##  ¿Quieres colaborar?

¡Nos encanta recibir aportes!  
Haz un fork del repo, crea una rama, sube tus cambios y abre un Pull Request.  
También puedes sugerir mejoras o nuevas funcionalidades para seguir fortaleciendo el proyecto.

---

## 👩‍💻 Autoras del Proyecto

- María de los Ángeles Amú Moreno [@mdlangeles](https://github.com/mdlangeles)  
- Manuela Mayorga Rojas [@ManuelaMayorga](https://github.com/ManuelaMayorga)  
- Mariana Mera Gutiérrez [@MarianaMera12](https://github.com/MarianaMera12)  

---

## 🔗 Recurso en línea

Accede a la aplicación web en:  
👉 [eco13-923878907217.us-central1.run.app](https://eco13-923878907217.us-central1.run.app)
