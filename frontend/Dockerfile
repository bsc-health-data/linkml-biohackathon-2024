# Usa la imagen oficial de Node como base
FROM node:20

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el package.json y package-lock.json al directorio de trabajo
COPY package*.json ./

# Instala las dependencias
RUN npm install

# Copia el resto de los archivos de la aplicación al contenedor
COPY . .

# Exponer el puerto 5173 (o el puerto de desarrollo especificado)
EXPOSE 5173

# Comando para iniciar el servidor de desarrollo
CMD ["npm", "run", "dev"]