// theme.js
import { createTheme } from '@mui/material/styles';

const theme = createTheme({
  palette: {
    primary: {
      main: '#7ED4AD', // Color principal para primary
      light: '#7ED4AD', // Color claro opcional
      dark: '#7ED4AD',  // Color oscuro opcional
      contrastText: '#fff', // Color de texto opcional
    },
    secondary: {
      main: '#ff4081', // Color principal para secondary
      light: '#ff79b0', // Color claro opcional
      dark: '#c60055',  // Color oscuro opcional
      contrastText: '#000', // Color de texto opcional
    },
    error: {
      main: '#f44336',  // Color para mensajes de error
    },
    warning: {
      main: '#ffa726',  // Color para advertencias
    },
    info: {
      main: '#29b6f6',  // Color para información
    },
    success: {
      main: '#66bb6a',  // Color para éxito
    },
    // Puedes agregar colores adicionales personalizados aquí:
    customColor: {
      main: '#ff5722', // Un color personalizado opcional
      contrastText: '#ffffff',
    },
    // Para modo oscuro:
    mode: 'light', // Cambia a 'dark' si necesitas modo oscuro
  },
});

export default theme;
