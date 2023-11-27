import { Box, IconButton, Typography } from "@mui/material";
import StartIcon from "@mui/icons-material/Start";

export interface IMenuPrincipal {
  cambiarMenu: (opcion: number) => void;
}
const MenuPrincipal: React.FC<IMenuPrincipal> = ({ cambiarMenu }) => {
  return (
    <Box>
      <Box
        sx={{
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
          justifyContent: "center",
        }}
      >
        <Typography component="h1" variant="h4">
          Sistema de Recomendacion de Tipos de Carne
        </Typography>
        <Typography component="h2" variant="h5" sx={{ mt: 2 }}>
          Recibe una recomendación que se adapte a lo que quieras cocinar!
        </Typography>
      </Box>
      <Box
        sx={{
          display: "flex",
          flexDirection: "column",
          justifyContent: "center",
          alignItems: "center",
          height: "65%",
        }}
      >
        <Typography component="h3" variant="h3" sx={{ mt: 20 }}>
          Comenzar
        </Typography>
        <IconButton
          onClick={() => cambiarMenu(2)}
          size="large"
          color="success"
          sx={{ width: 150, height: 150 }}
        >
          <StartIcon
            sx={{ width: 150, height: 150, p: 1, borderRadius: 20 }}
          ></StartIcon>
        </IconButton>
      </Box>
    </Box>
  );
};
export default MenuPrincipal
